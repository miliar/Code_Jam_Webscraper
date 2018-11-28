#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int l, d;
string dic[10000];
bool can[100][28];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	cin >> l >> d >> tc;
	getline(cin, dic[0]);
	REP(i,d)
		getline(cin, dic[i]);
	REP(it,tc){
		string s;
		getline(cin, s);
		FILL(can);
		int cur = 0;
		REP(i,l){
			if (s[cur] == '('){
				++cur;
				while (s[cur] != ')'){
					can[i][s[cur]-'a'] = true;
					++cur;
				}
				++cur;
			}
			else{
				can[i][s[cur]-'a'] = true;
				++cur;
			}
		}
		int ans = 0;
		REP(i,d){
			bool fl = true;
			REP(j,l)
				fl &= can[j][dic[i][j]-'a'];
			ans += fl;
		}
		printf("Case #%d: %d\n", it+1, ans);
	}
}
