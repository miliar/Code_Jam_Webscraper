#include <cstdio>
#include <algorithm>
using namespace std;
#define oo 105
int Test,Case;
int a[oo],P,Q;
int f[oo][oo];
int s[oo];

inline void readin()
{
	scanf("%d%d",&P,&Q);
	for (int i=1;i<=Q;++i)
		scanf("%d",a+i);
}

inline void solve()
{
	sort(a+1,a+1+Q);
	for (int i=1;i<=Q;++i)
		s[i]=a[i]-a[i-1]-1;
	s[Q+1]=P-a[Q];
	for (int i=1;i<=Q+1;++i)
		s[i]+=s[i-1];

	memset(f,63,sizeof f);
	for (int i=1;i<=Q+1;++i)
		f[i][i]=0;
	for (int i=Q+1;i>0;--i)
		for (int j=i+1;j<=Q+1;++j)
			for (int k=i;k<j;++k)
				f[i][j]<?=f[i][k]+f[k+1][j]+(s[j]-s[i-1])+(j-i-1);

	printf("%d\n",f[1][Q+1]);
}

int main()
{
	freopen("base.in","r",stdin);
    freopen("base.out","w",stdout);
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		readin();
		solve();
	}
	return 0;
}
