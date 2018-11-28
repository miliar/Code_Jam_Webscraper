#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORD(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define PB push_back
#define F firrst
#define S second
using namespace std;
int tab[100][100];
int main()
{
	int Z;
	scanf("%d",&Z);getchar();
	FOR(lol,1,Z+1)
	{
		int n,k;
		scanf("%d%d",&n,&k);getchar();
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				char temp;
				scanf("%c",&temp);
				tab[n-i][n-j]=(temp=='.'?0:(temp=='R'?1:2));
			}
			getchar();
		}
		int p=0;
		for(int i=1;i<=n;i++)
		{
			for(int j=n;j>=1;j--)
			{
				if(tab[i][j]==0)
				{
					FOR(h,0,p)
					{
						tab[i][j+h]=tab[i][j+h+1];
						tab[i][j+h+1]=0;
					}
					//p=0;
				}
				else p++;
			}
		}
		bool B=false,R=false;
		FOR(i,1,n+1)
		{
			FORD(j,n,1)
			{
				if(i+k-1<=n)
				{
					bool win=true;
					FOR(h,1,k)
					{
						if(tab[i][j]!=tab[i+h][j]){win=false;break;}
					}
					if(win){if(tab[i][j]==1)R=true;else if(tab[i][j]==2) B=true;}
				}
				if(j+k-1<=n)
				{
					bool win=true;
					FOR(h,1,k)
					{
						if(tab[i][j]!=tab[i][j+h]){win=false;break;}
					}
					if(win){if(tab[i][j]==1)R=true;else if(tab[i][j]==2) B=true;}
				}
				if((i+k-1<=n)&&(j+k-1<=n))
				{
					bool win=true;
					FOR(h,1,k)
					{
						if(tab[i][j]!=tab[i+h][j+h]){win=false;break;}
					}
					if(win){if(tab[i][j]==1)R=true;else if(tab[i][j]==2) B=true;}
				}	
				if((i+k-1<=n)&&(j-k+1>=1))
				{
					bool win=true;
					FOR(h,1,k)
					{
						if(tab[i][j]!=tab[i+h][j-h]){win=false;break;}
					}
					if(win){if(tab[i][j]==1)R=true;else if(tab[i][j]==2) B=true;}
				}
			}
		}
		printf("Case #%d: ",lol);
		if(!R&&!B)printf("Neither\n");
		else if(R&&B)printf("Both\n");
		else printf(R?"Red\n":"Blue\n");
	}
	return 0;
}
