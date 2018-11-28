#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

//#define ofs cout

typedef long long ll;

vector<set<int> > match;
VS words;
vector<VS > patterns;

void testcase(int tst)
{
	int l, d, n;

	ifs >> l >> d >> n;

	match.clear();
	words.clear();
	patterns.clear();

	words.assign(d, "");
	REP(i, d)
		ifs >> words[i];

	

	REP(i, n) {

		VS curpat;
		string pattern;
		ifs >> pattern;
		REP(j, pattern.sz) {
			if (pattern[j] == '(') {
				string curmask = "";
				int k = j+1;
				do {
					curmask += pattern[k];
					k++;
				} while (pattern[k] != ')');
				j = k;
				curpat.pb(curmask);
			} else {
				string curs = "";
				curs += pattern[j];
				curpat.pb(curs);
			}
		}
		patterns.pb(curpat);
	}

	match.assign(n, set<int>());

	REP(pt, n) {
		REP(wr, d) {
			match[pt].insert(wr);
		}
	}

	REP(i, l) {
		vector<set<int> > newmatch(n, set<int>());
		REP(pt, n) {
			REP(wr, d) {
				if (match[pt].find(wr) != match[pt].end()) {
					REP(j, patterns[pt][i].sz) {
						if (patterns[pt][i][j] == words[wr][i]) {
							newmatch[pt].insert(wr);
							break;
						}
					}
				}
			}
		}
		match = newmatch;
	}
	
	REP(i, n) {
		ofs << "Case #" << i+1 << ": " << match[i].sz << endl;
	}
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	testcase(1);
//	int t;
//	ifs >> t;
//	REP(tn, t)
//	{
//		testcase(tn);
//	}

	return 0;
} 
