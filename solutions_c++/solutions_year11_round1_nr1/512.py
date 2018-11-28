#include <iostream>
using namespace std;
template<class T> inline T gcd(T a,T b)
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

int solve(long long n, int pg, int pd)
{
	if(pg == 100 && pd < 100) 
		return 0;
	if(pg == 0 && pd > 0)
		return 0;

	int pda = pd;
	int pdb = 100;
	int pdd = gcd<int>(pda,pdb);
	pda /= pdd;
	pdb /= pdd;

	if(pdb <= n)
		return 1;

	return 0;
}


int main()
{
	int T;
	scanf("%d",&T);
	for(int Ti = 0;Ti <T ;Ti ++)
	{
		long long n;
		int pd, pg;
		scanf("%lld%d%d",&n,&pd,&pg);

		printf("Case #%d: ",Ti+1);
		if(solve(n,pg,pd))
			puts("Possible");
		else
			puts("Broken");
	}
}
