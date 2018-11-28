#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int main()
{
	int T,cs;
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		int n,i,j;
		char t[10005];
		char c[256][256];
		bool d[256][256];
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",t);
			c[t[0]][t[1]]=c[t[1]][t[0]]=t[2];
		}
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",t);
			d[t[0]][t[1]]=d[t[1]][t[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",t);
		for(i=1;i<n;i++)
		{
			if(c[t[i]][t[i-1]]!=0)
			{
				t[i]=c[t[i]][t[i-1]];
				t[i-1]=' ';
				continue;
			}
			for(j=i-1;j>=0;j--)
			{
				if(d[t[i]][t[j]]!=0)
					break;
			}
			if(j>=0)
			{
				for(j=0;j<=i;j++)
					t[j]=' ';
			}
		}
		string ans="";
		for(i=0;i<n;i++)
		{
			if(t[i]==' ')
				continue;
			ans+=t[i];
		}
		printf("Case #%d: [",cs);
		if(ans.size()>0)
		{
			printf("%c",ans[0]);
			for(i=1;i<ans.size();i++)
			{
				printf(", %c",ans[i]);
			}
		}
		printf("]\n");
	}
}