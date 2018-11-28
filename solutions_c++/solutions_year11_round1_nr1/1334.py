#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,N,PD,PG,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d %d %d",&N,&PD,&PG);
		if((PG==100 && PD!=100) || (PG==0 && PD!=0))printf("Case #%d: Broken\n",t);
		else if(N>=100)printf("Case #%d: Possible\n",t);
		else{
			for(i=1;i<=N;i++){
				if(i*PD%100==0)break;
			}
			if(i<=N)printf("Case #%d: Possible\n",t);
			else printf("Case #%d: Broken\n",t);
		}
	}
	
	return 0;
}
