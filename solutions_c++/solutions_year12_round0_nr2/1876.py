#include <stdio.h>

int main()
{
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int n,N,S,p,count=0;
		scanf("%d %d %d",&N,&S,&p);
		for(n=0;n<N;n++){
			int total,k,r;
			scanf("%d",&total);
			k=total/3;
			r=total%3;
			if(total==0){
				if(0>=p)count++;
			}
			else if(r==0){//k,k,k or k-1,k,k+1 * max = k+1
				if(k>=p)count++;
				else if(S>0&&k+1>=p){
					S--;
					count++;
				}
			}
			else if(r==1){//k,k,k+1 or k-1,k+1,k+1 * max = k+1
				if(k+1>=p)count++;
			}
			else if(r==2){//k,k,k+2 * or k,k+1,k+1 max = k+2
				if(k+1>=p)count++;
				else if(S>0&&k+2>=p){
					S--;
					count++;
				}
			}

		}
		printf("Case #%d: %d\n",t,count);
	}	
	return 0;
}
