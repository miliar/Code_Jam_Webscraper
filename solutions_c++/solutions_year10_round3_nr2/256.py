#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long INT;

int solve1(INT a, INT b, INT c)
{
	INT aa = a;
	int steps = 0;
	while((a*c < b) && (aa < b))
	{
		++steps;
		aa *= c*c;
		a  *= c;
	}
	return steps;
}

INT pow(INT c, int p)
{
	INT r=1;
	for(int i=0;i<p;i++)
	{
		r*=c;
	}
	return r;
}

int solve(INT a, INT b, INT c)
{
	int s = 1;
	int segms = 0;
	int steps = 0;
	for(;;)
	{
		int p = segms+1;
		INT cs = pow(c,p);
		if((a*cs)>=b) break;

		steps++;
		segms += s;
		s *= 2;
	}
	return steps;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	INT a, aa, b, c;
	
	scanf("%d", &t);
	for(int it=1;it<=t;it++)
	{
		scanf("%lld%lld%lld", &a,&b,&c);		
		
		printf("Case #%d: %d\n", it, solve(a,b,c));
	}
	return 0;
}