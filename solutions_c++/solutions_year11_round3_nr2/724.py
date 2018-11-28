#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define R 1010
using namespace std;
int l,t,n,c;
long long d[R];
long long dpref[R];
int main(){
	int Z;
	scanf("%d",&Z);
	FORQ(packs,1,Z){
		scanf("%d%d%d%d",&l,&t,&n,&c);
		FOR(i,0,c)scanf("%lld",&d[i]);
		dpref[0]=0;
		FORQ(i,1,n)dpref[i]=dpref[i-1]+d[(i-1)%c];
		if(l==0){printf("Case #%d: %d\n",packs,dpref[n]*2);continue;}
		long long out=-1;
		FOR(i,0,n){
			FOR(j,(l==1?i:i+1),n){
				long long cz=0;
				cz+=dpref[i]*2;
				if(t<=cz){
					cz+=dpref[i+1]-dpref[i];
				}
				else {
					if((t-cz)%2){break;}
					cz+=min((dpref[i+1]-dpref[i])*2,
								(t-cz)+dpref[i+1]-dpref[i]-(t-cz)/2);
				}
				if(l==2){
					cz+=(dpref[j]-dpref[i+1])*2;
					if(t<=cz){
						cz+=dpref[j+1]-dpref[j];
					}
					else {
						if((t-cz)%2){break;}
						cz+=min((dpref[j+1]-dpref[j])*2,
							(t-cz)+dpref[j+1]-dpref[j]-(t-cz)/2);
					}
					cz+=(dpref[n]-dpref[j+1])*2;
				}
				else cz+=(dpref[n]-dpref[i+1])*2;
				if(out==-1)out=cz;
				else out=min(out,cz);
				if(l==1)break;
			}
			//if(l==1)break;
		}
		printf("Case #%d: %lld\n",packs,out);
	}
	return 0;
}