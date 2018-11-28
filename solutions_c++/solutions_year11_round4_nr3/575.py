#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

int testNum = 0;
long long result;
long long N;

void read()
{
	int i;
	cin >> N;
	//for (i = 1; i <= N; ++i)
}

bool isPrime(long long n)
{
	if (n == 2)
		return true;
	int i;
	double sq = sqrt(n + 0.0) + 1;
	for (i = 2; i <= sq; ++i)
	{
		if (n % i == 0)
			return false;
	}
return true;
}

void printOut()
{
	cout << "Case #" << testNum << ": ";
	cout << result << "\n";
}
void solve()
{
	int i,j;
	result = 0;
	read();
	if (N == 1)
	{
		result = 0;
		printOut();
		return;
	}
	double sq = sqrt(N + 0.0) + 1;
	int p;
	int power;
	for (i = 2; i <= sq; ++i)
	{
		if (isPrime(i))
		{
			p = 0;
			power = i;
			while (power <= N)
			{
				power *= i;
				++p;
			}
			result += p - 1;
		}
	}
	++result;
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		cerr << testNum << "\n";
		++testNum;
		solve();
		--t;
	}
return 0;
}