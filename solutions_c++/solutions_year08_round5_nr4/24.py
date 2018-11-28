#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int a[100][100];
int d[100][100];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	int i,j,l,t,m,n,r,x,y;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d%d",&m,&n,&r);
		memset(a,0,sizeof(a));
		for (i=0;i<r;i++)
		{
			scanf("%d%d",&x,&y);
			a[x][y]=1;
		}
		memset(d,0,sizeof(d));
		d[1][1]=1;
		for (i=1;i<=m;i++)
			for (j=1;j<=n;j++)
				if ((i+j>2)&&(a[i][j]==0))
				{
					d[i][j]=0;
					if ((i>2)&&(j>1)) d[i][j]+=d[i-2][j-1];
					if ((i>1)&&(j>2)) d[i][j]+=d[i-1][j-2];
					d[i][j]%=10007;
				}
		printf("Case #%d: %d\n",l+1,d[m][n]);

	}
	return 0;
}

