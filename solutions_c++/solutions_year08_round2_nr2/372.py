#define _CRT_SECURE_NO_DEPRECATE 1
#include <vector>     
#include <map>     
#include <set>     
#include <deque>     
#include <algorithm>     
#include <utility>     
#include <sstream>     
#include <iostream>     
#include <cstdio>     
#include <cmath>     
#include <cstdlib>     

using namespace std; 

#define SZ(a) ((int)(a).size())
#define pii pair<int,int>
#define pll pair<__int64,__int64>
#define mp make_pair
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}
bool isPrime(int n)
{
	if (n == 1) return false;
	if (n == 2) return true;
	for (int i = 2; i <= ceil(sqrt((double)n)); ++i)
		if (n%i == 0)
			return false;
	return true;
}
int calc(int A, int B, int P)
{
	vector <int> primes;
	primes.clear();
	for (int i = P; i <= B; ++i)
		if (isPrime(i))
			primes.push_back(i);
	int a[1001];
	memset(a, 0, sizeof(a));
	int maxn = 1;
	a[A] = maxn;
	for (int i = A; i <= B; ++i)
	{
		for (int j = A; j <= B; ++j)
			if (i != j && !(a[i] > 0 && a[j] > 0 && a[i] == a[j]) )
			{
				for (int k = 0; k < SZ(primes); ++k)
					if (i%primes[k] == 0 && j%primes[k] == 0)
					{
						int tmin = min(a[i], a[j]);
						if (tmin == 0) tmin = max(a[i], a[j]);
						for (int ii = A; ii <= B; ++ii)
							if (a[ii] == a[j] || a[ii] == a[i])
								a[ii] = tmin;
					}
				if (a[j] == 0)
				{
					a[j] = ++maxn;
				}
			}
	}

	int b[1001];
	memset(b, 0, sizeof(b));
	int res = 0;
	for (int i = A; i <= B; ++i)
		if (b[a[i]] == 0)
		{
			++res;
			b[a[i]] = 1;
		}

	return res;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt = 0;
	cin >> testCnt;
	for (int testNum = 0; testNum < testCnt; ++testNum)
	{
		int A, B, P;
		cin >> A >> B >> P;
		cout << "Case #" << testNum+1 << ": " << calc(A, B, P) << endl;
	}
	return 0;
}