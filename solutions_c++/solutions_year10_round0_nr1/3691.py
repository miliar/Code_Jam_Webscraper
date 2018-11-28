#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
const int N = 505;
int n,k;
int p[N];
int cases=1;
int judge()
{
   int i,j;
   for(i=1;i<=n;i++)
   { 
	  if(p[i]==0) return 0;
   }
   return 1;
}
int main()
{
	int T,dk,i,j;
//	freopen("large.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d",&n,&k);
		k %= 1<<n;
		for(i=1;i<=n;i++)
		{
			dk=1<<i;
			int ss=k%dk;
			if(ss<dk/2) p[i]=0;
			else p[i]=1;

		}
		if(judge())
		{
		printf("Case #%d: ON\n",cases++);
		}
			else printf("Case #%d: OFF\n",cases++);

	}
}
