#include <list>
#include <stdio.h>

using namespace std;

int main()
{
	int numCases, num,a, b;
	long long c;
	list<long long> x,y;
	list<long long>::iterator px;
	list<long long>::reverse_iterator py;
	
	scanf("%d\n", &numCases);
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		scanf("%d\n", &num);
		x.clear();
		y.clear();
		for (a = 0; a < num; a++)
		{
			scanf("%d", &b);
			x.push_back(b);
		}
		for (a = 0; a < num; a++)
		{
			scanf("%d", &b);
			y.push_back(b);
		}
		x.sort();
		y.sort();
		c= 0;
		for (px = x.begin(), py = y.rbegin(); px != x.end(); ++px, ++py)
		{
			c += *px * *py;
		}
		printf("Case #%d: %lld\n", curCase, c);
	}
	return 0;
}
