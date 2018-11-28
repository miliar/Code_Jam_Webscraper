#define TSK "c"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ll long long
#define db double
#define rep(i,n) for(int (i) = 0;  (i) < (n); ++ (i))
#define forn(i,a,n) for(int (i) = (a);  (i) < (n); ++ (i))
#define tr(i,a) for(__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define PI pair<int,int>
#define fi first
#define se second
#define VPI vector<PI >
#define VVPI vector<VPI >
#define VI vector<int>
#define VII vector<VI >
#define VB vector<bool> 
#define VD vector<db>
#define VS vector<string>
#define INF 1000000000
#define deb(x) cerr <<"[line: " << __LINE__ << "] " #x " = " << x << endl
#define NONE 
int main(){
	int T;
	cin >> T;
	string s;
	rep(qwe,T){
		vector<vector<char> > comb(256, vector<char>(256, 0));
		vector<vector<bool> > oppo(256, vector<bool>(256, 0));
		int t;
		cin >> t;
		rep(i,t){
			cin >> s;
			comb[s[0]][s[1]] = s[2];
			comb[s[1]][s[0]] = s[2];
		}
		cin >> t;
		rep(i,t){
			cin >> s;
			oppo[s[0]][s[1]] = oppo[s[1]][s[0]] = 1;
		}
		vector<char> seq;
		cin >> t;
		cin >> s;
		vector<int> cnt(256,0);
		rep(i,t){
			seq.pb(s[i]);
			if (sz(seq) > 1){
				if (comb[seq[sz(seq) - 2]][seq.back()]){
					seq[sz(seq) - 2] = comb[seq[sz(seq) - 2]][seq.back()];
					seq.pop_back();
				}
				rep(j,sz(seq) - 1)
					if (oppo[seq[j]][seq.back()])
						seq.clear();
			}
		}
		printf("Case #%d: [",qwe + 1);
		rep(i,sz(seq) - 1)
			printf("%c, ", seq[i]);
		if (!seq.empty())
			printf("%c", seq.back());
		printf("]\n");
	}
	return 0;
}