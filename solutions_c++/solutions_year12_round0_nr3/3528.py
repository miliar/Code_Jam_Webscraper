// RecycledNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <set>
#include <math.h>

using namespace std;

long int compute(int A, int B)
{
	set<int> currResult;
	int n,m, a,b;
	long result = 0;

	for(n=A; n<B; ++n)
	{
		m = n;
		currResult.clear();
		int digits = (int)ceil(log10((float)n));
		int power = pow((long double) 10, digits-1);
		for (int j=0; j<=digits; ++j)
		{
			a = m%10;
			b=m/10;
			m = a*power + b;
			if (n < m && m <=B)
				currResult.insert(m);
		};

		result+= currResult.size();
	};

	return result;

}

int main(int argc, char* argv[])
{
	int cases;
	int A,B;

	freopen("c://temp//in2.txt", "r+", stdin);
	freopen("c://temp//out.txt", "w+", stdout);

	scanf("%i", &cases);

	for (int i=1; i<=cases; ++i)
	{
		scanf("%i", &A);
		scanf("%i", &B);
		long result = compute(A,B);
		//if (i%3==1 || i == 50)
		printf("Case #%i: %li\n",i, result);
	};

	return 0;
}

