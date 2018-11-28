#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

const double EPS = 1e-7;


double xx1, yy1, xx2, yy2, xx3, yy3, r1, r2, r3;
double s1, s2, s3, q, q1, q2, q3;
int tt, n;

inline double msqr(double a)
{
	return a * a;
}

inline bool f(double a, double b)
{
	if (b - a > EPS) return true;
	else return false;
}

int main()
{
	in >> tt;
	for (int t = 0; t < tt; t++) {
		out << "Case #" << t + 1 << ": ";
		in >> n;
		if (n == 3) {
			in >> xx1 >> yy1 >> r1 >> xx2 >> yy2 >> r2 >> xx3 >> yy3 >> r3;
			s1 = (sqrt(msqr(xx1 - xx2) + msqr(yy1 - yy2)) + r1 + r2) / 2.0;
			s2 = (sqrt(msqr(xx2 - xx3) + msqr(yy2 - yy3)) + r2 + r3) / 2.0;
			s3 = (sqrt(msqr(xx1 - xx3) + msqr(yy1 - yy3)) + r1 + r3) / 2.0;

			if (f(r3, s1)) q1 = s1;
			else q1 = r3;

			if (f(r1, s2)) q2 = s2;
			else q2 = r1;

			if (f(r2, s3)) q3 = s3;
			else q3 = r2;

			q = q1;
			if (f(q2, q)) q = q2;
			if (f(q3, q)) q = q3;
		}
		else if (n == 2) {
			in >> xx1 >> yy1 >> r1 >> xx2 >> yy2 >> r2;
			q = r1;
			if (f(q, r2)) q = r2;
		}
		else if (n == 1) {
			in >> xx1 >> yy1 >> r1;
			q = r1;
		}

		out << fixed << setprecision(6) << q << endl;		
	}

	return 0;
}
