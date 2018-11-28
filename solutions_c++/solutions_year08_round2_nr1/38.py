#include <cstdio>
using namespace std;
const int N = 3*3;

inline int t(long long x, long long y)
{
	return ((3*(x%3))+(y%3));
}

bool is_ok(int a, int b, int c)
{
	int x = (a%3)+(b%3)+(c%3);
	int y = (a/3)+(b/3)+(c/3);
	x%=3;
	y%=3;
	return ((x==0)&&(y==0));
}

void func(int cas)
{
	long long l[N];
	for (int i=0; i<N; i++)
		l[i]=0;
	long long m,n,a,b,c,d,x,y;
	scanf("%lld",&n);
	scanf("%lld%lld%lld%lld",&a,&b,&c,&d);
	scanf("%lld%lld",&x,&y);
	scanf("%lld",&m);
	l[t(x,y)]++;
	for (int i=1; i<n; i++)
	{
		x = (a*x+b)%m;
		y = (c*y+d)%m;
		l[t(x,y)]++;
	}
	long long res = 0;
	for (int i=0; i<N; i++)
		res += (((l[i])*(l[i]-1)*(l[i]-2))/6);
	for (int i=0; i<N; i++)
	for (int j=0; j<N; j++)
		if (i!=j&&is_ok(i,i,j))
			res += ((l[i]*(l[i]-1)*l[j])/2);
	for (int i=0; i<N; i++)
	for (int j=i+1; j<N; j++)
	for (int k=j+1; k<N; k++)
		if (is_ok(i,j,k))
			res += (l[i]*l[j]*l[k]);
	printf("Case #%d: %lld\n",1+cas,res);
}

int main()
{
	int n;
	scanf("%d",&n);
	for (int i=0; i<n; i++)
		func(i);
	return 0;
}




