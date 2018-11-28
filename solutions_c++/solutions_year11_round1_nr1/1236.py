#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define lli long long
#define ull unsigned long long
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define pii pair<int,int>

int main(){
	int casos;
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
		lli n,pd,pg;
		scanf("%lld %lld %lld",&n,&pd,&pg);
		int da=0;
		for(lli d=1;d<=n;d++){
			if(pg==pd && (d*pd)%100==0)da=1;
			for(lli b =1;b<=1000;b++){
				if( (d*pd)%100)continue;
				//printf("d*(pd-pg):%lld b:%lld\n",(d*(pd-pg)),b);
				if((d*(pd-pg))%b)
					continue;
				lli pg1 = pg - d*(pd-pg)/b; 
				if(pg1<0||pg1>100)continue;
				da=1;
				//printf("porra\n");
				//printf("%lld %lld %lld\n",d,b,pg1);
			}
		}
		if(da)
		printf("Case #%d: Possible\n",caso);
		else printf("Case #%d: Broken\n",caso);
	}	
	return 0;
}

