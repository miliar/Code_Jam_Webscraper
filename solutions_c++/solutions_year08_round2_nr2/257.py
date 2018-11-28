#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int ans;
int a, b, p;
int par[1001];
int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499};

int parent (int x)
{
	if (par[x] != x)
	{
		par[x] = parent(par[x]);
		return par[x];
	}
	return x;
}

void unite (int x, int y) {
	y = parent(y);
	par[y] = parent(x);
	ans--;
}

int main ()
{
	int tests, test;
	cin >> tests;
	for (test = 1; test <= tests; ++test) {
		ans = 0;
		cin >> a >> b >> p;
		for (int i = a; i <= b; ++i)
			par[i] = i;
		ans = b-a+1;
		bool ok = true;
		while (ok)
		{
			ok = false;
			for (int i = a; i <= b; ++i)
				for (int j = i; j <= b; ++j)
					if (parent(i) != parent(j))
				{
					for (int k = 0;true ;++k)
						if (primes[k] >= p)
					{
						if (i%primes[k] == 0 && j%primes[k] == 0) {
							unite(i,j);
							ok = true;
							break;
						}
						if (primes[k] == 499)
							break;
					}
				}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
}