#include <cstdio>
#include <cstdlib>
#include <list>
using namespace std;

#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
int flag[100][100];
int rank[100][100];

void update(int m,int n,int h,int w)
{
	if(m == 0)
	{
		if(n==0)
		{
			if((n+1<=w-1) && (rank[0][1]==-1)&& ((flag[0][0] == 3)|| (flag[0][1] == 2 )))
			{
				rank[0][1] = rank[0][0];
				update(0,1,h,w);
			}
			if((m+1<=h-1) &&(rank[1][0]==-1)&& ((flag[0][0] == 4)||(flag[1][0] == 1)))
			{
				rank[1][0] = rank[0][0];
				update(1,0,h,w);
			}
		}
		else if(n== w-1)
		{
			if((n-1>=0) &&(rank[0][w-2] ==-1) && ((flag[0][w-1] == 2)||(flag[0][w-2]==3)))
			{
				rank[0][w-2] = rank[0][w-1];
				update(0,w-2,h,w);
			}
			if((m+1<=h-1) &&(rank[1][w-1]==-1)&&((flag[0][w-1] == 4)||(flag[1][w-1]==1)))
			{
				rank[1][w-1] = rank[0][w-1];
				update(1,w-1,h,w);
			}
		}
		else
		{
			if((n-1>=0) &&(rank[0][n-1]==-1)&& ((flag[0][n] == 2)||(flag[0][n-1]==3)))
			{
				rank[0][n-1] = rank[0][n];
				update(0,n-1,h,w);
			}
			if((n+1<=w-1) &&(rank[0][n+1]==-1)&& ((flag[0][n] == 3)||(flag[0][n+1]==2)))
			{
				rank[0][n+1] = rank[0][n];
				update(0,n+1,h,w);
			}
			if((m+1<=h-1) &&(rank[1][n]==-1)&& ((flag[0][n] == 4)||(flag[1][n]==1)))
			{
				rank[1][n] = rank[0][n];
				update(1,n,h,w);
			}
		}
	}
	else if(m==h-1)
	{
		if(n==0)
		{
			if((m-1>=0) &&(rank[h-2][0]==-1)&& ((flag[h-1][0] == 1)||(flag[h-2][0]==4)))
			{
				rank[h-2][0] = rank[h-1][0];
				update(h-2,0,h,w);
			}
			if((n+1<=w-1) &&(rank[h-1][1]==-1)&& ((flag[h-1][0] == 3)||(flag[h-1][1]==2)))
			{
				rank[h-1][1] = rank[h-1][0];
				update(h-1,1,h,w);
			}
		}
		else if(n== w-1)
		{
			if((m-1>=0) &&(rank[h-2][w-1]==-1)&& ((flag[h-1][w-1] == 1)||(flag[h-2][w-1]==4)))
			{
				rank[h-2][w-1] = rank[h-1][w-1];
				update(h-2,w-1,h,w);
			}
			if((n-1>=0) &&(rank[h-1][w-2]==-1)&& ((flag[h-1][w-1] == 2)||(flag[h-1][w-2]==3)))
			{
				rank[h-1][w-2]= rank[h-1][w-1];
				update(h-1,w-2,h,w);
			}
		}
		else
		{
			if((n-1>=0) &&(rank[h-1][n-1]==-1)&& ((flag[h-1][n] == 2)||(flag[h-1][n-1]==3)))
			{
				rank[h-1][n-1] = rank[h-1][n];
				update(h-1,n-1,h,w);
			}
			if((m-1>=0) &&(rank[h-2][n] ==-1)&& ((flag[h-1][n] == 1)||(flag[h-2][n]==4)))
			{
				rank[h-2][n] = rank[h-1][n];
				update(h-2,n,h,w);
			}
			if((n+1<=w-1) &&(rank[h-1][n+1] ==-1)&& ((flag[h-1][n] == 3)||(flag[h-1][n+1]==2)))
			{
				rank[h-1][n+1] = rank[h-1][n];
				update(h-1,n+1,h,w);
			}
		}
	}
	else
	{
		if(n==0)
		{
			if((m-1>=0) &&(rank[m-1][0] ==-1)&& ((flag[m][0] == 1)||(flag[m-1][0]==4)))
			{
				rank[m-1][0] = rank[m][0];
				update(m-1,0,h,w);
			}
			if((m+1<=h-1) &&(rank[m+1][0]==-1)&& ((flag[m][0] == 4)||(flag[m+1][0]==1)))
			{
				rank[m+1][0] = rank[m][0];
				update(m+1,0,h,w);
			}
			if((n+1<=w-1) &&(rank[m][1]==-1)&& ((flag[m][0] == 3)||(flag[m][1]==2)))
			{
				rank[m][1] = rank[m][0];
				update(m,1,h,w);
			}
		}
		else if(n== w-1)
		{
			if((m-1>=0) &&(rank[m-1][w-1]==-1)&& ((flag[m][w-1] == 1)||(flag[m-1][w-1]==4)))
			{
				rank[m-1][w-1] = rank[m][w-1];
				update(m-1,w-1,h,w);
			}
			if((m+1<=h-1) &&(rank[m+1][w-1] ==-1)&& ((flag[m][w-1] == 4)||(flag[m+1][w-1]==1)))
			{
				rank[m+1][w-1] = rank[m][w-1];
				update(m+1,w-1,h,w);
			}
			if((n-1>=0) && (rank[m][w-2]==-1)&&((flag[m][w-1] == 2)||(flag[m][w-2]==3)))
			{
				rank[m][w-2] = rank[m][w-1];
				update(m,w-2,h,w);
			}
		}
		else
		{
			if((m+1<=h-1) &&(rank[m+1][n]==-1)&&((flag[m][n] == 4)||(flag[m+1][n]==1)))
			{
				rank[m+1][n] = rank[m][n];
				update(m+1,n,h,w);
			}
			if((m-1>=0) &&(rank[m-1][n] ==-1)&& ((flag[m][n] == 1)||(flag[m-1][n]==4)))
			{
				rank[m-1][n] = rank[m][n];
				update(m-1,n,h,w);
			}
			if((n-1>=0) &&(rank[m][n-1]==-1)&& ((flag[m][n] == 2)||(flag[m][n-1]==3)))
			{
				rank[m][n-1] = rank[m][n];
				update(m,n-1,h,w);
			}
			if((n+1<=w-1) &&(rank[m][n+1]==-1)&&((flag[m][n] == 3)||(flag[m][n+1]==2)))
			{
				rank[m][n+1] = rank[m][n];
				update(m,n+1,h,w);
			}
		}
	}
}

