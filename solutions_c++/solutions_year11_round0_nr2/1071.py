#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int main() 
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int tc, n;

	fin >> tc;

	REP(t,tc) {
		vector <string> c, o;
		string s, res = "";

		fin >> n;

		REP(i,n) {
			fin >> s;
			c.push_back(s);
		}

		fin >> n;

		REP(i,n) {
			fin >> s;
			o.push_back(s);
		}

		fin >> n;
		fin >> s;

		REP(i,n) {
			if (res.empty()) {
				res += s[i];
			} else {
				bool cmb = false;
				REP(j,c.size()) {
					if ( (c[j][0] == res[res.size()-1] && c[j][1] == s[i]) || (c[j][1] == res[res.size()-1] && c[j][0] == s[i]) ) {
						res[res.size()-1] = c[j][2];
						cmb = true;
						break;
					}
				}
				if (!cmb) {
					REP(j,o.size()) if ( (o[j][0] == s[i] && res.find(o[j][1]) != string::npos) || (o[j][1] == s[i] && res.find(o[j][0]) != string::npos) ) {
						res = "";
						break;
					}
					if (res != "") res += s[i];
				}
			}
		}

		fout << "Case #" << t+1 << ": ";
		fout << "[";
		REP(i,res.size()) {
			if (i > 0) fout << ", " << res[i];
			else fout << res[i];
		}
		fout << "]" << endl;
	}

	fout.close();

	return 0;
}