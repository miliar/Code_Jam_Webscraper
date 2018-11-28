#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=110,maxm=1010;

int n,m,t,q;
string str[maxn],qname[maxm];
char strt[110];
int remain[maxm][maxn];

int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%d\n",&n);
		for(int i=0;i<n;i++)
		{
			gets(strt);
			str[i]=strt;
		}
		scanf("%d\n",&q);
		for(int i=1;i<=q;i++)
		{
			gets(strt);
			qname[i]=strt;
		}
		memset(remain,0,sizeof(remain));
		for(int i=q;i;i--)
		{
			for(int j=0;j<n;j++)
			{
				if(qname[i]==str[j])
				{
					remain[i][j]=i;
				}
				else remain[i][j]=remain[i+1][j];
			}
		}
		int ans=0,pnt=1;
		while(1)
		{
			int tmp=0;
			for(int i=0;i<n;i++)
			{
				if(remain[pnt][i]==0){tmp=-1;break;}
				else if(remain[pnt][i]>tmp)tmp=remain[pnt][i];
			}
			if(tmp==-1)break;
			ans++;
			pnt=tmp;
		}
//		int ans=0;
		printf("Case #%d: %d\n",cs,ans);
	/*	for(int i=1;i<=q;i++)
		{
			for(int j=0;j<n;j++)
			{
				printf("%d ",remain[i][j]);
			}
			printf("\n");
		}*/
	}
	return 0;
}
