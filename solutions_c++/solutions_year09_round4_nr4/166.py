#include <queue>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long double ld;

struct pt
{
	ld x, y;
    pt(ld x = 0, ld y = 0): x(x), y(y) {};
};

vector<pt> p;
vector<ld> r;

int n;

pt cc[100][100][2];

ld result;

ld radii;

pt rotate(pt p, ld F)
{
	pt r;

	r.x = p.x * cos(F) - p.y * sin(F);
	r.y = p.x * sin(F) + p.y * cos(F);

    return r;
}

void cover(pt pa, ld ra, pt pb, ld rb, pt& c0, pt& c1)
{
	c0 = c1 = pa;

	if (ra > rb)
    	swap(pa, pb), swap(ra, rb);

    if (radii < ra || radii < rb)
        return;

    if (hypot(pa.x - pb.x, pa.y - pb.y) <= 1E-5)
        return;

    radii -= ra;
    rb -= ra;

    pb.x -= pa.x, pb.y -= pa.y;

    // now pa == 0
    // Ax + By + C == 0

    ld A = - 2 * pb.x;
    ld B = - 2 * pb.y;
    ld C = radii * radii - (radii - rb) * (radii - rb) + pb.x * pb.x + pb.y * pb.y;

    ld A0 = A * A + B * B;
    ld B0 = 2 * B * C;
    ld C0 = C * C - A * A * radii * radii;

    ld D0 = B0 * B0 - 4 * A0 * C0;
    if (D0 >= 0)
    {
    	ld y0 = (- B0 - sqrt(D0)) / 2 / A0;
        ld y1 = (- B0 + sqrt(D0)) / 2 / A0;

        //assert(fabs(A0 * y0 * y0 + B0 * y0 + C0) <= 1E-2);
        //assert(fabs(A0 * y1 * y1 + B0 * y1 + C0) <= 1E-2);

        ld x0 = (- C - B * y0) / A;
        ld x1 = (- C - B * y1) / A;

        //assert(fabs(hypot(x0, y0) - radii) <= 1E-2);
        //assert(fabs(hypot(x0 - pb.x, y0 - pb.y) - (radii - rb)) <= 1E-2);

        //assert(fabs(hypot(x1, y1) - radii) <= 1E-2);
        //assert(fabs(hypot(x1 - pb.x, y1 - pb.y) - (radii - rb)) <= 1E-2);

        c0 = pt(x0, y0);
        c1 = pt(x1, y1);
    }

    c0.x += pa.x;
    c0.y += pa.y;

    c1.x += pa.x;
    c1.y += pa.y;

    radii += ra;
}

bool inside(pt p, ld r, pt c, ld rc)
{
	return sqrt((c.x - p.x) * (c.x - p.x) + (c.y - p.y) * (c.y - p.y)) + r <= rc + 1E-9;
}

bool check(pt c1, const vector<bool>& used)
{
        forn(i, n)
        	if (!used[i] && !inside(p[i], r[i], c1, radii))
            	return false;
        return true;
}

bool cover(pt c0)
{
        vector<bool> used(n, false);

        forn(i, n)
        	if (inside(p[i], r[i], c0, radii))
            	used[i] = true;

        forn(i, n)
        	forn(j, n)
            {
            	if (check(cc[i][j][0], used))
                	return true;
                if (check(cc[i][j][1], used))
                	return true;
            }

        return false;
}

bool cover(ld radii)
{
	::radii = radii;

	forn(i, n)
    	forn(j, n)
        	if (i == j)
            	cc[i][j][0] = cc[i][j][1] = p[i];
            else
            {
            	pt a = rotate(p[i], 121);
            	pt b = rotate(p[j], 121);
            	cover(a, r[i], b, r[j], cc[i][j][0], cc[i][j][1]);
                cc[i][j][0] = rotate(cc[i][j][0], -121);
                cc[i][j][1] = rotate(cc[i][j][1], -121);
            }

    forn(i, n)
    	forn(j, n)
        {
        	if (cover(cc[i][j][0]))
            	return true;
        	if (cover(cc[i][j][1]))
            	return true;
        }
}

void readData()
{
	cin >> n;
    p.resize(n);
    r.resize(n);
    forn(i, n)
    {
    	cin >> p[i].x >> p[i].y >> r[i];
    }
}

void solve()
{
	ld lf = 0;
    ld rg = 1E6;

    //cout << cover(1000) << endl;

    forn(tt, 100)
    {
    	ld mid = (lf + rg) / 2.0;
        if (cover(mid))
        	rg = mid;
        else
        	lf = mid;
    }
	result = (lf + rg) / 2.0;
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int beginIndex = atoi(argv[1]);
	int endIndex = atoi(argv[2]);

	int testCount;

	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &testCount);
	
	for (int tt = 1; tt <= testCount; tt++)
	{
		readData();

		if (beginIndex <= tt && tt <= endIndex)
		{
			solve();
			printf("Case #%d: %.10lf\n", tt, double(result));
		}
	}

	fclose(stdin);
    fclose(stdout);
	
    return 0;
}
