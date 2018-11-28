#include<cstdio>
int N,K,pt;
int putere(int n, short int p)
{
	if (!p)
		return 1;
	if (p&1)
		return n*putere(n*n,p>>1);
	return putere(n*n,p>>1);
}
int main()
{
	freopen("snap.in","r",stdin);
	freopen("snap.out","w",stdout);
	short int t,timp=0;
	scanf("%hd",&t);
	while (t--)
	{
		scanf("%d%d",&N,&K);
		pt=putere(2,N);
		++timp;
		if ((K+1)%pt==0)
			printf("Case #%hd: ON\n",timp);
		else
			printf("Case #%hd: OFF\n",timp);
	}
	return 0;
}
