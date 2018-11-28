#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define INF (1LL << 60)

const int nmax = 60;
char c[nmax];
long long x[nmax];
bool used[nmax];
bool notZero[nmax];
int a[nmax];
long long mx;
int p;

int base;

class EncodedSum 
{
public:
	long long maximumSum(vector <string> numbers)
	{
		int i, j, n = (int)numbers.size();
		set<char> s;
		set<char> z;
		for(i = 0; i < n; ++i)
		{
			s.insert(numbers[i].begin(), numbers[i].end());
			z.insert(numbers[i][0]);
		}
		i = 0;

		set<char>::iterator cit;
		for(cit = s.begin(); cit != s.end(); ++cit, ++i)
		{
			c[i] = *cit;
		}

		p = i;

		if (p > base)
		{
			return -1;
		}


		memset(notZero, 0, sizeof(notZero));

		for(cit = z.begin(); cit != z.end(); ++cit)
		{
			notZero[find(c, c + p, *cit) - c] = true;
		}

		memset(x, 0, sizeof(x));
		for(i = 0; i < n; ++i)
		{
			long long t = 1;
			for(j = (int)numbers[i].size() - 1; j >= 0; --j)
			{
				x[find(c, c + p, numbers[i][j]) - c] += t;
				if (t > INF / base)
				{
					return -2;
				}
				t *= base;
			}
		}

		priority_queue< pair<long long, int> > pq;
		for(i = 0; i < p; ++i)
		{
			pq.push(make_pair(x[i], i));
		}

		long long sss = 0;
		pair<long long, int> pp;
		if (p > 1)
		{
			if (!notZero[pq.top().second])
			{
				pq.pop();
			}
			else
			{
				pp = pq.top();
				pq.pop();
				pq.pop();
				pq.push(pp);
			}
		}
		for(i = 1; i < base && !pq.empty(); ++i)
		{
			pp = pq.top();
			pq.pop();
			sss += pp.first * i;
			if (sss > INF)
			{
				return -2;
			}
		}
		return sss;
	}
};


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tt;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		vector<string> vs;
		string ts;
		cin >> ts;
		vs.push_back(ts);
		long long mn = INF, s;
		EncodedSum ___test;
		for(base = 2; base <= 100; ++base)
		{
			s = ___test.maximumSum(vs);
			if (s > 0)
			{
				mn = min(mn, s);
			}
			else
			{
				if (s == -2)
				{
					break;
				}
			}
		}
		cerr << tt + 1 << " finished\n";
		cout << "Case #" << tt + 1 << ": " << mn << '\n';
	}
//	printf("%lld\n%lld", INF, 1000000000000000000LL);
	return 0;
}