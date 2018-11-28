
#define _CRT_SECURE_NO_DEPRECATE 

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

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

const int SZ = 1 << 9;

int tests;

int n, m, d;

int w[SZ][SZ];

Long hs[SZ][SZ];
Long vs[SZ][SZ];

Long hsx[SZ][SZ];
Long vsx[SZ][SZ];

Long hsy[SZ][SZ];
Long vsy[SZ][SZ];

Long get_sum_h(int i, int j1, int j2)
{
	if(j1 > j2)
		swap(j1, j2);
	return hs[i][j2] - (j1 ? hs[i][j1 - 1] : 0);
}


Long get_sum_hx(int i, int j1, int j2)
{
	if(j1 > j2)
		swap(j1, j2);
	return hsx[i][j2] - (j1 ? hsx[i][j1 - 1] : 0);
}

Long get_sum_hy(int i, int j1, int j2)
{
	if(j1 > j2)
		swap(j1, j2);
	return hsy[i][j2] - (j1 ? hsy[i][j1 - 1] : 0);
}

Long get_sum_v(int j, int i1, int i2)
{
	if(i1 > i2)
		swap(i1, i2);
	return vs[i2][j] - (i1 ? vs[i1 - 1][j] : 0);
}

Long get_sum_vx(int j, int i1, int i2)
{
	if(i1 > i2)
		swap(i1, i2);
	return vsx[i2][j] - (i1 ? vsx[i1 - 1][j] : 0);
}

Long get_sum_vy(int j, int i1, int i2)
{
	if(i1 > i2)
		swap(i1, i2);
	return vsy[i2][j] - (i1 ? vsy[i1 - 1][j] : 0);
}

inline bool valid(int i, int j)
{
	if(i < 0 || i >= n)
		return false;
	if(j < 0 || j >= m)
		return false;
	return true;
}

void add(Long &sumx, Long &sumy, int ii, int jj, int i, int j)
{
	sumx += (Long)(ii - i) * w[ii][jj];
	sumy += (Long)(jj - j) * w[ii][jj];
}

