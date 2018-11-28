#include <stdio.h>
#include <stdlib.h>


char buf[1024];
int  flavors[1024];
int  cnt_one[1024];

int accept(int z, int a, int b);

int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		gets(buf);
		int N=atoi(buf);
		gets(buf);
		int M=atoi(buf);
		
		int  two_n = 1;   // 2^N
		for(int i=0; i<N; i++)
			two_n = two_n * 2;
		
		for(int i=0; i<two_n; i++)
		{
			flavors[i]=1;
			cnt_one[i]=(i>>9)+((i>>8)&1)+((i>>7)&1)+((i>>6)&1)
				+((i>>5)&1)+((i>>4)&1)+((i>>3)&1)+((i>>2)&1)+((i>>1)&1)+(i&1);
		}
		
		int  T;
		for(int j=1; j<=M; j++)
		{
  			scanf("%d", &T);
			int  a[11], b[11];
  			for (int k=1; k<=T; k++)
  			{
  				scanf("%d%d", &a[k], &b[k]);
//  				printf("[%d,%d]",a[k],b[k]);
    		}
 			gets(buf);
   		
   			for(int z=0; z<two_n; z++) {
				int  bAccepted = 0;
	 			for (int k=1; k<=T; k++) {
    				if ( accept(z,a[k],b[k]) ) {
    					bAccepted = 1;
    				}
    			}
    			if ( bAccepted == 0 )
    				flavors[z]=0;
			}
		}
		
		int  min = 99999;
		int  founded_y = 1024;
		for(int y=0; y<two_n; y++) {
			if ( flavors[y] == 1) {
				if ( cnt_one[y] < min ) {
					founded_y = y;
					min = cnt_one[y];
				}
			}
		}
		
		printf("Case #%d:", i);
		
		if ( founded_y < 1024 )	{
    		for(int x=1; x<=N; x++)
    			printf(" %d", (founded_y >> (x-1))&1);
    		printf("\n");
		} else {
			printf(" IMPOSSIBLE\n");
		}
	}
  
	return  0;  
}

int accept(int z, int a, int b)
{
	return  (((z >> (a-1)) & 1) == b );
}
