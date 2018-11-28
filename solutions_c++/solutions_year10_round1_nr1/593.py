#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <algorithm>
#include <set>
#include <deque>
#include <stack>
#include <numeric>
#include <functional>
#include <map>
#include <queue>
using namespace std;
int main(void)
{
	freopen("Ab.in","r",stdin);
	freopen("Ab.out","w",stdout);
	char a[100][100],c;
	int t,q,i,j,i1,j1,k,kl1,kl2,kl3,kl4,n;
	bool bo1,bo2;
	scanf("%d",&t);
	for (q=1;q<=t;q++)
	{
		scanf("%d%d",&n,&k);
		memset(a,0,sizeof(a));
		for (i=1;i<=n;i++)
		{
			scanf("%c",&c);
			for (j=1;j<=n;j++)
				scanf("%c",&a[i][j]);
		}
		for (i=1;i<=n;i++)
			for (j=n;j>0;j--)
				if (a[i][j]!='.')
				{
					j1=j;
					while (a[i][j1+1]=='.')
					{
						swap(a[i][j1],a[i][j1+1]);
						j1++;
					}
				}
		bo1=false;
		bo2=false;
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if (a[i][j]!='.')
				{
					kl1=1;
					c=a[i][j];
					j1=j+1;
					while (a[i][j1]==c)
					{
						j1++;
						kl1++;
					}
					kl2=1;
					j1=j+1;
					i1=i+1;
					while (a[i1][j1]==c)
					{
						i1++;
						j1++;
						kl2++;
					}
					kl3=1;
					i1=i+1;
					while (a[i1][j]==c)
					{
						i1++;
						kl3++;
					}
					kl4=1;
					i1=i+1;
					j1=j-1;
					while (a[i1][j1]==c)
					{
						i1++;
						j1--;
						kl4++;
					}
					if ((kl1>=k)||(kl2>=k)||(kl3>=k)||(kl4>=k))
					{
						if (c=='R')
							bo1=true; else
							bo2=true;
					}
				}
				printf("Case #%d: ",q);
				if (!bo1&&!bo2)
					printf("Neither\n"); else
					if (bo1&&bo2)
						printf("Both\n"); else
						if (bo1)
							printf("Red\n"); else
							printf("Blue\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
