#include <cstdio>
#define _USE_MATH_DEFINES
#include <cmath>
#include <cstdlib>
#include <cfloat>

#define MY_FLT_EPSILON     2.2204460492503131e-016 
//#define MY_FLT_EPSILON 0.000001

// FLT_EPSILON
bool double_eq(double a, double b)
{
	return (b - MY_FLT_EPSILON <= a) && (a <= b + MY_FLT_EPSILON);
}

bool double_ls(double a, double b)
{
	return b - a > MY_FLT_EPSILON;
}

bool double_gt(double a, double b)
{
	return a - b > MY_FLT_EPSILON;
}

double get_circle_area(double r)
{
	return M_PI * r * r;
}

// 360 -> 2*PI
double degree_to_radian(double degree)
{
	return degree / 18.0 * M_PI;
}

bool is_hit_vert_in_plus_zone(double x, double r, double g)
{
	double r_g_2 = r + 0.5 * g;
	double r2_g = 2.0 * r + g;

	// 세로줄 검사 ||||
	while(double_gt(x, r_g_2))
		x -= r2_g;

	while(double_ls(x, -r_g_2))
		x += r2_g;

	return (double_ls(-r, x) && double_ls(x, r));
}

bool is_hit_horiz_in_plus_zone(double y, double r, double g)
{
	double r_g_2 = r + 0.5 * g;
	double r2_g = 2.0 * r + g;

	// 가로줄 검사 ----
	while(double_gt(y, r_g_2))
		y -= r2_g;

	return (double_ls(-r, y) && double_ls(y, r));
}

bool is_hit_in_plus_zone(double x, double y, double r, double g)
{
	if(is_hit_vert_in_plus_zone(x, r, g))
		return true;
	else if(is_hit_horiz_in_plus_zone(y, r, g))
		return true;
	return false;
}

// @assume: 1사분면
double solve(double f, double R, double t, double r, double g)
{
	// 다음은 가정에 의하여 이루어진다. ( f 를 0 이라고 보는 대신 )
	t = t + f;
	r = r + f;
	g = g - 2.0 * f;

	double inR = R-t;

	double plus_zone_area = R * R;
	double outer_circle_area = M_PI * R * R / 4.0;
	double azone_area = M_PI * inR * inR / 4.0; // 1사분면 azone ( inner circle area )
	double bzone_area = outer_circle_area - azone_area;
	double czone_area = plus_zone_area - outer_circle_area;
	// All-Zone Prob
	double prob;

	long long azone_count = 0;
	long long azone_hit = 0;

	long long part_num = 20000000;

	for(int xi=0; xi<part_num; ++xi)
	{
		double x = -inR + (2.0 * inR * ((double)xi / (double)part_num));
		double inCircleBoundY = sqrt(inR * inR - x * x);

		if(is_hit_vert_in_plus_zone(x, r, g))
		{
			long long add_count = (long long)((2.0 * inCircleBoundY) / (2.0 * inR) * (double)part_num);
			azone_count += add_count;
			azone_hit += add_count;
		}
		// 비록 세로줄에 걸리지 않더라도
		// 가로줄의 두께만큼 .. 빠르게 통과한다.
		else
		{
			double rgr = r + g + r;

			double stringTotalWeight = 0.0; // 이것만2배씩
			double y;

			long long n = (long long)(inCircleBoundY / rgr);
			y = (double)n * rgr; // problem..
			stringTotalWeight += 2.0 * (double)n * (2.0*r);

			// 남은부분(while 이지만 1번만 돈다. break 이점을 보려고 일부러 while 했음)
			do {
				// 1. r 만큼 간다.
				y += r;
				stringTotalWeight += 2.0 * r;
				if(double_gt(y, inCircleBoundY))
				{
					stringTotalWeight -= 2.0 * (y - inCircleBoundY);
					break;
				}

				// 2. g 만큼 간다
				y += g;
				if(double_gt(y, inCircleBoundY))
					break;

				// 3. r 만큼 간다
				y += r;
				stringTotalWeight += 2.0 * r;
				if(double_gt(y, inCircleBoundY))
				{
					stringTotalWeight -= 2.0 * (y - inCircleBoundY);
					break;
				}
			} while(false);

			long long add_count = (long long)((2.0 * inCircleBoundY) / (2.0 * inR) * (double)part_num);
			azone_count += add_count;

			long long add_hit = (long long)(stringTotalWeight / (2.0 * inR) * (double)part_num);
			azone_hit += add_hit;
		}
	}

	prob = 0;

	double azone_hit_ratio;
	if(azone_count == 0)
		azone_hit_ratio = 0.0;
	else
		azone_hit_ratio = (double)azone_hit / (double)azone_count;
	prob += (azone_area / outer_circle_area) * azone_hit_ratio;

	double bzone_hit_ratio = 1.0;
	prob += (bzone_area / outer_circle_area) * bzone_hit_ratio;

	return prob;
}

int main(int argc, char* argv[])
{
	int N;
	scanf("%d", &N);
	for(int ni=0; ni<N; ++ni)
	{
		double f, R, t, r, g;
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		printf("Case #%d: %.6lf\n", ni+1, solve(f, R, t, r, g));
	}
}

