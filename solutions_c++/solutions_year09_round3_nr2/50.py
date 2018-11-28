#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

int n;
struct p{
	double x, y, z;
};
p a[100000], v[100000];
double solve(double t){
	double x = 0, y = 0, z = 0;
	forn(i, n){
		x += (a[i].x + v[i].x * t);
		y += (a[i].y + v[i].y * t);
		z += (a[i].z + v[i].z * t);
	}
	x /= (1.0 * n);
	y /= (1.0 * n);
	z /= (1.0 * n);
	return sqrt(x * x + y * y + z * z);
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(q, t){
		
		cin >> n;
		forn(i, n)
			cin >> a[i].x >> a[i].y >> a[i].z >> v[i].x >> v[i].y >> v[i].z;
		double t;
		double zn = 0, zn1 = 0, zn2 = 0, zn3 = 0, znv1 = 0, znv2 = 0, znv3 = 0;
		forn(i, n){
			zn1 += a[i].x;
			znv1 += v[i].x;
			zn2 += a[i].y;
			znv2 += v[i].y;
			zn3 += a[i].z;
			znv3 += v[i].z;
		}
		zn = (zn1 * znv1 + zn2 * znv2 + zn3 * znv3) / (1.0 * n * n);
		double ch1 = 0, ch2 = 0, ch3 = 0;
		double ch = 0;
		forn(i, n){
			ch1 += (v[i].x);
			ch2 += (v[i].y);
			ch3 += (v[i].z);
		}
		ch1 /= (1.0 * n);
		ch2 /= (1.0 * n);
		ch3 /= (1.0 * n);
		ch1 *= ch1;
		ch2 *= ch2;
		ch3 *= ch3;
		ch = ch1 + ch2 + ch3;
		if (ch == 0)
			t = 0;
		else
			t = - zn / ch;
		if (t < 0 || abs(t) < 0.00000001)
			t = 0;
		
			
			double d = solve(t);
		printf("Case #%d: %lf %lf\n", q + 1, d, t);
		
	}
	return 0;
}