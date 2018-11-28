#include<stdio.h>
#include<string>
#include<map>
#include<memory.h>
using namespace std;

int n,m;
char line[1000];
map<string,int> tree;
int a[1001],h[101];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T1,T,i,j;
	scanf("%d",&T);
	
	for(T1=1;T1<=T;T1++)
	{
		tree.clear();
		scanf("%d\n",&n);
		for(i=1;i<=n;i++)
		{
			gets(line);
			string s(line);
			tree[s]=i;
		}

		scanf("%d\n",&m);
		for(i=1;i<=m;i++)
		{
			gets(line);
			string s(line);
			a[i]=tree[s];
		}

		memset(h,0,sizeof(h));
		int tot=0;
		int ans=0;
		for(i=1;i<=m;i++)
		{
			if(a[i]==0) continue;

			if(h[a[i]]==0)
			{
				h[a[i]]=1;
				tot++;
				if(tot==n)
				{
					ans++;
					memset(h,0,sizeof(h));
					h[a[i]]=1;
					tot=1;
				}
			}
		}
		printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}