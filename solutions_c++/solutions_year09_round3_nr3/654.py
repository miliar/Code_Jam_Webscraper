#include<cstdio>
#define P 10001
#define N 101
bool ok[N],viz[P];
short int n,p,sol[N],v[N];
int s,minim=1000000000;
void suma()
{
	s=p-1;
	viz[sol[1]]=true;
	for (short int i=2; i<=n; ++i)
	{
		viz[sol[i]]=true;
		for (short int j=sol[i]-1;j&&!viz[j]; --j) 
			++s;
		for (short int j=sol[i]+1;j<=p&&!viz[j]; ++j)
			++s;
	}
	for (short int i=1; i<=n; ++i)
		viz[sol[i]]=false;
	if (s<minim)
		minim=s;
}
void back(short int k)
{
	if (k==n+1)
	{
		suma();
		return;
	}
	for (short int i=1; i<=n; ++i)
		if (!ok[i])
		{
			ok[i]=true;
			sol[k]=v[i];
			back(k+1);
			ok[i]=false;
		}
}
void citire()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	short int t;
	scanf("%hd",&t);
	for (short int i=1; i<=t; ++i)
	{
		minim=1000000000;
		scanf("%hd%hd",&p,&n);
		for (short int j=1; j<=n; ++j)
			scanf("%hd",&v[j]);
		back(1);
		printf("Case #%hd: %d\n",i,minim);
	}
}
int main()
{
	citire();
	return 0;
}
