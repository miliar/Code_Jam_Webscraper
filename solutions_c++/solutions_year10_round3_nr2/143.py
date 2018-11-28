#include <iostream>
#include <algorithm>
#include <math.h>
using namespace  std;

int l;
int p,c;


int main()
{
	freopen("b-small.in","r",stdin);
	freopen("b-small.out","w",stdout);
	int i, j;
	int Test;
	int Cases;
	scanf("%d",&Test);
	for (Cases = 1;Cases<=Test;Cases++)
	{
		int Count = 0;

		scanf("%d %d %d",&l,&p,&c);
		int ans =ceil(log(double(p)/double(l))/log(double(c)))-1;
		while (ans>0)
		{
			ans=(ans)/2;
			Count++;
		}

		printf("Case #%d: %d\n",Cases,Count);
	}

	return 0;
}