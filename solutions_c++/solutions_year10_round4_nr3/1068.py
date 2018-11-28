#include<stdio.h>
#include<gh.h>

int MIN(int a , int b) { return a < b ? a : b ; } 
int MAX(int a, int b) { return a > b ? a : b ; }

int main(){
	int tc , r;
	int g[200][200];
	int f[200][200];
	scanf("%d",&tc);
	int x1,y1,x2,y2;
	int el_time;
	int check ; 
	for(int t=1 ; t<=tc ; t++) {
		check = 0;
		el_time = 0 ; 
		for(int i=0;i<200;i++) 	{
			for(int j=0;j<200;j++) {
				g[i][j]=0;
				f[i][j]=0;
			}
		}
		
		scanf("%d",&r);
		for(int i=0;i<r;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1--;
			y1--;
			x2--;
			y2--;


			int MIN_x=MIN(x1,x2);
			int MAX_x=MAX(x1,x2);
			int MIN_y=MIN(y1,y2);
			int MAX_y=MAX(y1,y2);
			for(int i=MIN_y ; i<=MAX_y ; i++) {
				for(int j=MIN_x; j<=MAX_x; j++) {
					g[i][j]=1;
					f[i][j]=1;
				}
			}

		}
		while(true) {
			for(int i=0; i<100 ; i++) {
				for(int j=0;j<100; j++) {
											
						if((g[i-1][j]==0 && g[i][j-1]==0) || (i==0 && g[0][j-1] == 0) || (j==0 && g[i-1][0]==0))
							f [i][j]=0 ;

						if(i!=0 && j!=0 &&  g[i-1][j]==1 && g[i][j-1] == 1)
							f [i][j] = 1; 
							
				
				}
	
				
			}

			for(int i=0;i<100;i++)
			{
				for(int j=0;j<100;j++)
				{
					g[i][j]=f[i][j];
					if(g[i][j]==1)
						check=1;
				}
			}

			if(check ==1)
			{
				check = 0;
				el_time ++;
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %d\n",t,el_time+1);

	}
}
