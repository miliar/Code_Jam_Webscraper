/*###################START INCLUDE-urile#########################/*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

/*###################STOP INCLUDE-urile#########################/*/
using namespace std;
/*######################START PRECODE#############################*/
const long double eps = 1e-7; // marja de eroare
const long double pi=acos(-1.0);//valoarea lui PI
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int,int> PII;
#define PB push_back  //vector<> v.PB(X);
#define NP next_permutation //v.NP()
#define MP make_pair //MP
#define X first //.X 
#define Y second //.Y
#define ALL(a) (a).begin(), (a).end() //sort(ALL(v))
#define RALL(a) (a).rbegin(), (a).rend()//sort(RALL(v)) //sens invers
#define FORIT(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it) //parcurg cu iteratoru//FORIT(it, V) {cout << *it << '\n';}
#define STERGE(v) memset(v,0,sizeof v) //set 0 on something
long long BIG_INF =  0x3f3f3f3f;
#define STERGEI(v) memset(v,0x3f, sizeof(v)) //set cu infinit
//memcmp
typedef stringstream iss; //iss f(string); f>>X; sau f << X;//sau de output
/*#####################TEMPLATES##################################*/

template<class A, class B> inline A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //string x = i2s<string, int>(X);
template<class A> inline A abs(A a) {if (a < 0) return -a; return a;} //
//__gcd(A, B) - euclidu
template<class A> inline A euclid(A a, A b, A &x, A &y) {
	if (!b) {x=1, y = 0; return a;} 
	A ret = euclid(b, a%b, x, y);
	A aux = x; 
	x = y; y = aux - (a/b)*y;
	return ret;
} ///euclid(556, 21, A, B); si A * 556 + B * 21 = gcd-ul
//de verificad daca e prim
template<class A> inline int isPrime(A X) {
	if (X <= 1 || (X % 2 == 0 && X != 2)) return 0;
	for (A i = 3; i * i <= X; i+=2) if (X % i == 0) return 0;
	return 1;
} ///isPrime(22531);


void solve();
int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
int N, M;
int D;
LL v[501][501];
LL sum_l[501][501], sum_c[501][501];
LL w_ld[501][501], w_ls[1001][1001];
LL w_cd[501][501], w_cs[1001][1001];
void solve()
{
	cin >> N >> M;
	cin >> D;
	memset(v, 0, sizeof(v));
	memset(sum_l, 0, sizeof(sum_l));
	memset(sum_c, 0, sizeof(sum_c));
	memset(w_ld, 0, sizeof(w_ld));
	memset(w_ls, 0, sizeof(w_ls));
	memset(w_cd, 0, sizeof(w_cd));
	memset(w_cs, 0, sizeof(w_cs));

	for (int i = 1; i <= N; ++i)
	{
		string l;
		cin >> l;
		for (int j = 1; j <= M; ++j)
			v[i][j] = l[j-1] - '0' + D;
	}
	// sum_l
	for (int j = 1; j <= M; ++j)
	{
		for (int i = 1; i <= N; ++i)
			sum_l[i][j] = sum_l[i-1][j] + v[i][j];
		for (int i = 1; i <= N; ++i)
			w_ls[i][j] = w_ls[i-1][j] + LL(v[i][j]) * LL(2 * i - 1);
		for (int i = N; i >= 1; i--)
			w_ld[i][j] = w_ld[i+1][j] + LL(v[i][j]) * LL(2 * N - 2 * i + 1);
	}
	// sum_c
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= M; ++j)
			sum_c[i][j] = sum_c[i][j-1] + v[i][j];
		for (int j = 1; j <= M; ++j)
			w_cs[i][j] = w_cs[i][j-1] + LL(v[i][j]) * LL(2 * j - 1);
		for (int j = M; j >= 1; --j)
			w_cd[i][j] = w_cd[i][j+1] + LL(v[i][j]) * LL(2 * M - 2 * j + 1);
	}
	int best = 0;
	// pick a centru
	for (int cx = 1; cx < 2 * N; ++cx)
		for (int cy = 1; cy < 2 * M; ++cy)
		{
			LL K = 2;
			LL px = (cx + 1) / 2;
			LL py = (cy + 1) / 2;
			if (cx % 2 == 1 && cy % 2 == 1) K = 1;
			LL dx = 0, dy = 0;
			if (K == 2)
			{
				dx = v[px+1][py] + v[px+1][py+1] - v[px][py] - v[px][py+1];
				dy = v[px][py+1] + v[px+1][py+1] - v[px][py] - v[px+1][py];
			}
			LL vx, vy;
			if (K == 1) vx = vy = 0;
			else vx = vy = 1;
			while (1)
			{
				px--; py--;
				if (px == 0 || py == 0) break;
				K += 2;
				// fix dx
				vx += 2; vy += 2;

				dx +=LL(sum_c[px + K - 1][py + K - 1] - sum_c[px + K -
						1][py - 1]) * vx;
				dx -=LL(sum_c[px][py + K - 1] - sum_c[px][py-1]) * vx;

				// fix dy
				dy +=LL(sum_l[px + K - 1][py + K - 1] - sum_l[px - 1][py +
						K - 1]) * vy;
				dy -=LL(sum_l[px + K - 1][py] - sum_l[px-1][py]) * vy;
				if (K >= 3)
				{
					LL x = w_ls[px + K - 2][py] - w_ls[px][py];
					x += w_ls[px + K - 2][py + K - 1] - w_ls[px][py + K -
						1];
					// centru la 0
					x -= LL(cx) * LL(sum_l[px + K - 2][py] - sum_l[px][py]
							+ sum_l[px + K - 2][py + K - 1] -
							sum_l[px][py+K-1]); 
					dx += x;

					LL y = w_cs[px][py + K - 2] - w_cs[px][py];
					y += w_cs[px+K-1][py + K - 2] - w_cs[px + K - 1][py];

					y -= LL(cy) * LL(sum_c[px][py + K - 2] - sum_c[px][py]
							+ sum_c[px+K-1][py + K - 2] -
							sum_c[px+K-1][py]);
					dy += y;
					if (K >= 3 && K > best)
					{
						LL ax = dx;
						LL ay = dy;
						ax -= LL(v[px+K-1][py] + v[px+K-1][py+K-1] - v[px][py]
							- v[px][py + K - 1]) * vx;
						ay -= LL(v[px][py+K-1] + v[px+K-1][py+K-1] -
								v[px][py] - v[px+K-1][py]) * vy;
						if (ax == 0 && ay == 0)
							best = K;
					}
				}
			}
		}
	if (best < 3)
		cout << "IMPOSSIBLE\n";
	else cout << best << '\n';
}
