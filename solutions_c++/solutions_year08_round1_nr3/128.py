#include <cstdio>
#include <memory>
#include <cmath>
#define oo 2
long double x=3+sqrt(5);
int N,T,Case;
int f[oo]={2,6};
struct Tm
{
	int a[oo][oo];
}	a,b,res;

inline Tm operator *(Tm& A,Tm& B)
{
	memset(&res,0,sizeof res);
	for (int i=0;i<2;++i)
		for (int j=0;j<2;++j)
			for (int k=0;k<2;++k)
				res.a[i][j]=(res.a[i][j]+A.a[i][k]*B.a[k][j])%1000;
	return res;
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	for (scanf("%d",&T);T;T--)
	{
		scanf("%d",&N);
		
		a.a[0][1]=6,a.a[0][0]=2;
		a.a[1][0]=0,a.a[1][1]=0;
		
		b.a[0][0]=0,b.a[1][0]=1;
		b.a[0][1]=-4,b.a[1][1]=6;
		
		N--;
		while (N)
		{
			if (N&1) a=a*b;
			N>>=1;
			b=b*b;
		}
		
		printf("Case #%d: %.3d\n",++Case,(a.a[0][1]+999)%1000);
	}
	return 0;
}
	
//f[n]=6*f[n-1]-4*f[n-2]

