#include<cstdio>

int n,n2,s,s2;
double must,must2;
int A[210];

void f()
{
	s = n2 = 0;
	scanf("%d",&n);
	for(int c=1;c<=n;c++)
	{
		scanf("%d",&A[c]);
		s += A[c];
	}
	s2 = s;
	must = ( ( double )( 2*s ) ) / ( ( double )( n ) );
	//printf("%d %d %.2lf\n",n,s,must);
	for(int c=1;c<=n;c++) if( ((double)(A[c])) < ((double)(must)) )
	{
		s2 += A[c];
		n2 ++;
	}
	must2 = ( ( double )( s2 ) ) / ( ( double )( n2 ) );
	for(int c=1;c<=n;c++)
	{
		if( ((double)(A[c])) >= ((double)(must)) ) printf(" 0.000000");
		else printf(" %.6lf",(must2-A[c])*100/(double)(s));
	}
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("x.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d:",c);
		f();
		printf("\n");
	}
}