void add2(Long &sumx, Long &sumy, int ii, int jj, int i, int j)
{
	sumx += (Long)(2 * ii - 2 * i - 1) * w[ii][jj];
	sumy += (Long)(2 * jj - 2 * j - 1) * w[ii][jj];
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d%d%d", &n, &m, &d);
		REP(i, n)
			REP(j, m)
			{
				scanf("%1d", &w[i][j]);
				w[i][j] += d;
			}
		REP(i, n)
		{
			Long sum = 0, sumx = 0, sumy = 0;
			REP(j, m)
			{
				hs[i][j] = sum += w[i][j];
				hsx[i][j] = sumx += w[i][j] * (Long)i;
				hsy[i][j] = sumy += w[i][j] * (Long)j;
			}
		}
		
		REP(j, m)
		{
			Long sum = 0, sumx = 0, sumy = 0;
			REP(i, n)
			{
				vs[i][j] = sum += w[i][j];
				vsx[i][j] = sumx += w[i][j] * (Long)i;
				vsy[i][j] = sumy += w[i][j] * (Long)j;
			}
		}

		int res = -1;
		REP(i, n)
			REP(j, m)
			{
				bool v = true;
				Long sumx = 0, sumy = 0;
				FOR(ii, i - 1, i + 2)
					FOR(jj, j - 1, j + 2)
					{
						bool b = (abs(ii - i) != 1) || (abs(jj - j) != 1);
						if(!b)
							continue;
						if(!valid(ii, jj))
						{
							v = false;
							break;
						}
						sumx += (Long)(ii - i) * w[ii][jj];
						sumy += (Long)(jj - j) * w[ii][jj];
					}
				if(!v)
					continue;
				if(!sumx && !sumy)
					res = max(res, 3);
				int i1 = i - 1, i2 = i + 1;
				int j1 = j - 1, j2 = j + 1;

				int k = 3;
				while(true)
				{
					add(sumx, sumy, i1, j1, i, j);
					add(sumx, sumy, i1, j2, i, j);
					add(sumx, sumy, i2, j1, i, j);
					add(sumx, sumy, i2, j2, i, j);
					--i1, ++i2;
					--j1, ++j2;
					k += 2;
					if(!valid(i1, j1)) break;
					if(!valid(i2, j2)) break;
					sumx += get_sum_hx(i1, j1 + 1, j2 - 1);
					sumy += get_sum_hy(i1, j1 + 1, j2 - 1);
					sumx -= get_sum_h(i1, j1 + 1, j2 - 1) * i;
					sumy -= get_sum_h(i1, j1 + 1, j2 - 1) * j;

					
					sumx += get_sum_hx(i2, j1 + 1, j2 - 1);
					sumy += get_sum_hy(i2, j1 + 1, j2 - 1);
					sumx -= get_sum_h(i2, j1 + 1, j2 - 1) * i;
					sumy -= get_sum_h(i2, j1 + 1, j2 - 1) * j;

					sumx += get_sum_vx(j1, i1 + 1, i2 - 1);
					sumy += get_sum_vy(j1, i1 + 1, i2 - 1);
					sumx -= get_sum_v(j1, i1 + 1, i2 - 1) * i;
					sumy -= get_sum_v(j1, i1 + 1, i2 - 1) * j;

					sumx += get_sum_vx(j2, i1 + 1, i2 - 1);
					sumy += get_sum_vy(j2, i1 + 1, i2 - 1);
					sumx -= get_sum_v(j2, i1 + 1, i2 - 1) * i;
					sumy -= get_sum_v(j2, i1 + 1, i2 - 1) * j;

					if(!sumx && !sumy)
						res = max(res, k);
				}

			}

		REP(i, n)
			REP(j, m)
			{
				Long sumx = 0, sumy = 0;
				int i1 = i, i2 = i + 1;
				int j1 = j, j2 = j + 1;

				int k = 2;
				while(true)
				{
					add2(sumx, sumy, i1, j1, i, j);
					add2(sumx, sumy, i1, j2, i, j);
					add2(sumx, sumy, i2, j1, i, j);
					add2(sumx, sumy, i2, j2, i, j);
					--i1, ++i2;
					--j1, ++j2;
					k += 2;
					if(!valid(i1, j1)) break;
					if(!valid(i2, j2)) break;
					sumx += get_sum_hx(i1, j1 + 1, j2 - 1) * 2;
					sumy += get_sum_hy(i1, j1 + 1, j2 - 1) * 2;
					sumx -= get_sum_h(i1, j1 + 1, j2 - 1) * (2 * i + 1);
					sumy -= get_sum_h(i1, j1 + 1, j2 - 1) * (2 * j + 1);

					
					sumx += get_sum_hx(i2, j1 + 1, j2 - 1) * 2;
					sumy += get_sum_hy(i2, j1 + 1, j2 - 1) * 2;
					sumx -= get_sum_h(i2, j1 + 1, j2 - 1) * (2 * i + 1);
					sumy -= get_sum_h(i2, j1 + 1, j2 - 1) * (2 * j + 1);

					sumx += get_sum_vx(j1, i1 + 1, i2 - 1) * 2;
					sumy += get_sum_vy(j1, i1 + 1, i2 - 1) * 2;
					sumx -= get_sum_v(j1, i1 + 1, i2 - 1) * (2 * i + 1);
					sumy -= get_sum_v(j1, i1 + 1, i2 - 1) * (2 * j + 1);

					sumx += get_sum_vx(j2, i1 + 1, i2 - 1) * 2;
					sumy += get_sum_vy(j2, i1 + 1, i2 - 1) * 2;
					sumx -= get_sum_v(j2, i1 + 1, i2 - 1) * (2 * i + 1);
					sumy -= get_sum_v(j2, i1 + 1, i2 - 1) * (2 * j + 1);

					if(!sumx && !sumy)
						res = max(res, k);
				}

			}
		cerr << I + 1 << endl;
		printf("Case #%d: ", ++I);
		if(res == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", res);
	}
	return 0;
}