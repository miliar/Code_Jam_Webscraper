#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int T =0;
	scanf("%d",&T);

	long k=0,R=0,G=0;
	long g[1000] = {0};
	for(int t=0;t<T;t++){
		scanf("%d %d %d",&R,&k,&G);

		memset(g,0,1000);
		for(int gt =0;gt<G;gt++){
			scanf("%d",&g[gt]);
		}
	
		long i=0,kt=0;
		for(long r=0;r<R;r++){
			long ki=0;
			int si = i>G?0:i;
			for(long gi=i<G?i:0,ir=0;ki<k;gi++,ir++){
		
				gi = gi>=G?0:gi;
				if(ir>0 && si == gi){
					i = gi-1;
					break;
				}			


				if(g[gi]+ki > k)break;
				ki += g[gi];
				i = gi;
			}
			i++;
			kt += ki;
		}		
		printf("Case #%d: %d\n",t+1,kt);
	}
}

