#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()


const double EPS = 1E-08;

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		string s;
//		getline(cin, s);
//		cin >> s;

		int n;
		cin >> n;

		double s_x = 0, s_y = 0, s_z = 0, s_vx = 0, s_vy = 0, s_vz = 0;

		for (int i = 0; i < n; ++i)
		{		
			double x, y, z, vx, vy, vz;
			cin >> x >> y >> z >> vx >> vy >> vz;

			s_x += x; s_y += y; s_z += z;
			s_vx += vx; s_vy += vy; s_vz += vz;
		}

		s_x /= n; s_y /= n; s_z /= n;
		s_vx /= n; s_vy /= n; s_vz /= n;

		double A = s_vx * s_vx + s_vy * s_vy + s_vz * s_vz;
		double B = 2 * s_vx * s_x + 2 * s_vy * s_y + 2 * s_vz * s_z;
		double C = s_x * s_x + s_y * s_y + s_z * s_z;

		double t;

		if (abs(A) <= EPS)
		{
			if (abs(B) <= EPS)
				t = 0.0;
			else
				t = - C / B;
		} else
		{
			t = - B / (2 * A);
		}

		t = max(t, 0.00000000000000000000000000000000001);

		double res = sqrt(max(A * t * t + B * t + C, 0.0));


		printf("Case #%d: %.8f %.8f\n", test + 1, res, t);
	}

}