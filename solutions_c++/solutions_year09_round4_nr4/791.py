#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <complex>
#include <cctype>
#include <climits>
#include <fstream>
#include <iomanip>
using namespace std;

typedef complex<double> P;

const int N = 5;

struct Line
{
	P p1, p2;
	Line(const P &a, const P &b)
		: p1(a), p2(b)
	{}
};

// ŠOÏ
double cross(const P &a, const P &b)
{
	return (a.real() * b.imag() - a.imag() * b.real());
}

P crossPointL(const Line &l1, const Line &l2)
{
	P a = l1.p2-l1.p1;
	P b = l2.p2-l2.p1;
	return (l1.p1+a*cross(b, l2.p1-l1.p1)/cross(b,a));
}


int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	for (in>>T; T>0; --T) {


		static int counter = 0;
		out << "Case #" << ++counter << ": ";

		int n;
		in >> n;

		P p[N];
		double r[N];
		for (int i=0; i < n; ++i) {
			double x, y;
			in >> x >> y >> r[i];
			p[i] = P(x, y);
		}
		if (n==1) {
			out << setprecision(10) << r[0] << endl;
			continue;
		}
		if (n==2) {
			out << setprecision(10) << max(r[1],r[0]) << endl;
			continue;
		}

		double ans = 1e20;
		for (int i=0; i < n; ++i) {
			for (int j=i+1; j < n; ++j) {
				double d = abs(p[j]-p[i]) + r[i]+r[j];
				ans = min(d/2.0, ans);
			}
		}

		if (n==3) {
			P v1 = (p[0]-p[1]) * 0.5;
			P v2 = (p[0]-p[2]) * 0.5;
			P iv1 = v1 * P(0, 1);
			P iv2 = v2 * P(0, 1);
			P c1 = p[0] + v1;
			P c2 = p[0] + v2;
			Line l1(c1, c1+iv1);
			Line l2(c2, c2+iv2);
			P pp = crossPointL(l1, l2);
			double d = abs(pp-p[0])+r[0];
			ans = min(d, ans);
		}

		for (int i=0; i < 3; ++i) {
			ans = max(ans, r[i]);
		}
		out << setprecision(10) << ans << endl;
	}

	in.close();
	out.close();
	return 0;
}
