#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,j;
	int n,m;
	int c;
	int vstack[7];
	int vtot;
	bool hash[11000];
	scanf("%d",&c);
	int tc=1;
	while(c--)
	{
		scanf("%d%d",&n,&m);
		int res=0;
		for(i=n;i<m;i++)
		{
			vtot=0;
			n=i;
			int vt=0;
			int vs[10];
			while(n)
			{
				vs[vt++]=n%10;
				n/=10;
			}
			while(vt)
			{
				vstack[vtot++]=vs[--vt];
			}
			memset(hash,0,sizeof(hash));
			for(int k=0;k<vtot;k++)
			{
				int now=0;
				for(j=0;j<vtot;j++)
				{
					now=vstack[(j+k)%vtot]+now*10;
				}
				if(now>i&&now<=m&&!hash[now])
				{
					hash[now]=true;
					res++;
				}
			}
		}
		printf("Case #%d: %d\n",tc++,res);
	}
}
