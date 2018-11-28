#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i <= b; i++)
#define lod(i, a, b) for(i = a; i >= b; i--)

#define pb push_back

#define PI 3.14159265358979
#define Eps 1e-09

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("C.in", "r"), *outf = fopen("C.out", "w");

double f, R, t, r, g;
double S;

bool check(double x, double y)
{
	if( x * x + y * y < (R-f) * (R-f) - Eps)
		return true;
	return false;
}

double equa(double radi, double known)
{
	return sqrt(radi * radi - known * known);
}

int find(double x)
{
	int res = 0;
	int st, en, mid;

	st = 1, en = (R - r) / (r + r + g);

	while(st <= en)
	{
		mid = (st + en) / 2;

		if( check(x+g, (r+r+g)*mid - r))
		{
			res = mid;
			st = mid + 1;
		}

		else
			en = mid - 1;
	}

	return res;
}

void work()
{
	double x = r, y;
	double s = (g - f - f) * (g - f - f);
	double sx, ex, th2, th1;
	int num;

	if( s <= 0)
	{
		s = 0;
		return;
	}

	while( check(x+f, r))
	{
		y = r;

		num = find(x);		// counting pure squares
		S += s * num;
		y += num * (r + r + g);

		while( check(x+f, y+f))
		{
			if(check(x+f, y + g - f))
				sx = equa( R - f, y + g - f);
			else
				sx = x+f;

			S += (sx - x - f) * (g - f - f);

			if(check(x+g-f, y+f))
				ex = x+g-f;
			else
				ex = equa( R-f, y+f);

			th2 = asin( ex / (R-f));
			th1 = asin( sx / (R-f));

			S += (R-f)*(R-f) / 2 * (th2 - th1) + (sin(2*th2) - sin(2*th1)) / 4 - (ex - sx) * (y + f); 

			y += r+r+g;
		}

		x += r+r+g;
	}
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		fscanf(inf, "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		R -= t;
		S = 0;
		work();
		S *= 4;

		fprintf(outf, "Case #%d: %0.6lf\n", i+1, (PI*(R+t)*(R+t) - S) / (PI * (R+t) * (R+t)));
	}
	return 0;
}