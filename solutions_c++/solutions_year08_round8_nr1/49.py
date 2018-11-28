#include <cstdio>
#include <algorithm>
#include <cmath>
#define sqr(x) ((x)*(x))
const double PI = 2*acos(0.0);

using namespace std;

int NRT;

struct trg{
	double x1, x2, x3, y1, y2, y3;
	double getAngle(){
		if (x1 == x2) return PI/2;
		return atan( (y2-y1) / (x2-x1));
	}
	double getLength(){
		double dx = sqr(x1-x2);
		double dy = sqr(y1-y2);
		return sqrt(dx + dy);
	}
};

double randR(){
	long long r = (long long)rand()*RAND_MAX + rand();
	return r / ((double) RAND_MAX * RAND_MAX);
}

double randR2(){
	return (randR()-0.5) * 1e-4;
}

void solve(){
	printf("Case #%d: ", ++NRT);
	trg t1, t2;
	scanf("%lf %lf %lf %lf %lf %lf", &t1.x1, &t1.y1, &t1.x2, &t1.y2, &t1.x3, &t1.y3);
	scanf("%lf %lf %lf %lf %lf %lf", &t2.x1, &t2.y1, &t2.x2, &t2.y2, &t2.x3, &t2.y3);
	double u = t2.getAngle() - t1.getAngle();
	double rap = t2.getLength() / t1.getLength();
	const int ITER = 1000000;
	double best = 1e9;
	double solX, solY;
	double bestA, bestB, bestC;
	for (int i=0; i<ITER; i++){
		double a = randR(), b = randR(), c = randR();
		double sum = a+b+c;
		a /= sum;
		b /= sum;
		c /= sum;
		double px1 = t1.x1*a + t1.x2*b + t1.x3*c;
		double py1 = t1.y1*a + t1.y2*b + t1.y3*c;
		double px2 = t2.x1*a + t2.x2*b + t2.x3*c;
		double py2 = t2.y1*a + t2.y2*b + t2.y3*c;
		double dist = sqrt(sqr(px1-px2) + sqr(py1-py2));
		if (dist < best){
			best = dist;
			solX = (px1+px2)/2.0;
			solY = (py1+py2)/2.0;
			bestA = a;
			bestB = b;
			bestC = c;
		}
	}
	for (int step=1; step<5; step++){
		double rap = pow(0.005, step);
		for (int i=0; i<ITER; i++){
			double a = bestA + randR2()*rap, b = bestB + randR2()*rap, c = bestC + randR2()*rap;
			double sum = a+b+c;
			a /= sum;
			b /= sum;
			c /= sum;
			double px1 = t1.x1*a + t1.x2*b + t1.x3*c;
			double py1 = t1.y1*a + t1.y2*b + t1.y3*c;
			double px2 = t2.x1*a + t2.x2*b + t2.x3*c;
			double py2 = t2.y1*a + t2.y2*b + t2.y3*c;
			double dist = sqrt(sqr(px1-px2) + sqr(py1-py2));
			if (dist < best){
				best = dist;
				solX = (px1+px2)/2.0;
				solY = (py1+py2)/2.0;
				bestA = a;
				bestB = b;
				bestC = c;
			}
		}
	}
	fprintf(stderr, "%.10f", best);
	printf("%.8f %.8f\n", solX, solY);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
	int tst;
	scanf("%d", &tst);
	while (tst--)
		solve(), fprintf(stderr, "%d\n", tst);
    return 0;
}
