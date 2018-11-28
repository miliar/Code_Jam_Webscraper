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

int a[20000];
int can[20000];
int d[20000][2];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int i,j,k,t,l,n,v,tmp,x,y,op;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&n,&v);
		for (i=0;i<(n-1)/2;i++)
		{
			scanf("%d%d",&a[i],&can[i]);
		}
		memset(d,-1,sizeof(d));
		for (i=(n-1)/2;i<n;i++)
		{
			scanf("%d",&a[i]);
			can[i]=0;
			d[i][a[i]]=0;
		}
		for (i=(n-1)/2-1;i>=0;i--)
		{
			x=2*i+1;
			y=2*i+2;
			op=a[i];
			for (j=0;j<2;j++)
				if (d[x][j]!=-1)
					for (k=0;k<2;k++)
						if (d[y][k]!=-1)
						{
							if (op==0) tmp=j|k;
							else tmp=j&k;
							if ((d[i][tmp]==-1)||(d[i][tmp]>d[x][j]+d[y][k]))
								d[i][tmp]=d[x][j]+d[y][k];
						}
			if (can[i]==0) continue;
			op=1-op;
			for (j=0;j<2;j++)
				if (d[x][j]!=-1)
					for (k=0;k<2;k++)
						if (d[y][k]!=-1)
						{
							if (op==0) tmp=j|k;
							else tmp=j&k;
							if ((d[i][tmp]==-1)||(d[i][tmp]>d[x][j]+d[y][k]+1))
								d[i][tmp]=d[x][j]+d[y][k]+1;
						}
		}
		if (d[0][v]==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n",l+1);
		}
		else
		{
			printf("Case #%d: %d\n",l+1,d[0][v]);
		}
	}
	return 0;
}

