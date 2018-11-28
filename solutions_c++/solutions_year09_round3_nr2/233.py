#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((x).size())
#define sqr(x) ((x)*(x))
#define slen(x) ((x).length())

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, m;
double x[600], y[600], z[600], vx[600], vy[600], vz[600];

int main()
{
	int i, j, t;
	
//	freopen("input", "r", stdin);
//	freopen("output", "w", stdout);
	cin >> t;
	double sumX, sumY, sumZ, sumVx, sumVy, sumVz, sumVx2, sumVy2, sumVz2;
	
	for (i = 0; i < t; i++)
	{
		cin >> n;
		sumX = 0;
		sumY = 0;
		sumZ = 0;
		sumVx = 0;
		sumVy = 0;
		sumVz = 0;
		sumVx2 = 0;
		sumVy2 = 0;
		sumVz2 = 0;
		for (j = 0; j < n; j++)
		{
			cin >> x[j] >> y[j] >> z[j] >> vx[j] >> vy[j] >> vz[j];
			sumX += x[j];
			sumY += y[j];
			sumZ += z[j];
			sumVx += vx[j];
			sumVy += vy[j];
			sumVz += vz[j];
		}
		sumVx2 = sumVx * sumVx;
		sumVy2 = sumVy * sumVy;
		sumVz2 = sumVz * sumVz;
		double t = -(sumX * sumVx + sumY * sumVy + sumZ * sumVz);
		if (sumVx2 + sumVy2 + sumVz2 < 1e-7)
			t = 0;
		else
			t /= (sumVx2 + sumVy2 + sumVz2);

		if (t < 1e-7)
			t = 0;

		double ax = 0, ay = 0, az = 0;
		for (j = 0; j < n; j++)
		{
			x[j] += vx[j] * t;
			y[j] += vy[j] * t;
			z[j] += vz[j] * t;
			ax += x[j];
			ay += y[j];
			az += z[j];
		}
		ax /= n;
		ay /= n;
		az /= n;
		printf("Case #%d: %.8lf %.8lf\n", i + 1, abs(sqrt(ax * ax + ay * ay + az * az)), t);
	}
		
	return 0;
}
