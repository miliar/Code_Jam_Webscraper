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

char B[110][110];

Double WP[110];
Double OWP[110];
Double OOWP[110];

int main()
{
//	freopen("-small.in", "r", stdin);
//	freopen("-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%s", B[i]);
		for (int i = 0; i < N; ++i)
		{
			int k = 0;
			int w = 0;
			for (int j = 0; j < N; ++j)
			{
				if (B[i][j] != '.')
					++k;
				if (B[i][j] == '1')
					++w;
			}
			WP[i] = w/(Double)k;
		}
		for (int ip = 0; ip < N; ++ip)
		{
			Double sum = 0;
			int ko = 0;
			for (int i = 0; i < N; ++i)
				if (B[ip][i] != '.')
				{
					++ko;
					int k = 0;
					int w = 0;
					for (int j = 0; j < N; ++j)
					{
						if (j == ip)
							continue;
						if (B[i][j] != '.')
							++k;
						if (B[i][j] == '1')
							++w;
					}
					sum += w/(Double)k;
				}
			OWP[ip] = sum / ko;
		}
		for (int i = 0; i < N; ++i)
		{
			Double sum = 0;
			int ko = 0;
			for (int j = 0; j < N; ++j)
				if (B[i][j] != '.')
				{
					++ko;
					sum += OWP[j];
				}
			OOWP[i] = sum / ko;
		}
		printf("Case #%d:\n", t+1);
		for (int i = 0; i < N; ++i)
		{
			double rpi = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
			printf("%.12lf\n", rpi);
		}
	}
	return 0;
}