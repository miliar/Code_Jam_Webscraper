#include<cstdio>

int Z = 0;
bool vst[10000010];
int p10[10];

int goes(int i)
{
	int r = i%10;
	i /= 10;
	i += Z*r;
	return i;
}

void func()
{
	Z = 0;
	long long ans = 0LL;
	int x,y,o;
	scanf("%d%d",&x,&y);
	o = y;
	while( o != 0 ) o /= 10, Z ++;
	for(int c=x;c<y;c++)
	{//printf("! %d\n",c);
		for(int d=1;d<Z;d++)
		{
			int r = ( c / p10[d] ) + ( c % p10[d] ) * p10[Z-d];
			//printf("%d : %d\n",c,r);
			//printf("> %d %d %d\n",d,r,Z);
			if( r > c and r <= y )
			{
				if( !vst[r] ) vst[r] = true, ans ++;
				//else printf("%d %d\n",c,r);
			}
		}//printf("??\n");
		for(int d=1;d<Z;d++)
		{
			int r = ( c / p10[d] ) + ( c % p10[d] ) * p10[Z-d];
			vst[r] = false;
		}//printf("XX\n");
	}
	printf("%lld",ans);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.txt","w",stdout);
	p10[0] = 1;
	for(int c=1;c<10;c++) p10[c] = 10*p10[c-1];
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		func();
		if( c != t ) printf("\n");
	}
}
