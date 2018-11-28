

#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <list>

using namespace std;

const double eps=1e-8;

int main(){
	list<long> lst;
	long cc,tt;
	scanf("%d",&tt);
	long i,j;
	long n,k,b,t;
	long spd[111],x[111],cango[111];
	long needtobeturn[111];
	long cangosum;
	long havedone;
	long turns,sumturns;

	for(cc=0;cc<tt;cc++){
		cangosum=0;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&spd[i]);
		for(i=0;i<n;i++)
			if((double)(b-x[i])/spd[i]<=t+eps){
				cango[i]=1;
				cangosum++;
			}else
				cango[i]=0;
		
		if(cangosum<k){
			printf("Case #%d: IMPOSSIBLE\n",cc+1);
		}else{
			//memset(needtobeturn,0,sizeof(needtobeturn));
			/*for(i=0;i<n;i++){
				needtobeturn[i]=0;
				for(j=i+1;j<n;j++)
					if(!cango[j])
						needtobeturn[i]++;
			}*/

			havedone=0;sumturns=0;
			for(i=n-1;havedone<k;i--){
				if(cango[i]){
					havedone++;
					turns=0;
					for(j=i+1;j<n;j++)
						if(!cango[j])
							turns++;
					sumturns+=turns;
				}
			}

			printf("Case #%d: %d\n",cc+1,sumturns);
		}
	}
	return 0;
}