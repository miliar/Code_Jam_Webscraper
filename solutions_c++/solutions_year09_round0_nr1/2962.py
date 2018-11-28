#include <iostream>
#include <string.h>

using namespace std;

char pro[5001][20],ans[501];
int answer[5001];
bool hash[501][16][27];

int main()
{
	freopen("f.in","r",stdin);
	freopen("f.out","w",stdout);
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	int i,j;
	for(i=0;i<d;i++)
		scanf("%s",&pro[i]);
	for(i=0;i<n;i++)
	{
		int k=0,p=0;
		scanf("%s",ans);
		for(j=0;j<strlen(ans);j++)
		{
			if(ans[j]=='(')
				p=1;
			else if(ans[j]==')')
			{p=0;k++;}
			else
			{
				if(p)
					hash[i][k][ans[j]-'a']=true;
				else
				{
					hash[i][k][ans[j]-'a']=true;
					k++;
				}
			}
		}
	}
	int v;
	for(i=0;i<d;i++)
	{
		for(v=0;v<n;v++)
		{
			for(j=0;j<l;j++)
			{
				if(!hash[v][j][pro[i][j]-'a'])
					break;
			}
			if(j==l)
				answer[v]++;
		}
	}
	for(i=0;i<n;i++)
	{
		printf("Case #%d: %d\n",i+1,answer[i]);
	}
}