#include <stdio.h>
#include <queue>
using namespace std;
int c[1000];
int calc()
{
	int r , k , n , tmp  ,rec;
	int res = 0;
	queue<int>qu;
	scanf("%d%d%d",&r,&k,&n);
	for(int i = 0 ; i < n ; i++)
	{
		scanf("%d",&tmp);
		qu.push(tmp);
	}
	while(r--)
	{
		tmp = 0;
		c[0] = 0;
		while(!qu.empty())
		{
			if(tmp+qu.front() <= k)
			{
				c[++c[0]] = qu.front();
				qu.pop();
				tmp += c[c[0]];
			}else break;
		}
		for(int i = 1 ; i <= c[0] ; i++)
		{
		//	printf("%d ",c[i]);
			qu.push(c[i]);
		}
	//	puts("");
		res+=tmp;
	}
	return res;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int cas=0;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: %d\n",++cas,calc());
	}
}
