#include <stdio.h>
#include <math.h>

static void or_onto (unsigned char res[1024], const unsigned char src[1024])
{
	for (int i=0; i<1024; ++i)
		res[i] |= src[i];
}

#if 0
static double revfact[1024];
static double Pj[1024];

static void do_Pj ()
{
	// P(n)/n!. P(n)为n的错排数
	double res = 0.;
	double fac = 1.;
	for (int j=0; j<1024; ++j) {
		revfact[j] = fabs (fac);
		res += fac;
		Pj[j] = res;
		fac /= -(j + 1);
	}
}
#endif

static double f (unsigned n)
{
#if 0
	static double res[1024] = { 0., 0., 0. };
	static char mask[1024] = { 1, 1, 0, 0 };
	if (mask[n])
		return res[n];

	double s = 0;
	for (unsigned j=0; j<n; ++j)
		s += Pj[j] * revfact[n-j] * (f(j) + 1);
	s += Pj[n];
	s = s / (1 - Pj[n]);
	mask[n] = 1;
	res[n] = s;
	return s;
#else
	if (n < 2)
		return 0;
	return n;
#endif
}

static double work ()
{
	double res = 0;
	unsigned N;
	scanf ("%u", &N);

	unsigned value[1024];
	unsigned char handled[1024] = {0};
	for (unsigned j=0; j<N; ++j) {
		scanf ("%u", &value[j]);
		value[j]--;
	}
	for (unsigned j=0; j<N; ++j) {
		if (handled[j])
			continue;
		if (value[j] == j) {
			handled[j] = 1;
			continue;
		}
		unsigned char h[1024] = {0};
		unsigned cnt = 1;
		h[j] = 1;
		unsigned cur = value[j];
		while (cur != j) {
			++cnt;
			h[cur] = 1;
			cur = value[cur];
		}
		or_onto (handled, h);
		res += f(cnt);
	}
	return res;
}

int main ()
{
//	do_Pj ();
//	for (int j=0; j<1024; ++j)
//		printf ("f(%u) = %.20g\n", j, f(j));
	unsigned T;
	scanf ("%u", &T);
	for (unsigned j=1; j<=T; ++j) {
		printf ("Case #%u: %.6f\n", j, work());
	}
	return 0;
}
