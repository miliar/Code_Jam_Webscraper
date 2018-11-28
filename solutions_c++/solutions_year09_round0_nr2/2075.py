#include <fstream>

using namespace std;

inline int MIN(int a,int b) {return (a>=b) ? b : a;}

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int N,m,n;
	dat >> N;
	for(int t=0;t<N;t++)
	{
		dat >> n >> m;
		int D[101][101]={0};
		int i,j;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				dat >> D[i][j];                
			}                
		}        
		int cur=1,F[101][101]={0};
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if (i-1>=0&&D[i][j]>D[i-1][j])
				{
//					F[i][j]=cur;
//					cur++;
					continue;
				}
				if (i+1<n&&D[i][j]>D[i+1][j])
				{
//					F[i][j]=cur;
//					cur++;
					continue;
				}           
				if (j-1>=0&&D[i][j]>D[i][j-1])
				{
//					F[i][j]=cur;
//					cur++;
					continue;
				}           
				if (j+1<m&&D[i][j]>D[i][j+1])
				{
//					F[i][j]=cur;
//					cur++;
					continue;
				}
				F[i][j]=-cur;
				cur++;
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if (F[i][j]==0)
				{
					int r=-1;
					if (i-1>=0&&(D[i-1][j]<r||r==-1))
					{
						r=D[i-1][j];
					}
					if (i+1<n&&(r>D[i+1][j]||r==-1))
					{
						r=D[i+1][j];
					}
					if (j-1>=0&&(r>D[i][j-1]||r==-1))
					{
						r=D[i][j-1];
					}
					if (j+1<m&&(r>D[i][j+1]||r==-1))
					{
						r=D[i][j+1];
					}
					if (i-1>=0&&D[i-1][j]==r)
					{
						F[i][j]=1;
						continue;
					}
					if (j-1>=0&&D[i][j-1]==r)
					{
						F[i][j]=2;
						continue;
					}
					if (j+1<m&&D[i][j+1]==r)
					{
						F[i][j]=3;
						continue;
					}
					if (i+1<n&&D[i+1][j]==r)
					{
						F[i][j]=4;
						continue;
					}
				}
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if (F[i][j]>0)
				{
					int curx=i,cury=j,dx[4]={-1,0,0,1},
									  dy[4]={0,-1,1,0};
					for(;F[curx][cury]>0;)
					{
						int f=F[curx][cury]-1;
						curx+=dx[f];
						cury+=dy[f];
					}
					F[i][j]=F[curx][cury];
				}
			}
		}
		char Ans[101][101]={0},curl='a';
		bool used[100]={0};
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if (!used[-F[i][j]])
				{
					used[-F[i][j]]=true;
					for(int ii=0;ii<n;ii++)
					{
						for(int jj=0;jj<m;jj++)
						{
							if (F[ii][jj]==F[i][j]) Ans[ii][jj]=curl;
						}
					}
					curl=(char)((int)curl+1);
				}
			}
		}
		sol << "Case #" << t+1 << ":" << endl;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if (j==0) sol << Ans[i][j];
				if (j!=0) sol << " " << Ans[i][j];
			}
			sol << endl;
		}
	}
	return 0;
}
