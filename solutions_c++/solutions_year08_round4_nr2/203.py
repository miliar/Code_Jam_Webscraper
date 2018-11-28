#include<stdio.h>

int main(){

	int T,N,flag;
	int X,Y,A,x1,y1,x2,y2;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
	
		scanf("%d%d%d",&X,&Y,&A);

		flag = 0;

		for(x1=1;x1<=X && !flag;x1++){
			
			for(x2=1;x2<=X && !flag;x2++){
				
				for(y1=0;y1<=Y;y1++){
					
					if( (A+x2*y1)%x1 )
						continue;
					
					y2 = (A+x2*y1)/x1;

					if( 0<=y2 && y2<=Y){
						flag = 1;
						break;
					}
				}
				if(flag)break;

			}
			if(flag)break;

		}

		if(flag)
			printf("Case #%d: %d %d %d %d %d %d\n",N,0,0,x1,y1,x2,y2);
		else
			printf("Case #%d: IMPOSSIBLE\n",N);



	}

	return 0;
}