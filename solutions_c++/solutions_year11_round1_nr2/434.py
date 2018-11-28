#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

char a[10010][15],b[200][30];
int alive[10010],app[10010][300],n,m,val[10010][200],tes,le[10010],op[20];

void calc(int l,int r)
{
	int tt=0;
	for (int i=1;i<=n;i++) alive[i]=1;
	int len=strlen(b[r]),ll=le[l];
	for (int i=1;i<=n;i++) if (le[i]!=ll) alive[i]=0;
	//cout << len<<" ";
	for (int i=0;i<len;i++)
	{
		char c=b[r][i];
		int ok=0;
		for (int ii=1;ii<=n;ii++)
			if (alive[ii] && app[ii][c]) { ok=1; break; }	
		if (!ok) continue;
		for (int jj=1;jj<=n;jj++)
			if (alive[jj]) 
			{
				for (int ii=0;ii<ll;ii++)
					if ((a[jj][ii]==c) ^ (a[l][ii]==c)) { alive[jj]=0; break; }
			}
		ok=0;
		for (int ii=0;ii<ll;ii++) if (a[l][ii]==c) { ok=1; break; }
		if (!ok) tt++;
	}
	val[l][r]=tt;
}

void work()
{
	for (int i=1;i<=n;i++) le[i]=strlen(a[i]);
	for (int i=1;i<=n;i++)
	{
		for (int j='a';j<='z';j++) app[i][j]=0;
		for (int j=0;j<le[i];j++) app[i][a[i][j]]=1;
	}
	for (int j=1;j<=m;j++) 
	{
		int t=1;
		for (int i=1;i<=n;i++) 
		{
			calc(i,j);
			if (val[i][j]>val[t][j]) t=i;
		}
		printf("%s",a[t]);
		if (j<m) printf(" ");
		else printf("\n");
	}	
}


int main()
{
	freopen("b5.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		printf("Case #%d: ",ttt);
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) scanf("%s",a[i]);
		for (int i=1;i<=m;i++) scanf("%s",b[i]);
		work();
	}
	return 0;
}
