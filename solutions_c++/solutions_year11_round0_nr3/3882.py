#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double pi = 2*acos(0.0);

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	int n;
	int max, total, limit;
	int sum1, sum2;
	int sump1, sump2;
	int candies[1001];

	scanf("%d", &t);
	For(test, 1, t) 
	{
		Fill(candies, 0);
		max = 0;
		total = 0;

		scanf("%d", &n);
		Rep (i, n)
		{
			scanf ("%d", &candies[i]);
			total += candies[i];
		}

		limit = (int)(pow((double)2, n)/2.0);
		For (i, 1, limit)
		{
			sum1 = 0;
			sum2 = 0;
			sump1 = 0;
			sump2 = 0;

			Rep (j, n)
			{
				if (i & (1 << j))
				{
					sum1 += candies[j];
					sump1 ^= candies[j];
				}
				else
				{
					sump2 ^= candies[j];
				}
			}
			if (sump1 == sump2)
			{
				sum2 = total - sum1;
				checkMax(sum1, sum2);
				if (sum1 > max)
					max = sum1;
			}
		}
		
		if (max > 0)
			printf("Case #%d: %d\n", test, max);
		else
			printf("Case #%d: NO\n", test);
	}
	
	fclose (stdin);
	fclose (stdout);

	exit(0);
}
