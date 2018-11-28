#include <stdio.h>
#define NMAX 1005
int t,n,rez;
struct muchie
{
	int a,b;
};
muchie A[NMAX];
void read()
{
	scanf("%d",&n);
	int i;
	for (i=1; i<=n; i++)
		scanf("%d%d",&A[i].a,&A[i].b);
}
void solve()
{
	rez=0;
	int i,j;
	for (i=1; i<=n; i++)
		for (j=i+1; j<=n; j++)
			if ((A[i].a>=A[j].a && A[i].b<A[j].b) || (A[j].a>=A[i].a && A[j].b<A[i].b))
				rez++;
}
int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d",&t);
	int i;
	for (i=1; i<=t; i++)
	{
		read();
		solve();
		printf("Case #%d: %d\n",i,rez);
	}
	return 0;
}
