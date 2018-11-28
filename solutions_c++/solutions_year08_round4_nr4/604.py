
#pragma warning(disable:4996)
#pragma warning(disable:4018)
#pragma warning(disable:4267)

#include <iostream>
#include <fstream>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#include <cstring>
#include <memory>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <functional>
#include <cctype>

using namespace std;

#define _TRACE

#ifdef _TRACE
#define t(a) ((a))
#else
#define t(a) ()
#endif

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define fi(n) for (i = 0; i < (n); ++i)
#define fj(n) for (j = 0; j < (n); ++j)
#define fk(n) for (k = 0; k < (n); ++k)
#define wt while (true)
#define sz size()
#define pb push_back
#define mp(a,b) (make_pair((a),(b))

typedef long long int64;
typedef vector<int> vi;
typedef unsigned int uint;

ifstream fin;
ofstream fout;

int k;
int len;
string s;
vi pm;

void solve()
{
	pm.clear();
	fin >> k;
	fin >> s;
	int i, j;
	for (i = 0; i < k; ++i)
	{
		pm.pb(i);
	}
	int bst = 50001;
	do
	{
		int cur = 0;
		int last = 'a' - 1;
		int t= s.length() / k;
		for (i = 0; i < t; ++i)
		{
			int b = i * k;
			for (j = 0; j < k; ++j)
			{
				int idx = b + pm[j];
				if (s[idx] != last)
				{
					++cur;
					last = s[idx];
				}
			}
		}
		if (cur < bst)
		{
			bst = cur;
		}
	}
	while (next_permutation(pm.begin(), pm.end()));
	fout << bst << endl;
}


int main()
{
	fin.open("in.in");
	fout.open("out.txt");

	int n, i;
	fin >> n;

	fi(n)
	{
		fout << "Case #" << i + 1 << ": ";
		solve();
	}

	fout.close();
	fin.close();
	cin.get();
	return 0;
}

