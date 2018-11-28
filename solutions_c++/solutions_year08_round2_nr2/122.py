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

#define FOR(i,a,b) for (int i = (int)a; i < (int)b; ++i)
#define REP(i,a) FOR(i,0,a)
#define ALL(a) a.begin(),a.end()
#define SIZE(a) (int)((a).size())
#define PB push_back
#define FILL(a) memset(&a,0,sizeof(a))
typedef long long LL;

using namespace std;

bool con[1001][1001];
bool isp[1001];
int a,b;

void dfs(int nom){
	isp[nom]=true;
	FOR(i,a,b+1){
		if (!isp[i]&&con[nom][i]) dfs(i);
	}
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	bool primes[2000];
	FILL(primes);
	FOR(i,2,1001){
		bool fl=true;
		FOR(j,2,i){
			if (i%j==0) fl=false;
		}
		primes[i]=fl;
	}
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		int p;
		cin>>a>>b>>p;
		FILL(con);
		FOR(i,a,b+1){
			FOR(j,i,b+1){
				FOR(i2,p,min(i,j)+1){
					if (primes[i2]&&(i%i2==0)&&(j%i2==0)){
						con[i][j]=true;
						con[j][i]=true;
						break;
					}
				}
			}
		}
		FILL(isp);
		int res=0;
		FOR(i,a,b+1){
			if (!isp[i]){
				dfs(i);
				++res;
			}
		}
		printf("Case #%d: %d\n",it+1,res);
	}
}