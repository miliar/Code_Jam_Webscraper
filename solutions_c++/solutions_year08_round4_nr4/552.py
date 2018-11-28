#include <stdio.h>
#include <algorithm>

using namespace std;

int p[10];
char s[10000];
char s2[10000];
int h[20];
int k,n,sol;

void perm(int pz, int l)
{
	int i;

	for (i=0;i<=l;i++)
		s2[i+pz]=s[ pz+p[i] ];
}

void back(int nivel)
{
	int i,nr;
	if (nivel==k)
		{
			for (i=0;i<n;i+=k)
				perm(i,k);

			nr=1;
			for (i=1;i<n;i++)
				if (s2[i]!=s2[i-1]) nr++;
			sol=min(sol,nr);
		}

	for (i=0;i<k;i++) 
		if (!h[i])
			{
				p[nivel]=i;
				h[i]=1;
				back(nivel+1);
                                h[i]=0;
			}
}

void solve()
{
	scanf("%d\n",&k);
	fgets(s,10000,stdin);

	for (n=0;(s[n]>='a')&&(s[n]<='z');n++);

	sol=n;
	back(0);
	printf("%d\n",sol);
}

int main()
{
	freopen("perm.in","r",stdin);
	freopen("perm.out","w",stdout);

	int T;
	scanf("%d ",&T);

	for (int i=1;i<=T;i++)
		{
			printf("Case #%d: ",i);
			solve();
		}
	return 0;
}
