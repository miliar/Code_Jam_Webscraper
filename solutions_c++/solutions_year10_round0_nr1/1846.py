#include<cstdio>
inline void rezolva()
{
	int n,k;
	scanf("%d%d",&n,&k);
	int x=1<<n;
	--x;
	++k;
	if((k&x)==0)
		fputs("ON\n",stdout);
	else
		fputs("OFF\n",stdout);
}
int main()
{
	freopen("proba.in","r",stdin);
	freopen("proba.out","w",stdout);

        int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d: ",i);
		rezolva();
	}

	return 0;
}

