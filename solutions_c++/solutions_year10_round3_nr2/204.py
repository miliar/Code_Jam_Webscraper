#include<cstdio>
#include<cmath>
using namespace std;

int main()
{
	int t;
	double l,p,c;
	int z=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf",&l,&p,&c);
		printf("Case #%d: %.0lf\n",++z,ceil(log(ceil(log(ceil(p/l))/log(c)))/log(2.0)));
	}
	return 0;
}
