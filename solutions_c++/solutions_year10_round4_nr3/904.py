
#include "string.h"
#include "math.h"
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <string>
#include <iostream>
using namespace std;

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))

const int MAX_INT = 0x07070707;
const double eps = 1e-10;

const int N =102;

int a[N][N][2];
void set(int x0,int y0,int x1,int y1)
{
	for(int i=x0;i<=x1;i++)
		for(int j=y0;j<=y1;j++)
			a[i][j][0]=1;
}
int main()
{
	freopen("F://Google Code Jam//C-small-attempt2.in","r",stdin);
	//freopen("F://Google Code Jam//read.txt","r",stdin);
	freopen("F://Google Code Jam//write.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int tst=1;tst<=cas;tst++)
	{
		printf("Case #%d: ",tst);
		memset(a,0,sizeof(a));
		int x0,y0,x1,y1;
		int i,j,n;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d",&y0,&x0,&y1,&x1);
			set(x0,y0,x1,y1);
		}

		bool flag = 1;
		int c=0,t=0;
		while(flag)
		{
			flag =0;
			t++;
			for(i=1;i<=100;i++)
			{
				for(j=1;j<=100;j++)
				{
					a[i][j][t%2]=a[i][j][(t+1)%2];
					if(a[i][j][(t+1)%2]==0)
					{
						if(a[i-1][j][(t+1)%2]==1 && a[i][j-1][(t+1)%2]==1){
							flag =1;
							a[i][j][t%2]=1;
						}
					}
					else
					{
						
						if(a[i-1][j][(t+1)%2]==0 && a[i][j-1][(t+1)%2]==0)
							a[i][j][t%2]=0;
						else
							flag =1;
					}
				}
			}
			for(i=1;i<=100;i++)
				for(j=1;j<=100;j++)
					a[i][j][(t+1)%2]=0;
			c++;
		}
		printf("%d\n",c);
	}
	return 0;
}