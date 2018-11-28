//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

//#define INF 1000000000

//#define ll long long int
//#define INF ( ((ll)1) << 60 )

#define N 111
int n;

char s[N][N];

double W[N], L[N], OW[N], OWP[N], OOWP[N], RPI[N];

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		mset(s, 0);
		mset(OW, 0), mset(OWP, n); mset(OOWP, 0), mset(RPI, n);
		scanf("%d", &n);
		for (i = 0; i < n; ++i) scanf("%s", s[i]);

		// OW
		for (i = 0; i < n; ++i)
		{
			int w = 0, l = 0;
			for (j = 0; j < n; ++j)
			{
				if (s[i][j] == '1') ++w;
				if (s[i][j] == '0') ++l;
			}
			OW[i] = ((double)(w)) / (double)(w+l);
			W[i] = w, L[i] = l;
		}

		// OWP
		for (i = 0; i < n; ++i)
		{
			double sum = 0.0, cnt = 0.0;
			for (j = 0; j < n; ++j)
			{
				if (s[i][j] == '1')
				{
					++cnt;
					sum += (W[j]) / (W[j] - 1 + L[j]);
				}
				if (s[i][j] == '0')
				{
					++cnt;
					sum += (W[j] - 1) / (W[j] - 1 + L[j]);
				}
			}
			OWP[i] = sum / cnt;
		}

		// OOWP
		for (i = 0; i < n; ++i)
		{
			double sum = 0.0, cnt = 0.0;
			for (j = 0; j < n; ++j)
			{
				if (s[i][j] != '.')
				{
					++cnt;
					sum += OWP[j];
				}
			}
			OOWP[i] = sum / cnt;
		}

		printf("Case #%d:\n", cas);

		// RPI
		for (i = 0; i < n; ++i)
		{
			RPI[i] = 0.25 * OW[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			printf("%.9lf\n", RPI[i]);		}
		
		
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}


