#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define pt complex<double>
//kAc
const double pi = acos(-1.0), eps = 1e-9;
const int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1};
const int dy[8] = {0, 0, 1, -1, 1, -1, -1, 1};
const int MO = (int)(1e9 + 7);

#define ALL(x) x.begin(), x.end()
#define fr(x, E) for (__typeof(E.begin()) x = E.begin(); x != E.end(); x++)
#define MP make_pair
#define PB push_back
#define FR first
#define SC second
#define ERR cerr << "ERROR" << endl
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PIII pair<PII, int>
#define PDI pair<double, int>
#define PID pair<int, double>
#define SZ(a) (int)((a).size())
#define VEC vector
#define STR string
#define ISS istringstream
#define OSS ostringstream
#define CLR(a, b) memset(a, b, sizeof(a))
#define gmin(a, b) { if (b < a) a = b; }
#define gmax(a, b) { if (b > a) a = b; }
#define y1 hehehe
using namespace std;
LL w, h;
int Rand()
{
	return (rand() << 15) ^ rand();
}
LL Lrand()
{
	return ((LL)Rand() << 30ll) ^ Rand();
}
pt rp()
{
	LL nw = w * 1000, nh = h * 1000;
	LL x = Lrand() % (nw + 1), y = Lrand() % (nh + 1);
	return pt((double)x / 1000.0, (double) y / 1000.0);
}
int n;
double r[10001]; pt p[1001];
int main()
{
freopen("temp.in", "r", stdin); freopen("temp.out", "w", stdout);
int TEST; cin >> TEST;
for (int ti = 1; ti <= TEST; ti++){
	printf("Case #%d: ", ti);
	cin >> n >> w >> h;
	for (int i = 1; i <= n; i++) cin >> r[i];
//	for (int i = 1; i <= 10; i++) cout << real(rp())  << " " << imag(rp()) << endl;
    int time = 0;
	while(1){
		++time;
		for (int i = 1; i <= n; i++) p[i] = rp();
		bool ok = true;
		for (int i = 1; i <= n; i++)
			for (int j = i + 1; j <= n; j++) if (abs(p[i] - p[j]) < r[i] + r[j]) ok = false;
		if (ok){
			cout << setprecision(10);
			for (int i = 1; i <= n; i++) cout << real(p[i]) << " " << imag(p[i]) << " ";
			cout << endl;
			cerr << time << endl;
			break;
		}
	}
		}	
}

