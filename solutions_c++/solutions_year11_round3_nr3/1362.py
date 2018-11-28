#include <cstdio>
#include <set>

using namespace std;

int num[200];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ca=1;
	int n;
	int l,h;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&n,&l,&h);

		int i;
		for(i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
		}
		for(i=l;i<=h;i++)
		{
			bool flag=true;
			for(int j=0;j<n;j++)
			{
				if(num[j]%i!=0 && i%num[j]!=0)
				{
					flag=false;
					break;
				}
			}
			if(flag) break;
		}
		printf("Case #%d: ",ca++);
		if(i>h) printf("NO\n");
		else printf("%d\n",i);
	}

	return 0;
}