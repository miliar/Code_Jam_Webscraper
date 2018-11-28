#include<iostream>
using namespace std;
char str[10000][20];

int a[30][30];
	char tmp[10000];
int main()
{
	int l,d,n;
	int i,j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while(scanf("%d%d%d",&l,&d,&n)!=EOF)
	{
		for(i=0;i<d;i++) scanf("%s",str[i]);
		for(int t=1;t<=n;t++)
		{
			for(i=0;i<30;i++)
			{
				for(j=0;j<30;j++) a[i][j]=0;
			}
			scanf("%s",tmp);
			for(i=j=0;i<l;i++)
			{
				if(tmp[j]=='(')
				{
					for(j++;tmp[j]!=')';j++)
					{
						a[i][tmp[j]-'a']=1;
					}
					j++;
				}
				else
				{
					a[i][tmp[j]-'a']=1;
					j++;
				}
			}
			int ans=0;
			for(i=0;i<d;i++)
			{
				for(j=0;j<l;j++)
				{
					if(a[j][str[i][j]-'a']==0) break;
				}
				if(j==l) ans++;
			}
			printf("Case #%d: %d\n",t,ans);
		}
	}
	return 0;
}