#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int hash[20000];
int main()
{
	int t;
	int stack[10];
	int text=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n,m;
		int last=0;
		scanf("%d%d",&n,&m);
		for(int i=n;i<=m;i++)
		{
			int mid[10];
			int num=0;
			int k=0;
			int v=i;
			while(v)
			{
				mid[k++]=v%10;
				v/=10;
			}
			int u=0;
			while(k)
			{
				stack[u++]=mid[--k];
			}
			memset(hash,0,sizeof(hash));
			
			for(int j=0;j<u;j++)
			{
				int ans=0;
				for(int z=0;z<u;z++)
				{
					ans=stack[(j+z)%u]+ans*10;
				//	cout<<"ans="<<ans<<endl;
				}
			//	cout<<"i="<<i<<" m="<<m<<" ans="<<ans<<endl;
				if(ans>i && ans<=m && !hash[ans])
				{
			//		cout<<"***"<<endl;
					hash[ans]=1;
					last++;
			//		cout<<"last="<<last<<endl;
				}
			}
		
		}
		printf("Case #%d: %d\n",text++,last);
			
	}
	return 0;
}