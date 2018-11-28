#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
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
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);

	int i;
	Int X, Y, Z, DX, DY, DZ;
	X = Y = Z = DX = DY = DZ = 0;
	FOR(i, 0, N)
	{
		int x, y, z, dx, dy, dz;
		scanf("%d%d%d", &x, &y, &z);
		scanf("%d%d%d", &dx, &dy, &dz);
		X += x;
		Y += y;
		Z += z;
		DX += dx;
		DY += dy;
		DZ += dz;
	}

	double A = DX*DX + DY*DY + DZ*DZ;
	double B = X*DX + Y*DY + Z*DZ;
	double C = X*X + Y*Y + Z*Z;

	vector<double> v;
	v.PB(0.0);

	if(A != 0)
	{
		double temp = -B/A;
		if(temp >= 0)
			v.PB(temp);
	}

	double res = sqrt(C + 0.0);
	double time = 0.0;
	sort(ALL(v));
	FOR(i, 0, SIZE(v))
	{
		double temp = sqrt(C + B*2*v[i] + A*v[i]*v[i]);
		if(temp < res)
		{
			res = temp;
			time = v[i];
		}
	}

	printf("Case #%d: %.7lf %.7lf\n", test + 1, res/N, time);

	return 0;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	char buf[1 << 10];
	gets(buf);
	int T, t;
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
		SolveTest(t);

	return 0;
};
