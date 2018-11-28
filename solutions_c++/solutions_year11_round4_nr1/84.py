#include <cstdio>
#include <algorithm>
using namespace std;

namespace Solve
{
	const int NWALKWAY_MAX = 1005;
	struct Walkway
	{
		int len, speed;
		inline bool operator < (const Walkway &w) const
		{ return speed < w.speed; }
	};
	Walkway walkway[NWALKWAY_MAX];

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		int len, v1, v2, nwkw;
		double t;
		fscanf(fin, "%d%d%d%lf%d", &len, &v1, &v2, &t, &nwkw);
		for (int i = 0; i < nwkw; i ++)
		{
			int a, b;
			fscanf(fin, "%d%d%d", &a, &b, &walkway[i].speed);
			b -= a;
			len -= b;
			walkway[i].len = b;
		}
		walkway[nwkw].speed = 0;
		walkway[nwkw ++].len = len;
		sort(walkway, walkway + nwkw);
		double ans = 0;
		for (int i = 0; i < nwkw; i ++)
		{
			double vmax = (walkway[i].speed + v2);
			double tcur = min(t, walkway[i].len / vmax);
			t -= tcur;
			ans += tcur + (walkway[i].len - tcur * vmax) / (walkway[i].speed + v1);
		}
		fprintf(fout, "Case #%d: %.10lf\n", casenu, ans);
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

