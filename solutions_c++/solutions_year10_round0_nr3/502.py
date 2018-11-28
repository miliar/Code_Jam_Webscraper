//Jakub Sygnowski
#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(I,N) for(int I=0;I<(N);I++)
#define F first
#define S second
//#define DEBUG
int t,n,tab[1007],r,k,zero;
pair<long long,int> cykl[1007]; //F - zysk, S- obrotow
long long sum,ts;
int main(){
	scanf("%d",&t);
	for(int nr=0;nr<t;nr++){
		printf("Case #%d: ",nr+1);
		scanf("%d%d%d",&r,&k,&n);
		REP(i,n){
		       scanf("%d",&tab[i]);
		       cykl[i].F=0; cykl[i].S=0;
		}
		sum=0;ts=0;zero=n-1;
		for(int c=0;r;c=(c+1)%n){
#ifdef DEBUG
			printf("c=%d r=%d sum=%lld zero=%d\n",c,r,sum,zero);
#endif
			ts+=tab[c];
			if (ts+tab[(c+1)%n]>k||zero==c){ //nastepna grupa sie nie zmiesci
				r--;
				sum+=ts;
				ts=0;
				zero=c;
				if (cykl[c].F){
					cykl[c].S-=r; //teraz w cykl[c].S pamietam, ile trzeba rundek zrobic zeby uzyskac costam
					cykl[c].F=sum-cykl[c].F;
					while(r>=cykl[c].S){
						r-=cykl[c].S;
						sum+=cykl[c].F;
					}
				}
				else {
				cykl[c].F=sum;
				cykl[c].S=r;
				}
			}
		}
		printf("%lld\n",sum);
	}
}