int main()
{
		FILE* stream = fopen("output.out", "w");
		int T,H,W;
		int i,j,k;
		int ds[100][100];

		int bas;

		scanf("%d",&T);

		for(i=1;i <= T; i++)
		{
			bas = 0;
			int t1,t2,t3,t4;
			scanf("%d %d",&H,&W);
			for(j=0;j<H;j++)
				for(k=0;k<W;k++)
					scanf("%d",&ds[j][k]);
			memset(rank,-1,sizeof(rank));
			memset(flag,0,sizeof(flag));

			for(j=0;j<H;j++)
				for(k=0;k<W;k++)
				{
					if(j==0)
					{
						if(k==0)
						{
							if(k+1<=W-1)
								t3 = ds[0][0]-ds[0][1];
							else
								t3 = -32678;
							if(j+1<=H-1)
								t4 = ds[0][0]-ds[1][0];
							else
								t4 = -32678;
							if(t3>0 || t4>0)
							{
								if(t3 >= t4)
									flag[0][0] = 3;
								else
									flag[0][0] = 4;
							}
						}
						else if(k==W-1)
						{
							t2 = ds[0][W-1]-ds[0][W-2];
							if(j+1 <= H-1)
								t4 = ds[0][W-1]-ds[1][W-1];
							else
								t4 = -32678;
							if(t2>0 || t4>0)
							{
								if(t2 >= t4)
									flag[0][W-1] = 2;
								else
									flag[0][W-1] = 4;
							}
						}
						else
						{
							t2 = ds[0][k]-ds[0][k-1];
							if(k+1 <= W-1)
								t3 = ds[0][k]-ds[0][k+1];
							else
								t3 = -32678;
							if(j+1 <= H-1)
								t4 = ds[0][k]-ds[1][k];
							else
								t4 = -32678;
							if(t2>0 || t3>0 || t4>0)
							{
								if(t2>=t3 && t2>=t4)
									flag[0][k] = 2;
								else if(t3 >= t4)
									flag[0][k] = 3;
								else
									flag[0][k] = 4;
							}

						}
					}
					else if(j==H-1)
					{
						if(k==0)
						{
							t1 = ds[H-1][0]-ds[H-2][0];
							if(k+1 <= W-1)
								t3 = ds[H-1][0]-ds[H-1][1];
							else
								t3 = -32678;
							if(t1>0 || t3>0)
							{
								if(t1 >= t3)
									flag[H-1][0] = 1;
								else
									flag[H-1][0] = 3;
							}
						}
						else if(k==W-1)
						{
							t1 = ds[H-1][W-1]-ds[H-2][W-1];
							t2 = ds[H-1][W-1]-ds[H-1][W-2];
							if(t1>0 || t2>0)
							{
								if(t1 >= t2)
									flag[H-1][W-1] = 1;
								else
									flag[H-1][W-1] = 2;
							}
						}
						else
						{
							t1 = ds[H-1][k]-ds[H-2][k];
							t2 = ds[H-1][k]-ds[H-1][k-1];
							if(k+1 <= W-1)
								t3 = ds[H-1][k]-ds[H-1][k+1];
							else
								t3 = -32678;
							if(t1>0 || t2>0 || t3>0)
							{
								if(t1>=t2 && t1>= t3)
									flag[H-1][k] = 1;
								else if(t2 >= t3)
									flag[H-1][k] = 2;
								else
									flag[H-1][k] = 3;
							}
						}
					}
					else
					{
						if(k==0)
						{
							t1 = ds[j][0]-ds[j-1][0];
							if(k+1 <= W-1)
								t3 = ds[j][0]-ds[j][1];
							else
								t3 = -32678;
							if(j+1 <= H-1)
								t4 = ds[j][0]-ds[j+1][0];
							else
								t4 = -32678;
							if(t1>0 || t3>0 || t4>0)
							{
								if(t1>=t3 && t1>=t4)
									flag[j][0] = 1;
								else if(t3>=t4)
									flag[j][0] = 3;
								else
									flag[j][0] = 4;
							}
						}
						else if(k== W-1)
						{
							t1 = ds[j][W-1]-ds[j-1][W-1];
							t2 = ds[j][W-1]-ds[j][W-2];
							if(j+1 <= H-1)
								t4 = ds[j][W-1]-ds[j+1][W-1];
							else
								t4 = -32678;
							if(t1>0 || t2>0 || t4>0)
							{
								if(t1>=t2 && t1>=t4)
									flag[j][W-1] = 1;
								else if(t2>=t4)
									flag[j][W-1] = 2;
								else
									flag[j][W-1] = 4;
							}
						}
						else
						{
							t1 = ds[j][k]-ds[j-1][k];
							t2 = ds[j][k]-ds[j][k-1];
							if(k+1 <= W-1)
								t3 = ds[j][k]-ds[j][k+1];
							else
								t3 = -32678;
							if(j+1 <= H-1)
								t4 = ds[j][k]-ds[j+1][k];
							else
								t4 = -32678;
							if(t1>0 || t2>0 || t3>0 || t4>0)
							{
								if(t1>=t2 && t1>=t3 && t1>=t4)
									flag[j][k] = 1;
								else if(t2>=t3 && t2>= t4)
									flag[j][k] = 2;
								else if(t3>=t4)
									flag[j][k] = 3;
								else
									flag[j][k] =4;
							}
						}
					}
				}
			
			rank[0][0] = bas++;
			update(0,0,H,W);

			for(j=0;j<H;j++)
				for(k=0;k<W;k++)
				{
					if((rank[j][k] == -1) && (flag[j][k] == 0))
					{
						rank[j][k] = bas++;
						update(j,k,H,W);
					}
				}

		fseek(stream,0L,SEEK_END);
		fprintf(stream,"Case #%d:\n",i);
		for(j=0;j<H;j++)
		{
			for(k=0;k<W;k++)
			{
				fprintf(stream,"%c ",'a'+rank[j][k]);
			}
			fprintf(stream,"\n");
		}
	}

	fclose(stream);

	return 0;
}
