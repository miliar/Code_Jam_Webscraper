#include<stdio.h>
#include<math.h>

int min(int a , int b)
{
	if(a<b)
		return a;
	else
		return b;
}

int max(int a, int b)
{
	if(a>b)
		return a;
	return b;
}

int main(){
	int tc , r;
	int mat[200][200];
	int temp[200][200];
	scanf("%d",&tc);
	int x1,y1,x2,y2;
	int el_time;
	int check ; 
	for(int t=1 ; t<=tc ; t++)
	{
		check = 0;
		el_time = 0 ; 
		for(int i=0;i<200;i++)
		{
			for(int j=0;j<200;j++)
			{
				mat[i][j]=0;
				temp[i][j]=0;
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

		/*	if(x1 == x2)
			{
				for(int i=min(y1,y2); i<= max(y1,y2) ; i++)
				{
					mat[i][x1] = 1;
					temp[i][x1] = 1; 
				}
			}
			else if(y1 == y2)
			{
				for(int i=min(x1,x2) ; i<= max(x1,x2) ; i++)
				{
					mat[y1][i] = 1;
					temp[y1][i] = 1;
				}
			} */


			int min_x=min(x1,x2);
			int max_x=max(x1,x2);
			int min_y=min(y1,y2);
			int max_y=max(y1,y2);
			for(int i=min_y ; i<=max_y ; i++)
			{
				for(int j=min_x; j<=max_x; j++)
				{
					mat[i][j]=1;
					temp[i][j]=1;
				}
			}

		}
		while(1)
		{
			for(int i=0; i<100 ; i++)
			{
				for(int j=0;j<100; j++)
				{
				
					
					
						if((mat[i-1][j]==0 && mat[i][j-1]==0) || (i==0 && mat[0][j-1] == 0) || (j==0 && mat[i-1][0]==0))
							temp [i][j]=0 ;

						if(i!=0 && j!=0 &&  mat[i-1][j]==1 && mat[i][j-1] == 1)
							temp [i][j] = 1; 
					
					
				
				}

			
				
			}

			for(int i=0;i<100;i++)
			{
				for(int j=0;j<100;j++)
				{
					mat[i][j]=temp[i][j];
					if(mat[i][j]==1)
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
