#include <stdio.h>
#define NMAX 20
#define LMAX 2000005
int t,a,b,A[NMAX],r,pos[NMAX],nr;
bool marc[LMAX];
int solve()
{
	int i,j,x,y,rez,val;
	rez=0;
	for (i=a; i<b; i++)
	{
		x=i; r=0; val=1;
		while (x){A[++r]=x%10; x/=10; val=val*10;}
		val/=10;
		for (j=1; j<=r/2; j++)
			y=A[j],A[j]=A[r-j+1],A[r-j+1]=y;
		for (j=r+1; j<=2*r; j++)
			A[j]=A[j-r];
		x=i; nr=0;
		for (j=2; j<=r; j++)
		{
			x-=val*A[j-1];
			x=x*10+A[r+j-1];
			
			if (x>i && x<=b)
				pos[++nr]=x;
		}
		for (j=1; j<=nr; j++)
			if (!marc[pos[j]])
				rez++,marc[pos[j]]=1;
		for (j=1; j<=nr; j++)
			marc[pos[j]]=0;
	}
	return rez;
}
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	int i;
	for (i=1; i<=t; i++)
	{
		scanf("%d%d",&a,&b);
		printf("Case #%d: ",i);
		printf("%d\n",solve());
	}
	return 0;
}
