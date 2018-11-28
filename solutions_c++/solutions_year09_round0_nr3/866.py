#include<stdio.h>
#include<string.h>
#define N 510
#define M 10000
int a[20];
int poz[15][7];
char c[N];
inline int hash(char c)
{
	if(c=='w')
		return 0;
	if(c=='e')
		return 1;
	if(c=='l')
		return 2;
	if(c=='c')
		return 3;
	if(c=='o')
		return 4;
	if(c=='m')
		return 5;
	if(c==' ')
		return 6;
	if(c=='t')
		return 7;
	if(c=='d')
		return 8;
	if(c=='j')
		return 9;
        if(c=='a')
		return 10;
	return -1;
}
inline void init()
{
	poz[0][0]=1;
	poz[0][1]=0;

        poz[1][0]=3;
	poz[1][1]=1;
	poz[1][2]=6;
	poz[1][3]=14;

        poz[2][0]=1;
	poz[2][1]=2;

        poz[3][0]=2;
	poz[3][1]=3;
	poz[3][2]=11;

	poz[4][0]=3;
	poz[4][1]=4;
	poz[4][2]=9;
	poz[4][3]=12;

        poz[5][0]=2;
	poz[5][1]=5;
	poz[5][2]=18;

        poz[6][0]=3;
	poz[6][1]=7;
	poz[6][2]=10;
	poz[6][3]=15;

        poz[7][0]=1;
	poz[7][1]=8;

        poz[8][0]=1;
	poz[8][1]=13;

        poz[9][0]=1;
	poz[9][1]=16;

        poz[10][0]=1;
	poz[10][1]=17;
}
inline void rezolva()
{
	fgets(c,N,stdin);
	memset(a,0,sizeof(a));
	int n=0;
	a[19]=1;
	for(; (c[n]>='a' && c[n]<='z') || c[n]==' '; ++n)
	       ;
	if(n==0)
	{
		fputs("0000\n",stdout);
		return;
	}

	--n;
	int cod;
	for(; n>=0; --n)
	{
		cod=hash(c[n]);
		if(cod==-1)
			continue;
		for(int i=1; i<=poz[cod][0]; ++i)
		{
			a[poz[cod][i]]+=a[poz[cod][i]+1];
			if(a[poz[cod][i]]>=M)
				a[poz[cod][i]]-=M;
		}
	}
	printf("%04d\n",a[0]);
}	
int main()
{
	freopen("pc.in","r",stdin);
	freopen("pc.out","w",stdout);
        int T;
	scanf("%d\n",&T);
	init();
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d: ",i);
	        rezolva();
	}
	return 0;
}

