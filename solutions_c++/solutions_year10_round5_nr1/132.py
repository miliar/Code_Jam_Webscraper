#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int isp[1000009] = {0};

int mpow(int num, int p)
{
	int M = p;
	p -= 2;
	int res = 1;
	int d = num;
	while (p > 0)
	{
		if (p & 1)
		{
			res = (res * (long long)d) % M;
		}
		p /= 2;
		d = (d * (long long)d) % M;
	}
	return res;
}

int isok(const vector<int>& x, int a, int b, int p)
{
	for (int i = 0; i+1 < x.size(); ++i)
	{
		if ((x[i]*(long long)a + b) % p != x[i+1])
		{
			return -1;
		}
	}
	return ((x.back()*(long long)a) + b) % p;
}

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");	
	isp[0] = isp[1] = 1;
	for (int i = 2; i*i <= 1000000; ++i)
	{
		if (isp[i] == 0)
		{
			for (int j = i*i; j <= 1000000; j += i)
			{
				isp[j] = 1;
			}
		}
	}
	vector<int> prime;
	for (int i= 0; i <= 1000000; ++i)
	{
		if (isp[i] == 0)
			prime.push_back(i);
	}

	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int d, n;
		ifs >> d >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
		{
			ifs >> a[i];
		}
		if (n == 1 || n == 2 && a[0] != a[1])
		{
			ofs << "Case #" << test+1 << ": " << "I don't know." << endl;
		}
		else if (n == 2 && a[0] == a[1])
		{
			ofs << "Case #" << test+1 << ": " << a[0] << endl;
		}
		else 
		{
			int ten = 1;
			for (int i = 0; i < d; ++i)
			{
				ten *= 10;
			}
			int j = 0;
			int maxd = *max_element(a.begin(), a.end());
			bool amb = false;
			int resall = -1;
			while (j < prime.size() && prime[j] <= ten)
			{
				if (prime[j] > maxd)
				{
					int first = (a[2]+prime[j]-a[1]) % prime[j];
					int second = (a[1] + prime[j]-a[0]) % prime[j];
					int aa = (first * (long long)mpow(second, prime[j])) % prime[j];
					int b = (a[0]*(long long)aa) % prime[j];
					b = (a[1]+prime[j]-b) % prime[j];
					int res = isok(a, aa, b, prime[j]);
					if (res != -1)
					{
						if (resall != -1 && res != resall)
						{
							amb = true;
							break;
						}
						else resall = res;
					}
				}
				++j;
			}
			if (amb)
			{
				ofs << "Case #" << test+1 << ": " << "I don't know." << endl;
			}
			else 
			{
				ofs << "Case #" << test+1 << ": " << resall << endl;
			}
		}
	}
  	return 0;
}
