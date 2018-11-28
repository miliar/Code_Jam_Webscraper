#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define DBGV(_v) { cout << #_v << endl; REP(_i, _v.size()) { cout << _v[_i] << "\n";} cout << endl;} 
typedef pair<int,int> PII;
#define OK(x, y) (x>=0 && y>=0 && x<h && y<w)
#define INF (int)1e6
#define sz size()
#define isLower(c) (c >= 'a' && c <= 'z')

int main() {
	int l = GI, d = GI, kases = GI;
	vector <string> dict;
	string t;
	REP(i, d) {
		cin >> t;
		dict.push_back(t);
	}
	sort(dict.begin(), dict.end());
	REP(kase, kases) {
		vector <string> word(16, ""), words(d, "");
		string in;
		cin >> in;
		int pos = 0, res = 0;
		bool inside = false;
		string r = "";
		REP(i, in.sz) {
			if (in[i] == '(') {
				inside = true;
			}
			else if (in[i] == ')') {
				inside = false;
				word[pos] = r;
				pos++;
				r = "";
			}
			else if (inside == true) {
				r += in[i];			
			}
			else {
				word[pos] = in[i];
				pos++;
			}
		}

		int cnt = 0;		
		REP(i, dict.sz) {
			REP(j, l) {
				REP(k, word[j].sz) {
					if (dict[i][j] == word[j][k]) {
						words[i] += dict[i][j];
					}
				}
			}
		}
		
		//DBGV(words);
		
		REP(i, d) {
			if (words[i].sz == l) res++;
		}
		printf("Case #%d: %d\n", kase+1, res);
	}
}
