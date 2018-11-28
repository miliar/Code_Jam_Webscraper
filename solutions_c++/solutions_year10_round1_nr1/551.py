#include <stdio.h>

int cal(char bord[][60], int n, int k)
{
	int i,j,kk,kk2,ok[128];
	ok['R']=ok['B']=0;
	for (i=0; i<n; i++)
	{
		for (j=0; j<n; j++)
		{
			if (bord[i][j]=='.') continue;
			if (j<=n-k)
			{
				for (kk=j+1; kk<j+k; kk++)
					if (bord[i][kk]!=bord[i][j]) break;
				if (kk==j+k) ok[bord[i][j]]=1; 
			}
			if (i<=n-k) 
			{
				for (kk=i+1; kk<i+k; kk++)
					if (bord[kk][j]!=bord[i][j]) break;
				if (kk==i+k) ok[bord[i][j]]=1; 
			}
			if (i<=n-k && j<=n-k)
			{
				for (kk=i+1, kk2=j+1; kk<i+k; kk++,kk2++)
				{
					if (bord[kk][kk2]!=bord[i][j]) break;
				}
				if (kk==i+k) ok[bord[i][j]]=1;
			}
			if (i<=n-k && j>=k-1)
			{
				for (kk=i+1,kk2=j-1; kk<i+k; kk++,kk2--)
				{
					if (bord[kk][kk2]!=bord[i][j]) break;
				}
				if (kk==i+k) ok[bord[i][j]]=1;
			}
		}
	}
	if (ok['B']==1 && ok['R']==1) return 4;
	if (ok['R']==1) return -1;
	if (ok['B']==1) return 1;
	return 0;
}	

int main()
{
	int t,cas,n,k,i,j,kk,an;
	char bord[60][60];
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%d%d",&n,&k);
		for (i=0; i<n; i++) scanf("%s",bord[i]);
		for (i=0; i<n; i++)
		{
			for (j=n-1; j>0; j--)
			{
				if (bord[i][j]!='.') continue;
				for (kk=j-1; kk>=0; kk--) if (bord[i][kk]!='.') break;
				if (kk<0) break;
				bord[i][j]=bord[i][kk];
				bord[i][kk]='.';
			}
		}
//		for (i=0; i<n; i++) printf("%s\n",bord[i]);
		an=cal(bord,n,k);
		if (an==0) printf("Case #%d: %s\n",cas,"Neither");
		else if (an==-1) printf("Case #%d: %s\n",cas,"Red");
		else if (an==1) printf("Case #%d: %s\n",cas,"Blue");
		else printf("Case #%d: %s\n",cas,"Both");
	}
	return 0;
}
						
