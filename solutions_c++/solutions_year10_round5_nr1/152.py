#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



int npr[1111111];


int d, k;
long long x[1000];
int minx;


void Load()
{
	cin >> d >> k;
	int i;

	minx = 0;

	for (i = 0; i < k; i++)
	{
		cin >> x[i];
		if (minx < x[i]) minx = x[i];
	}
}



long long Pow(long long x, long long k, long long p)
{
	if (k == 0) return 1 % p;
	if (k == 1) return x % p;
	long long res = Pow(x, k/2, p);
	res = (res*res) % p;
	if (k & 1) res = (res*x) % p;
	return res;
}

long long Inv(long long x, long long p)
{
	x = x % p;
	if (x < 0) x += p;
	return Pow(x, p-2, p);
}


void Solve()
{
	int N = 1;
	int i, j, l;
	for (i = 0; i < d; i++) N *= 10;

	bool tomany = false;
	bool was = false;
	int curans = 0, ans = 0;
	int a, b;


	if (k < 3) 
	{
		if (k < 2 || x[0] != x[1])
			cout << "I don't know.\n";
	    else cout << x[0] << "\n";
		return;
	}

	for (i = minx + 1; i < N; i++)
	{
		if (npr[i]) continue;
		a = ((Inv(x[1]-x[0], i)*(x[2]-x[1])) % i + i) % i;
		b = ((x[1] - x[0]*a) % i + i) % i;
		
		bool bad = false;
		for (j = 3; j < k; j++)
		{
			l = ((x[j-1]*a+b-x[j]) % i + i) % i;	
			if (l != 0) bad = true;
		}

		if (!bad)
		{
			curans = (a*x[k-1]+b) % i;
			if (was && ans != curans) tomany = true;
			was = true;
			ans = curans;
		}
	}
	if (!was || tomany)
		cout << "I don't know.\n";
	else cout << ans << "\n";

}


void Gen()
{
	npr[1] = 1;
	int i, j;
	for (i = 2; i < 1111111; i++)
	{
		if (npr[i]) continue;
		for (j = i+i; j < 1111111; j += i)
			npr[j] = 1;
	}
}

int main()
{
	int nt, tt;
	cin >> nt;
	Gen();
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
