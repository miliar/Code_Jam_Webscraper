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
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	REP(i,T) {
		printf("Case #%d: ",i+1);
		int n,k;
		scanf("%d%d",&n,&k);
		if (k==0) {
			puts("OFF");
		} else {
			if ((k+1)%(1<<n)==0) puts("ON");
			else puts("OFF");
		}
	}
}
