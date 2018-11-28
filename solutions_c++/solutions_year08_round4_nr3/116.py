#include <iostream>
#include <cmath>
using namespace std;
const int MAX = 15;

int n;
struct INFO
{
	double x, y, z, p;
}ship[MAX], st, end, temp, nst, nend;

int main (void)
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, Case = 1;
	scanf("%d", &T);
	while(T --)
	{
		scanf("%d", &n);
		int ii;
		st.x = st.y = st.z = 1e10;
		end.x = end.y = end.z = -1e10;
		for (ii = 0; ii < n; ++ ii)
		{
			scanf("%lf %lf %lf %lf", &ship[ii].x, &ship[ii].y, &ship[ii].z, &ship[ii].p);
			if (ship[ii].x < st.x) st.x = ship[ii].x;
			if (ship[ii].y < st.y) st.y = ship[ii].y;
			if (ship[ii].z < st.z) st.z = ship[ii].z;
			if (ship[ii].x > end.x) end.x = ship[ii].x;
			if (ship[ii].y > end.y) end.y = ship[ii].y;
			if (ship[ii].z > end.z) end.z = ship[ii].z;
		}

		nst = st; nend = end;
		double base = 100000;
		double i, j, k, t, tt;
		int q;
		while (base > 1e-6)
		{
			temp.p = 1e100;
			for (i = st.x; i <= end.x; i += base)
				for (j = st.y; j <= end.y; j += base)
					for (k = st.z; k <= end.z; k += base)
					{
						t = 0;
						for (q = 0; q < n; ++ q)
						{
							tt = (fabs(i-ship[q].x) + fabs(j-ship[q].y) + fabs(k-ship[q].z))/ship[q].p;
							if (tt > t)
								t = tt;
						}
						if (temp.p > t)
						{
							temp.p = t;
							temp.x = i; temp.y = j; temp.z = k;
						}
					}
			st.x = temp.x-base; end.x = temp.x+base;
			st.y = temp.y-base; end.y = temp.y+base;
			st.z = temp.z-base; end.z = temp.z+base;
			if (st.x < nst.x) st.x = nst.x;
			if (st.y < nst.y) st.y = nst.y;
			if (st.z < nst.z) st.z = nst.z;
			if (end.x > nend.x) end.x = nend.x;
			if (end.y > nend.y) end.y = nend.y;
			if (end.z > nend.z) end.z = nend.z;
			base /= 10;
		}
		printf("Case #%d: %.8lf\n", Case++, temp.p);
	}
	return 0;
}