#include <cstdio>

long long x[101], y[101];
int T, n;
long long A, B, C, D, x0, y0,M;

void solve(int caz)
{
	int i, j, k;
	long long s=0;
	double xa, ya;
	for(i=1;i<=n;++i)
		for(j=i+1;j<=n;++j)
			for(k=j+1;k<=n;++k)
			{
				xa=(double) (x[i]+x[j]+x[k])/(double)3.0;
				ya=(double) (y[i]+ y[j] + y[k]) /(double)3.0;
				
				int xx=(int) xa;
				int yy=(int) ya;
				
				if(xa*3==(x[i]+x[j] + x[k])  && ya*3==(y[i]+y[j]+y[k])) ++s;
			}
			
	printf("Case #%d: %lld\n", caz, s);
	
	
	
}

int main()
{
	
	int i, j;
	
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
	scanf("%d\n", &T);
	
	for(int ii=1;ii<=T;++ii)
	{
		scanf("%d %d %d %d %d %d %d %d\n", &n, &A, &B, &C, &D, &x0, &y0,&M);
		
		x[1]=x0;
		y[1]=y0;
		
		for(i=2;i<=n;++i)
		{
			x[i]=(A*x[i-1]+B)% M;
			y[i]=(C*y[i-1]+D)%M;
		}
		
		solve(ii);
	}
	
	return 0;
}