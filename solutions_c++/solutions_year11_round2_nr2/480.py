#include <stdio.h>

double stack[300][3];
int stop;

double min(double a, double b)
{
	if (a>b)
		return b;
	return a;
}

void push(double l, double r, double t)
{
	if (stop != 0 && stack[stop-1][1] > l) {
		double oldl = stack[stop-1][0];
		double oldr = stack[stop-1][1];
		double oldt = stack[stop-1][2];
		stop --;
		if (t > oldt) {
			double deltaT = t-oldt;
			double deltaD = oldr-l;
			if (deltaT >= deltaD) {
				push(oldl-deltaD, r, t);
			}
			else {
				push(oldl-deltaT-(deltaD-deltaT)/2.0, r+(deltaD-deltaT)/2.0, t+(deltaD-deltaT)/2.0);
			}
		}
		else if (t < oldt) {
			double deltaT = oldt-t;
			double deltaD = oldr-l;
			if (deltaT >= deltaD) {
				push(oldl, r+deltaD, oldt);
			}
			else {
				push(oldl-(deltaD-deltaT)/2.0, r+deltaT+(deltaD-deltaT)/2.0, oldt+(deltaD-deltaT)/2.0);
			}
		}
		else {
			double deltaD = oldr-l;
			push(oldl-deltaD/2.0, r+deltaD/2.0, t+deltaD/2.0);
		}
	}
	else if (stop != 0 && stack[stop-1][1] == l) {
		stack[stop-1][1] = r;
		if (t > stack[stop-1][2])
			stack[stop-1][2] = t;
		return;
	}
	else {
		stack[stop][0] = l;
		stack[stop][1] = r;
		stack[stop][2] = t;
		stop ++;
	}
}

int main()
{
	int N;
	double D;
	int C;
	scanf("%d", &N);
	for (int cases = 0; cases <N; cases ++) {
		scanf("%d%lf", &C, &D);
		stop = 0;
		for (int i = 0; i<C; i++) {
			double P, V;
			scanf("%lf%lf", &P, &V);
			int v = (int)V;
			if (v%2 == 0)
				push(P - v/2*D, P + v/2*D, v/2*D-D/2.0);
			else
				push(P-(v-1)/2*D-D/2.0, P+(v-1)/2*D+D/2.0, (v-1)/2*D);
		}
		double ans = 0.0;
		for (int i = 0; i<stop; i++) {
			if (ans < stack[i][2])
				ans = stack[i][2];
		}
		printf ("Case #%d: %.16f\n", cases+1, ans);
	}
	return 0;
}
