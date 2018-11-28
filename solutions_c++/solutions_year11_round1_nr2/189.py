#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN = 10050;
const int MAXL = 15;
const int MAXM = 105;
char a[MAXN][MAXL];
char now[50];
int f[MAXN][26];
int all[MAXN];
int ok;
bool yes[MAXN];
int len[MAXN];
int n,m;
int Get(int x)
{
	int res=0;
	ok=(1<<26);
	for (int i=1;i<=n;i++)
	if (len[i]==len[x])
	{
		ok |= all[i];
		yes[i] = true;
	} else yes[i]=false;
	int ff=0;
	for (int ii=0;ii<26;ii++) 
	{
		int i = now[ii]-'a';
		if ( (ok & (1<<i)) == 0) continue;
		if ((all[x] & (1<<i))==0) 
		{
			res ++;
			for (int j=1;j<=n;j++)
			if (all[j] & (1<<i)) yes[j]=false;
		} else
		{
			ff |= (1<<i);
			for (int j=1;j<=n;j++)
			if (f[j][i] != f[x][i]) yes[j]=false;
		}
		if (ff == all[x]) break;
		ok = 0;
		for (int j=1;j<=n;j++)
			if (yes[j]) ok |= all[j];
	}
	return res;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",a[i]);
			len[i]=strlen(a[i]);
			memset(f[i],0,sizeof(f[i]));
			all[i]=0;
			for (int j=0;j<len[i];j++)
			{
				f[i][a[i][j]-'a'] |= (1<<j);
				all[i] |= (1<<(a[i][j]-'a'));
			}
		}
		printf("Case #%d:",tcase);
		for (int p=1;p<=m;p++)
		{
			scanf("%s",now);
			int an=-1,k;
			for (int i=1;i<=n;i++)
			{
				int temp= Get(i);
				if (temp>an)
				{
					an=temp;
					k=i;
				}
			}
			printf(" %s",a[k]);
		}
		printf("\n");
	}
}
