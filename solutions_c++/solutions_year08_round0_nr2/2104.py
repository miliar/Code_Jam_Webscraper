#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;i++)
const int maxt=10002;
using namespace std;
int abss[maxt],abt[maxt],bas[maxt],bat[maxt],hh,mm,t,ca,i,j,n,m,ti,ansa,ansb,nowa,nowb;
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&ca);
	fr(t,1,ca){
		memset(abss,0,sizeof(abss));
		memset(abt,0,sizeof(abt));
		memset(bas,0,sizeof(bas));
		memset(bat,0,sizeof(bat));
		scanf("%d%d%d",&ti,&n,&m);
		fr(i,1,n){
			scanf("%d:%d",&hh,&mm);
			abss[hh*60+mm]++;
			scanf("%d:%d",&hh,&mm);
			abt[hh*60+mm+ti]++;
		}
		fr(i,1,m){
			scanf("%d:%d",&hh,&mm);
			bas[hh*60+mm]++;
			scanf("%d:%d",&hh,&mm);
			bat[hh*60+mm+ti]++;
		}
		ansa=ansb=nowa=nowb=0;
		fr(i,0,maxt-1){
			nowa+=bat[i];
			nowb+=abt[i];
			if(nowa<abss[i]){
				ansa+=abss[i]-nowa;
				nowa=abss[i];
			}
			if(nowb<bas[i]){
				ansb+=bas[i]-nowb;
				nowb=bas[i];
			}
			nowa-=abss[i];
			nowb-=bas[i];
		}
		printf("Case #%d: %d %d\n",t,ansa,ansb);
	}
	return 0;
}