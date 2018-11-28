#include<iostream>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<algorithm>
#include<vector>
#include<string.h>
#include<queue>

using namespace std;

int mat[101][101];
int next[101][101];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int cas,Te=1;
	scanf("%d",&cas);
	while( cas-- )
	{
		memset(mat,0,sizeof(mat));
		int N;
		cin>>N;
		while( N-- )
		{
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			for(int i=x1;i<=x2;i++)
			{
				for(int j=y1;j<=y2;j++)
					mat[i][j]=1;
			}
		}


		int ret=0;

		while( true )
		{
			bool flag=true;
			for(int i=1;i<=100 && flag;i++) 
				for(int j=1;j<=100 && flag;j++) 
					if( mat[i][j] ) flag=false;

			if( flag ) break;
			else ret++;

			//memset(next,0,sizeof(next));
			for(int i=1;i<=100;i++)
			{
				for(int j=1;j<=100;j++)
				{
					if( mat[i][j] )
					{
						if( mat[i][j-1] == 0 && mat[i-1][j]==0) 
							next[i][j]=0;
						else next[i][j]=1;
					}
					else
					{
						if(  mat[i][j-1] == 1 && mat[i-1][j]==1)
							next[i][j]=1;
						else next[i][j]=0;
					}
				}
			}
			//ret++;
			memcpy(mat,next,sizeof(mat));
		}

		printf("Case #%d: %d\n",Te++,ret);
	}
}