#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define R 10010
using namespace std;
typedef long long int LL;
int n,L,H;
int tab[R];
LL NWD(LL a,LL b){
	while(a*b) a>b?a%=b:b%=a;
	return a+b;
}
/*int main(){
	int Z;
	scanf("%d",&Z);
	FORQ(packs,1,Z){
		scanf("%lld%lld%lld",&n,&L,&H);
		FOR(i,0,n)scanf("%lld",&tab[i]);
		sort(tab,tab+n);
		bool fail=true;
		LL out;
		FOR(i,0,n){
			LL b=tab[0], e=tab[i];
			FOR(j,1,n){
				if(j==i)continue;
				if(j<i)b=NWD(b,tab[j]);
				else e=NWD(e,tab[j]);
			}
			LL temp=1;
			if(i>0){
				FOR(j,0,i)temp*=tab[j];
				b=temp/b;
			}
			else b=e;
			if((e%b==0)&&b>=L&&b<=H){
				fail=false;
				out=b;
				break;
			}
		}
		printf("Case #%d: ",packs);
		if(fail)printf("NO\n");
		else printf("%lld\n",out);
	}
	return 0;
}*/

int main(){
	int Z;
	scanf("%d",&Z);
	FORQ(packs,1,Z){
		scanf("%d%d%d",&n,&L,&H);
		FOR(i,0,n)scanf("%d",&tab[i]);
		int out=-1;
		FORQ(i,L,H){
			bool fail=false;
			FOR(j,0,n){
				if(max(tab[j],i)%min(tab[j],i)!=0){fail=true;break;}
			}
			if(!fail){out=i;break;}
		}
		if(out==-1)printf("Case #%d: NO\n",packs);
		else printf("Case #%d: %d\n",packs,out);
	}
	return 0;
}