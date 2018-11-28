#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int l, d, n;
	ifstream fin("a.in");
	ofstream fout("a.out");

	fin >> l >> d >> n;

	vector <string> dict(d);
	for (int word = 0; word < d; word++) fin >> dict[word];

	for (int test = 0; test < n; ++test) {
		string line;
		fin >> line;
		int count = 0;
		for (int k = 0; k < d; ++k) {

			int cur = 0, i = 0;
			bool found = false, opened = false;

			for (i = 0; i < int(line.size()); ++i) {
				if (line[i] == '(') {
					found  = false;
					opened = true;
					continue;
				}
				if (line[i] == ')') {
					if (!found) break;
					opened = false;
					cur++;
					continue;
				}

				if (opened  && line[i] == dict[k][cur]) found = true;


				if (!opened && line[i] != dict[k][cur]) break;
				else if (!opened) cur++;

			}
			if (i == int(line.size())) count++;
		}
		fout << "Case #" << test + 1 << ": " << count << endl;
	}


	fin.close();
	fout.close();
	return 0;
}
