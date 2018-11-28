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
#define MOD 1000000007
using namespace std;

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);

	int number, times;
	cin >> number;
	for (times = 0 ;times < number ;times++)
	{
		unsigned long long n, m , x, y , z;
		cin >>n>> m >> x>> y >>z;
		unsigned long long i , j;
		unsigned long long a[1000];
		for (i = 0 ; i < m ; i++)
		{
			cin >>a[i];
			
		}
		unsigned long long speed[1000];
		for (i = 0 ; i < n ; i++)
		{
			speed[i] = a[i % m];
			a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
			
		}
		unsigned long  dp[1000];
		dp[0] =1;
		unsigned long sum= 1;
		for (i = 1; i < n ; i++)
		{
			dp[i] = 1;
			for (j = 0 ; j < i ; j++)
				if (speed[j] < speed[i]) dp[i] = (dp[i] + dp[j]) % MOD;
			sum = (sum + dp[i]) % MOD;
		}
		printf("Case #%d: %lu\n" , times+1  , sum);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
