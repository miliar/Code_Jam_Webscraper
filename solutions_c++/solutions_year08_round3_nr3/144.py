
#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define MOD 1000000007

long long N, n, m, X, Y, Z;

vector <long long> b;

vector <long long> mem;

void go(int k)
{
	long long res = 0;
	for (int i = k+1; i < n; i++)
	{
		if (b[i] <= b[k])
			continue;
		res = (res + mem[i]) % MOD;
	}
	
	mem[k] = res+1;
	
}

int main()
{
	vector <long long> a;
	cin >> N;
	
	for (long long t = 0; t < N; t++)
	{
		cin >> n >> m >> X >> Y >> Z;
	

		a.resize(m);	
		b.resize(n);
		mem.resize(n, -1);
		
		for (long long i = 0; i < m; i++)
		{
			cin >> a[i];
		}
		
		for (long long i = 0; i < n; i++)
		{
			b[i] = a[i%m];
			a[i%m] = (X * a[i%m] + Y * (i+1)) % Z;
		}
		
		long long res = 0;
		for (long long i = n-1; i >= 0; i--)
		{
			go(i);
			res = (res + mem[i])%MOD;
		}
		
		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}
