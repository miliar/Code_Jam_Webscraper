#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define MP make_pair

const int infinity = (int)1e+8;
const int bufSize = 200;
char buf[bufSize + 1];

int main() {
	int n;
	fin >> n;
	for (int i = 0; i < n; i++) {
		int s;
		fin >> s;
		fin.ignore(bufSize, '\n');
		vector <string> search(s);
		for (int j = 0; j < s; j++) {
			fin.getline(buf, bufSize);
			search[j] = buf;
		}
		int q;
		fin >> q;
		fin.ignore(bufSize, '\n');
		vector <string> query(q);
		for (int j = 0; j < q; j++) {
			fin.getline(buf, bufSize);
			query[j] = buf;
		}
		map <string, int> changes;
		for (int j = 0; j < s; j++)
			changes.insert(MP(search[j], 0));
		for  (int j = 0; j < q; j++) {
			map <string, int> changesNew;
			for (int k = 0; k < s; k++) {
				if (search[k] != query[j]) {
					int best = changes[search[k]];
					for (int l = 0; l < s; l++)
						if (l != k)
							best = min(best, changes[search[l]] + 1);
					changesNew[search[k]] = best;
				}
			}
			changesNew[query[j]] = infinity;
			changes = changesNew;
		}
		int ans = infinity;
		for (int j = 0; j < s; j++)
			ans = min(ans, changes[search[j]]);
		fout << "Case #" << (i + 1) << ": " << ans << endl;
		cout << "Case #" << (i + 1) << ": " << ans << endl;
	}
	return 0;
}