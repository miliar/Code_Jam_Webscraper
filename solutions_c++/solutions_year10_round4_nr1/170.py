#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int F(int x)
{
	return ((1+x)*x)/2 + (x*(x-1))/2;
}

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		vector<string> B;
		int K;
		scanf("%d", &K);
		for (int i = 0; i < K; ++i)
		{
			int n = i+1;
			string v;
			for (int j = 0; j < n; ++j)
			{
				int a;
				scanf("%d", &a);
//				a = rand() % 10;
				v.PB(a+'0');
			}
			B.PB(v);
		}
		for (int i = K-2; i >= 0; --i)
		{
			int n = i+1;
			string v;
			for (int j = 0; j < n; ++j)
			{
				int a;
				scanf("%d", &a);
//				a = rand() % 10;
				v.PB(a+'0');
			}
			B.PB(v);
		}
		int res = 2000000000;
		int N = 2*K-1;
		for (int i = 0; i < N; ++i)
		{
			int j;
			for (j = 1; i-j >= 0 && i+j < N; ++j)
			{
				string a = B[i-j];
				string b = B[i+j];
				if (a.size() > b.size())
					swap(a, b);
				if (b.substr((b.size()-a.size())/2, a.size()) != a)
					break;
			}
			if ((i-j >= 0 && i+j < N))
				continue;
			int km = K + abs(i-(K-1));
			// right
			for (j = 0; ; ++j)
			{
				int q;
				for (q = 0; q < N; ++q)
				{
					int L = km - abs(q-i);
					int a = (L-B[q].size()) / 2;
					int ml = (L+j-1)/2 - a;
					int mr = (L+j)/2 - a;
					while (ml >= 0 && mr < B[q].size())
					{
						if (B[q][ml] != B[q][mr])
							break;
						--ml;
						++mr;
					}
					if ((ml >= 0 && mr < B[q].size()))
						break;
				}
				if (q < N)
					continue;
				res = min(res, F(km + j) - F(K));
				break;
			}
			// left
			for (j = 0; j < N; ++j)
				reverse(ALL(B[j]));
			for (j = 0; ; ++j)
			{
				int q;
				for (q = 0; q < N; ++q)
				{
					int L = km - abs(q-i);
					int a = (L-B[q].size()) / 2;
					int ml = (L+j-1)/2 - a;
					int mr = (L+j)/2 - a;
					while (ml >= 0 && mr < B[q].size())
					{
						if (B[q][ml] != B[q][mr])
							break;
						--ml;
						++mr;
					}
					if ((ml >= 0 && mr < B[q].size()))
						break;
				}
				if (q < N)
					continue;
				res = min(res, F(km + j) - F(K));
				break;
			}
			for (j = 0; j < N; ++j)
				reverse(ALL(B[j]));
		}


		printf("Case #%d: %d\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}