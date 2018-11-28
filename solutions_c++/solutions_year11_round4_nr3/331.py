#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;


int N;
int mem[1 << 20];

long long gcd(long long a, long long b) 
{
	return b == 0 ? a : gcd(b, a % b); 
}

int getMax(int curBought, int enteredMask)
{
	int l = 1;
	for (int j = 0; j < N; j++)
	{
		if ((enteredMask & (1 << j)))
		{
			l = l * (j + 1) / gcd(l, j + 1);
		}
	}

	if (enteredMask != 0)
	{
		assert (curBought == l);
	}


	if (enteredMask == (1 << N) - 1)
		return 0;

	//assert (curBought < 10000);
	int& res = mem[enteredMask];
	if (res != -1)
		return res;

	res = 0;

	for (int i = 0; i < N; i++)
	{
		if (enteredMask & (1 << i))
			continue;

		int a = i + 1;

		if (curBought == 0 || ((curBought % a) != 0))
		{
			int l = 1;
			for (int j = 0; j < N; j++)
			{
				if ((enteredMask & (1 << j)) || j == i)
				{
					l = l * (j + 1) / gcd(l, j + 1);
				}
			}
			int newBought = (curBought / l + 1) * l;

			res = max(res, 1 + getMax(newBought, enteredMask ^ (1 << i)));
		}
		else
		{
			res = max(res, getMax(curBought, enteredMask ^ (1 << i)));
		}
	}

	return res;
}

int getMin(int curBought, int enteredMask)
{
	if (enteredMask == (1 << N) - 1)
		return 0;

	//assert (curBought < 10000);
	int& res = mem[enteredMask];
	if (res != -1)
		return res;

	res = 10000;

	for (int i = 0; i < N; i++)
	{
		if (enteredMask & (1 << i))
			continue;

		int a = i + 1;

		if (curBought == 0 || ((curBought % a) != 0))
		{
			int l = 1;
			for (int j = 0; j < N; j++)
			{
				if ((enteredMask & (1 << j)) || j == i)
				{
					l = l * (j + 1) / gcd(l, j + 1);
				}
			}
			int newBought = (curBought / l + 1) * l;

			res = min(res, 1 + getMin(newBought, enteredMask ^ (1 << i)));
		}
		else
		{
			res = min(res, getMin(curBought, enteredMask ^ (1 << i)));
		}
	}

	return res;
}


int primeList[1000];
int primeCount;

bool test_prime(int p)
{
	if (p < 2) return false;
	for (int i = 2; i * i <= p; i++)
		if (p % i == 0)
			return false;
	return true;
}

int getMax2()
{
	vector<int> maxPrimes(primeCount, 0);

	int ans = 1;

	for (int i = 2; i <= N; i++)
	{
		int c = i;
		/*if ((cur % i) != 0)
		{
			ans++;
			cur = cur * i / gcd(cur, i);
		}*/
		bool need = false;

		for (int j = 0; j < primeCount; j++)
		{
			int cnt = 0;
			while (c % primeList[j] == 0)
			{
				c /= primeList[j];
				cnt++;
			}

			if (cnt > maxPrimes[j])
			{
				need = true;
				maxPrimes[j] = cnt;
			}

			if (c == 1)
				break;
		}

		if (need) ans++;
	}

	return ans;
}


int getMin2()
{
	vector<int> maxPrimes(primeCount);
	for (int i = 0; i < primeCount; i++)
	{
		for (int c = 1; c <= N; c++)
		{
			int cnt = 0;
			int j = c;
			while ((j % primeList[i]) == 0)
			{
				j /= primeList[i];
				cnt++;
			}
			maxPrimes[i] = max(maxPrimes[i], cnt);
		}
	}

	int ans = 0;
	for (int i = 0; i < primeCount; i++)
	{
		if (maxPrimes[i] == 0)
			continue;

		ans++;
	}

	return ans;
}

int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif

	for (int i = 2; i <= 1000; i++)
		if (test_prime(i))
		{
			primeList[primeCount++] = i;
		}

	/*N = 12;
	int res2 = getMin2();

	N = 10;
	int res = getMax(0,  0);

	for (N = 2; N < 20; N++)
	{

		memset(mem, -1, sizeof(mem));
		int res = getMax(0,  0);

		int res3 = getMax2();
		if (res != res3)
		{
			printf("FAILED");
		}

		memset(mem, -1, sizeof(mem));
		int res2 = getMin(0,  0);
		
		res3 = getMin2();

		if (res2 != res3)
		{
			printf("FAILED");
		}

		printf("%d: %d %d\n", N, res, res2);
	}*/
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{	
		cin >> N;

		int res = N == 1 ? 0 : getMax2() - getMin2();
				

		printf("Case #%d: %d\n", nTest, res);
	
		fflush(stdout);
	} 


	return 0;
}


