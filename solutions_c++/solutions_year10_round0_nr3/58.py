#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
using namespace std;


int vez[1001][1001];
int group[1001];
long long acumulado[1000002];
int r,k,n;

typedef long long ll;

ll calcula(int&le,int&ri){
	ll cap=k;
	le=(ri+1)%n;
	int comido=0;
	while(comido<n&&cap-group[(ri+1)%n]>=0){
		ri=(ri+1)%n;
		cap-=group[ri];
		comido++;
	}
	return k-cap;
}

int main(){	
	int tt; cin>>tt;
	for(int t=1;t<=tt;t++){
		scanf("%d %d %d",&r,&k,&n);
		for(int i=0;i<n;i++) scanf("%d",&group[i]);
		
		for(int i=0;i<n;i++) for(int j=0;j<n;j++) vez[i][j]=-1;
		
		acumulado[0]=0;
		int le=n-1,ri=n-1;
		int init=-1,len=-1;
		for(int rep=1;rep<=min(n*n+1,r);rep++){
			long long toma=calcula(le,ri);
			
			acumulado[rep]=acumulado[rep-1]+toma;
			if(vez[le][ri]==-1) vez[le][ri]=rep;
			else{
				len=rep-vez[le][ri];
				init=vez[le][ri];
				break;
			}
		}
		
		printf("Case #%d: ",t);
		
		if(len==-1){
		 	printf("%lld\n",acumulado[r]);
		}else{
			ll res=acumulado[init]+
					(((r-init)/len)*(acumulado[init+len]-acumulado[init]))+
					(acumulado[init+(r-init)%len]-acumulado[init]);	
			printf("%lld\n",res);
		}
	}
}

