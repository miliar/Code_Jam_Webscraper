#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<queue>

using namespace std;

typedef long long LL;

#define FT first
#define SD second
#define MP make_pair
#define PB push_back

int T;
LL xa,xb,xc;
LL ya,yb,yc;
int n,m;
int ca;
LL a;
bool ok=false;

int main(){
	scanf("%d",&T);
	ca=0;
	while(T--){
		ca++;
		scanf("%d %d",&n,&m);
		scanf("%lld",&a);
		printf("Case #%d: ",ca);
		ok=false;
		if((long long)n*(long long)m>=a){
			for(xa=0;xa<=n & !ok;xa++){
				for(xb=0;xb<=n & !ok;xb++){
					for(xc=0;xc<=n & !ok;xc++){
						for(ya=0;ya<=m & !ok;ya++){
							for(yb=0;yb<=m & !ok;yb++){
								for(yc=0;yc<=m & !ok;yc++){
									if(a==llabs(xa*yc-xa*yb+xb*ya-xb*yc+xc*yb-xc*ya)){
										ok=true;
										printf("%lld %lld %lld %lld %lld %lld\n",xa,ya,xb,yb,xc,yc);
									}
								}
							}
						}
					}
				}
			}
		}
		if(!ok) printf("IMPOSSIBLE\n");
	}
	return 0;
}

