#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <ctype.h>

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

int cmp(const void *p , const void *q)
{
	return *(int *) p < *( int * )q ? 1: 0;
}

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);
	int times, number;
	cin >> number;
	for (times = 0 ;times < number ; times ++)
	{
		int n, p , k , l;
		cin >> p>> k>>l;
		int i;
		int a[1000];
		for (i = 0 ;i < l; i++)
		{
			cin >> a[i];
		}
		qsort(a , l , sizeof(int) , cmp);
		long long res = 0;
		for (i = 0; i < l ; i++)
		{
			res += a[i] * (i / k+1) ;
		}
		cout <<"Case #"<<times+1<<": "<<res <<endl;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
