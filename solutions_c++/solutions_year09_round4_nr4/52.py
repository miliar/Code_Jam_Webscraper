#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>

using namespace std;

#define EPS 1e-8
#define SQR(d) ((d) * (d))

typedef complex<double> vector_t;
typedef complex<double> point_t;

double dot(const vector_t &a, const vector_t &b) { return real(conj(a) * b); }
double cross(const vector_t &a, const vector_t &b) { return imag(conj(a) * b); }
vector_t perpendicular_vector(const vector_t &v) { 	return vector_t(imag(v), -real(v)); }

struct circle_t
{
	point_t origin;
	double r;
};

int N;
circle_t circles[45];
circle_t poss[45];

int intersect(const circle_t &a, const circle_t &b, point_t &p, point_t &q)
{
	vector_t u = b.origin - a.origin;
	vector_t v = perpendicular_vector(u);

	double length_u = abs(u);
	double s = ((SQR(a.r) - SQR(b.r)) / SQR(length_u) + 1.0) / 2.0;
	double t = SQR(a.r) / SQR(length_u) - SQR(s);
	if (t < -EPS) return 0;

	p = a.origin + s * u + sqrt(t) * v;
	q = a.origin + s * u - sqrt(t) * v;
	return 2;
}

int n_ips;
point_t ips[2000];
long long mask[2000];

bool can(double R)
{
	n_ips = 0;
	for (int i = 0; i < N; ++i)
	{
		poss[i] = circles[i];
		poss[i].r = R - poss[i].r;
		ips[n_ips++] = poss[i].origin;
	}

	for (int i = 0; i < N; ++i)
		for (int j = i + 1; j < N; ++j)
		{
			point_t p, q;
			if (intersect(poss[i], poss[j], p, q))
			{
				ips[n_ips++] = p;
				ips[n_ips++] = q;
//				printf("%lf %lf\n", abs(p - poss[i].origin), poss[i].r);
//				printf("%lf %lf\n", abs(p - poss[j].origin), poss[j].r);
//				printf("%lf %lf\n", abs(q - poss[i].origin), poss[i].r);
//				printf("%lf %lf\n", abs(q - poss[j].origin), poss[j].r);
			}
		}

	memset(mask, 0, sizeof(mask));
	for (int i = 0; i < n_ips; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			double D = abs(ips[i] - circles[j].origin) + circles[j].r;
			if (D <= R + EPS) mask[i] |= 1LL << j;
		}
	}

	for (int i = 0; i < n_ips; ++i)
		for (int j = 0; j < n_ips; ++j)
			if ((mask[i] | mask[j]) == (1LL << N) - 1) return true;
	return false;
}

int main()
{
//	freopen("D.in", "r", stdin);
	
	int cases;
	
	scanf("%d", &cases);
	for (int caseId = 0; caseId < cases; ++caseId)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			double x, y, r;
			scanf("%lf%lf%lf", &x, &y, &r);
			circles[i] = (circle_t) {point_t(x, y), r};
		}

		double l = 0, r = 4000.0;
		for (int i = 0; i < N; ++i) l = max(l, circles[i].r);
		for (; l + 0.0000001 < r;)
		{
			double m = (l + r) / 2.0;
			if (can(m)) r = m; else l = m;
		}

		printf("Case #%d: %lf\n", caseId + 1, (l + r) / 2.0);
	}
		
	return 0;	
}
