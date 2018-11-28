#include <iostream>
#include <cstring>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,f,t) for(int i=f;i<=t;i++)
using namespace std;

int T,dl,akt;
char ss[100]; 
 
int lis[10]={1,0,2,3,4,5,6,7,8,9}; 
int odp[300];
int nowy[100];
 
void wypisz(int z){
	unsigned long long pot=1;
	unsigned long long res=0;
	for(int i=dl-1;i>=0;i--){
		res+=nowy[i]*pot;
		pot*=akt;
	}
	printf("Case #%d: %llu\n",z+1,res);
} 
 
int main(){
	scanf("%d",&T);
	REP(z,T){
		REP(o,300) odp[o]=-1;
		scanf("%s",ss);
		dl=strlen(ss);
		akt=0;
		REP(i,dl){
			if(odp[ss[i]]==-1){
				odp[ss[i]]=lis[akt];
				akt++;
			}
			nowy[i]=odp[ss[i]];
		}
		if(akt==1) akt=2;
		wypisz(z);
	}
	return 0;
}

