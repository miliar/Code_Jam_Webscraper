#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int n, k;
char s[50];
int a[110][110];
int g[110][110], mt[110];
bool vtd[110];
int ans;

bool findm(int x)
{
	vtd[x]=true;
	for(int i=1;i<=n;++i)
		if (g[x][i]) 
		if (mt[i]==0 || !vtd[mt[i]] && findm(mt[i])) {
			mt[i]=x; return true;
	}
	return false;
}

void h()
{
	memset(mt,0,sizeof(mt));
	ans=0;
	for(int i=1;i<=n;++i) {
		memset(vtd,0,sizeof(vtd));
		if (findm(i)) ++ans;
	}
}

int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("c.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
 	while (tt<T) {
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;++i) {
			for(int j=1;j<=k;++j)
				scanf("%d",&a[i][j]);
		}
		for(int i=1;i<=n;++i) 
			for(int j=1;j<=n;++j) {
				bool can=1;
				for(int p=1;p<=k;++p) {
					if (a[i][p]<=a[j][p]) can=0;
				g[i][j]=can;
			}
		}
		h();
		printf("Case #%d: %d\n",++tt, n-ans);
	}
	return 0;
}