#include<stdio.h>
int h[50];
inline int hash(char c)
{
	if(c>='0' && c<='9')
		return c-'0';
        return 12+c-'a';
}
inline void rezolva()
{
	char c[65]={0};
	fgets(c,65,stdin);
	long long b=0;
	int i;
	for(i=0; (c[i]>='0' && c[i]<='9') || (c[i]>='a' && c[i]<='z'); ++i)
	{
		if(h[hash(c[i])]==-1)
		{
			++b;
			if(b==1)
				h[hash(c[i])]=1;
			else
			if(b==2)
				h[hash(c[i])]=0;
			else
				h[hash(c[i])]=(int)b-1;
		}
	}
        int n=i-1;
	long long rez=0;
	if(b==1)
	{
		rez=(long long)h[hash(c[n])];
		b=2;
		long long b1=1;
		for(i=n-1; i>=0; --i)
		{
			b1*=b;
			rez+=(long long)h[hash(c[i])]*b1;
		}
		printf("%lld\n",rez);
		return;
	}
	long long b1=1;
	rez=(long long)h[hash(c[n])];
	for(i=n-1; i>=0; --i)
	{
		b1*=b;
		rez+=(long long)h[hash(c[i])]*b1;
	}
	printf("%lld\n",rez);
}	
int main()
{
	freopen("pa.in","r",stdin);
	freopen("pa.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for(int i=1; i<=T; ++i)
	{
        	for(int j=0; j<50; ++j)
			h[j]=-1;
		printf("Case #%d: ",i);
		rezolva();
	}
	return 0;
}

