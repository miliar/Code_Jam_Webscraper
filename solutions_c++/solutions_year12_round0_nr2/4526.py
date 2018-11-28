#include <iostream>
using namespace std;

void process(int caseNum)
{
	int n, s, p;
	n = s = p = 0;

	scanf("%d %d %d\n", &n, &s, &p);
	
	int maxG = 0, minNormal, minSurprising;
	
	{
		int p3 = 3*p;
		
		minNormal = p3 - 2;
		minSurprising = p3 - 4;
		
		if (minNormal <= 0)
			minNormal = p;
		
		if (minSurprising <= 0)
			minSurprising = p;
	}
	
	for( int i=0; i<n; ++i)
	{
		int sum = 0;
		scanf("%d", &sum);
		
		if (sum >= minNormal)
		{
			++maxG;
		}
		else if( sum >= minSurprising && s > 0)
		{
			++maxG;
			--s;
		}
	}
	printf("Case #%d: %d\n", caseNum, maxG);
}

int main()
{
	int t = 0;
	scanf("%d\n", &t);
	
	for(int i=1; i<=t; ++i) 
		process(i);
	
	return 0;
}