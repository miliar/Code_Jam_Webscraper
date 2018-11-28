#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

long long N, L, H;
vector<long long> x;
long long cmmdc[10001];
long long cmmmc[10001];


long long gcd(long long a, long long b)
{
	long long r;

	r = a % b;
	while( r != 0)
	{
		a = b;
		b = r;
		r = a%b;
	}

	return b;
}


long long findMin(long long a, long long b, long long k, int d)
{
	if (d%k != 0) return -1;

	long long A = ceil(a*1.0/k);
	long long B = floor(b*1.0/k);
	long long D = d/k; 
	long long r = A%D;
	long long C;

	//if (r == 0) return k*A;

	/*
	if (r != 0)
		C = A + D-r;
	else
		C = A;

	if
	

	//if (r == D) return -1;
	if (C <= B) return k*C;
    */

	for (int i = A; i <= B; i++)
	{
		if (D % i == 0)
			return i*k;
	}
	return -1;
}


long long solve()
{
	cmmdc[N-1] = x[N-1];
	for (int i = N-2; i >= 0; i--)
	{
		cmmdc[i] = gcd(x[i], cmmdc[i+1]);
	}

	cmmmc[0] = x[0];
	for (int i = 1; i < N; i++)
	{	
		long double ld = 1.0*x[i]/gcd(cmmmc[i-1], x[i])*cmmmc[i-1];

		if ( (ld > H) )
			cmmmc[i] = -1;
		else
			cmmmc[i] = cmmmc[i-1]*x[i]/gcd(cmmmc[i-1], x[i]);
	}

	long long num = findMin(L, H, 1, cmmdc[0]);
	
	if (num != -1) 
		return num;

	for (int i = 0; i <= N-2; i++)
	{
		if (cmmmc[i] == -1) return -1;

		num = findMin(L, H, cmmmc[i], cmmdc[i+1]);

		if (num != -1) 
			return num;
	}

	if (cmmmc[N-1] == -1) return -1;

	long long A = ceil(L*1.0/cmmmc[N-1]);
	long long B = floor(H*1.0/cmmmc[N-1]);

	if (A <= B) return A*cmmmc[N-1];
	return -1;
}



int main()
{
	fstream f, g;
	int nTests;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> nTests;

	for (int k = 1; k <= nTests; k++)
	{
		f >> N >> L >> H;
		x.clear();

		for (int i = 0; i < N; i++)
		{
			long long value;
			f >> value;
			x.push_back(value);
		}

		sort(x.begin(), x.end());

		long long res = solve();

		g << "Case #" << k <<": ";

		if (res == -1) 
		{
			g << "NO";
		}
		else
		{
			g << res;
		}

		if (k != nTests)
			g << "\n";


	}

	f.close();
	g.close();

	return 0;
}