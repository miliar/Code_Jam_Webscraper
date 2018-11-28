#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

#define PI 3.14159265358979323846264338327950288419716939
#define EPS 1e-9

double f, R, t, r, g, rin, ans, R2;
int tc;

double dist(double x1, double y1)
{
	return x1 * x1 + y1 * y1;
}

double area3(double x1, double y1, double x2, double y2, double x3, double y3)
{
	return abs(x1 * y2 + x2 * y3 + x3 * y1 
			       - x2 * y1 - x3 * y2 - x1 * y3) / 2.0;
}

int main()
{
	int i;
	double x, y, delta, sy, size, rin2, size2, in1, in2, angle1, angle2, extra;
	
	scanf("%d", &tc);
	FOR(i, tc)
	{
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		ans = 0.0;

		if (g > 2 * f)
		{
			R2 = R * R;
			rin = R - t - f; rin2 = rin * rin;
			size = g - 2 * f; size2 = size * size;
			x = sy = r + (g - size) / 2;
			delta = r + g + r;

//			fprintf(stderr, "prelim: %lf :: %lf :: %lf :: %lf\n", rin, size, x, delta);
			
			for (; dist(x, sy) < rin2; x += delta)
			{
				for (y = sy; dist(x, y) < rin2; y += delta)
				{
					if (dist(x + size, y + size) + EPS < rin2) ans += size2;
					else // need to calculate the intersection
					{
						if (dist(x, y + size) + EPS > rin2)
						{   
							// |
							// +--
							if (dist(x + size, y) + EPS > rin2)
							{
//fprintf(stderr, "here1\n");
								in1 = sqrt(rin2 - x * x);
								in2 = sqrt(rin2 - y * y);
								angle1 = atan(in1 / x);
								angle2 = atan(y / in2);
								ans += rin2 * (angle1 - angle2) / 2 - 
									     area3(x, y, 0, 0, x, in1) - 
											 area3(x, y, 0, 0, in2, y);
//fprintf(stderr, "%lf -- %lf -- %lf -- %lf -- %lf -- %lf -- %lf\n", x, y, in1, in2, angle1, angle2);
//fprintf(stderr, "%lf %lf %lf\n", rin2 * (angle1 - angle2), area3(x, y, 0, 0, x, in1), area3(x, y, 0, 0, in2, y));
							}
							// |   |
							// +---+
							else
							{
//fprintf(stderr, "here2\n");
								in1 = sqrt(rin2 - x * x);
								in2 = sqrt(rin2 - (x + size) * (x + size));
								angle1 = atan(in1 / x);
								angle2 = atan(in2 / (x + size));
								extra = (x + size) * y / in2;

//fprintf(stderr, "%lf -- %lf -- %lf -- %lf\n", in1, in2, angle1, angle2);
								ans += rin2 * (angle1 - angle2) / 2 - 
									     area3(x, y, 0, 0, x, in1) -
											 area3(x, y, 0, 0, extra, y) + 
											 area3(x + size, y, x + size, in2, extra, y);
							}
						}
						else 
						{
							// +--
							// |
							// +--
							if (dist(x + size, y) + EPS > rin2)
							{
//fprintf(stderr, "here3\n");
								in1 = sqrt(rin2 - y * y);
								in2 = sqrt(rin2 - (y + size) * (y + size));
								angle2 = atan(y / in1);
								angle1 = atan((y + size) / in2);
								extra = (y + size) * x / in2;
								
//fprintf(stderr, "%lf -- %lf -- %lf -- %lf\n", in1, in2, angle1, angle2);
								ans += rin2 * (angle1 - angle2) / 2 -
								       area3(x, y, 0, 0, in1, y) -
											 area3(x, y, 0, 0, x, extra) +
											 area3(x, y + size, in2, y + size, x, extra);
							}
							// +--
							// |   |
							// +---+
							else
							{
//fprintf(stderr, "here4\n");
								in1 = sqrt(rin2 - (y + size) * (y + size));
								in2 = sqrt(rin2 - (x + size) * (x + size));
								angle1 = atan((y + size) / in1);
								angle2 = atan(in2 / (x + size));
//fprintf(stderr, "%lf -- %lf -- %lf -- %lf\n", in1, in2, angle1, angle2);
								ans += rin2 * (angle1 - angle2) / 2 - 
									     area3(in1, y + size, 0, 0, x + size, in2) +
											 area3(in1, y + size, x, y + size, x, y) + 
											 area3(in1, y + size, x, y, x + size, in2) + 
											 area3(x + size, in2, x, y, x + size, y);
							}
						}
					}
//fprintf(stderr, "%lf\n", ans);
				}
			}
			ans /= R2 * PI;
//fprintf(stderr, "area = %lf\n", R2 * PI / 4);
		}

		printf("Case #%d: %.6lf\n", i + 1, 1.0 - ans * 4);
	}
	return 0;
}

