#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
	ifstream fin("input.txt");
	FILE* fout = fopen("output.txt", "w");
	int l, d, n;
	fin>>l>>d>>n;
	vector<string> v(d);
	for (int i = 0; i < d; ++i) 
		fin>>v[i];
	for (int nt = 1; nt <= n; ++nt) {
		string s;
		fin>>s;
		int ret = 0;
		for (int i = 0; i < d; ++i) {
			bool ok = true;
			for (int j = 0, pos = 0; j < l && ok; ++j) {
				int k = pos;
				if (s[pos] == '(') 
					for(; s[pos] != ')'; ++pos);
				else pos++;
				ok = false;
				
				for (; k < pos && !ok; ++k)
					if (v[i][j] == s[k])
						ok = true;

				if (s[pos] == ')') ++pos;
			}
			if (ok) 
				ret++;
		}
		fprintf (fout, "Case #%d: %d\n", nt, ret);
	}
	fclose(fout);
	return 0;
}
