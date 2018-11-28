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

int MOD = 10000;
string phrase = "welcome to code jam";
string s;
int cnt[30][600];

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	getline(cin, s);
	int len = phrase.length();
	REP(it,tc){
		getline(cin,s);
		FILL(cnt);
		int n = s.length();
		REP(i,n)
			if (s[i] == phrase[len-1])
				cnt[len-1][i] = 1;
		for (int i = len-2; i >= 0; --i)
			REP(j,n)
				if (s[j] == phrase[i])
					FOR(k,j+1,n)
						if (s[k] == phrase[i+1]){
							cnt[i][j] += cnt[i+1][k];
							cnt[i][j] %= MOD;
						}
		int ans = 0;
		REP(i,n)
			if (s[i] == phrase[0]){
				ans += cnt[0][i];
				ans %= MOD;
			}
		printf("Case #%d: %04d\n", it+1, ans);
	}
}
