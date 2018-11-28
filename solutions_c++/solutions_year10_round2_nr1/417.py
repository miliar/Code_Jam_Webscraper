#include "bignum.h"
#include<iostream>
#include<list>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>
#include<algorithm>
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,a,b) for(i=(a);i<(b);++i)
#define PB push_back
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<LL> VLL;
const int dx[]={-1,0,1,0,-1,-1,1,1};
const int dy[]={0,1,0,-1,-1,1,-1,1};
char s[100010];
map<string,bool> mp;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int _T,T;
	scanf("%d",&_T);
	REP(T,_T) {
		printf("Case #%d: ",T+1);
		int n,m;
		scanf("%d%d\n",&n,&m);
		int i,j;
		mp.clear();
		REP(i,n) {
			gets(s);
			int l=strlen(s);
			FOR(j,1,l) {
				if (s[j]=='/') {
					mp[string(s+1,s+j)]=true;
//					if (!mp[string(s+1,s+j)]) {
//						mp[string(s+1,s+j)]=true;
//					}
				}
			}
			mp[string(s+1,s+l)]=true;
		}
		int cnt=0;
		REP(i,m) {
			gets(s);
			int l=strlen(s);
			FOR(j,1,l+1) {
				if (j==l || s[j]=='/') {
					if (!mp[string(s+1,s+j)]) {
						mp[string(s+1,s+j)]=true;
						++cnt;
					}
				}
			}
		}
		printf("%d\n",cnt);
	}
}
