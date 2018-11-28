#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

struct Point {
	double x;
	double y;
};

double dist(Point P, Point Q)
{
	return sqrt((Q.x-P.x)*(Q.x-P.x)+(Q.y-P.y)*(Q.y-P.y));
}

double getarea(Point P1, Point P2, Point Q)
{
	double d = dist(P1, P2);
	double R1 = dist(P1, Q);
	double R2 = dist(P2, Q);

	if(abs(R1+R2-d)<1e-12) // on the same line
		return 0;

	if(abs(R1+d-R2)<1e-12)
		return  6*asin(0.5)*R1*R1;

	if(abs(R2+d-R1)<1e-12)
		return  6*asin(0.5)*R2*R2;

	if(abs(d)<1e-12)
		return 6*asin(0.5)*R1*R1;

	if(abs(R1)<1e-12)
		return 0;

	if(abs(R2)<1e-12)
		return 0;

	double h, A1, A2, theta1, theta2, w1, w2, tmp;
	
	// deal with either theta1=90 degree or theta2=90 degree special case
	if(abs(R2*R2+d*d-R1*R1)<1e-12) {// theta2=90 
		theta1 = asin(R2/R1);
		A1 = theta1*R1*R1-d*R2;
		A2 = 3*asin(0.5)*R2*R2;
		return A1+A2;
	}
	if(abs(R1*R1+d*d-R2*R2)<1e-12) {// theta1=90 
		theta2 = asin(R1/R2);
		A2 = theta2*R2*R2-d*R1;
		A1 = 3*asin(0.5)*R1*R1;
		return A1+A2;
	}
	

	// deal with > 90 degree case
	if(R1*R1>d*d+R2*R2) {
		tmp = (R1*R1-(d*d+R2*R2))/(2*d);
		h = sqrt(R2*R2-tmp*tmp);
		theta1 = asin(h/R1);
		theta2 = asin(h/R2);
		w2 = tmp;
		w1 = d+tmp;
		A1 = theta1*R1*R1-w1*h;
		A2 = theta2*R2*R2-w2*h;
		A2 = 6*asin(0.5)*R2*R2-A2;
		return A1+A2;
	}

	if(R2*R2>d*d+R1*R1) {
		tmp = (R2*R2-(d*d+R1*R1))/(2*d);
		h = sqrt(R1*R1-tmp*tmp);
		theta1 = asin(h/R1);
		theta2 = asin(h/R2);
		w1 = tmp;
		w2 = d+tmp;
		A2 = theta2*R2*R2-w2*h;
		A1 = theta1*R1*R1-w1*h;
		A1 = 6*asin(0.5)*R1*R1-A1;
		return A1+A2;
	}

	// deal with both theta1 < 90 and theta2 < 90

	tmp = (d*d+R2*R2-R1*R1)/(2*d);
	h = sqrt(R2*R2-tmp*tmp);
	//h = sqrt((R1+R2-d)*(R1+R2+d)*(R1+d-R2)*(R2+d-R1))/(2*d);
    theta1 = asin(h/R1);
	theta2 = asin(h/R2);
	w1 = sqrt(R1*R1-h*h);
	w2 = sqrt(R2*R2-h*h);
	A1 = theta1*R1*R1-w1*h;
	A2 = theta2*R2*R2-w2*h;
	return A1+A2;

}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	freopen("D:\\tmp\\D-small.in","r",stdin);freopen("D:\\tmp\\D-small.out","w",stdout);
	//freopen("D:\\tmp\\B-large.in","r",stdin);freopen("D:\\tmp\\B-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N, M;
		cin >> N >> M;
		Point P1, P2, Q;
		double A;
		printf("Case #%d: ",caseId);
		cin >> P1.x >> P1.y;
		cin >> P2.x >> P2.y;
		for(int i=0; i<M; i++) {
			cin >> Q.x >> Q.y;
			A = getarea(P1, P2, Q);
			printf("%lf ", A);
		}
		printf("\n");
		fflush(stdout);
	}

	return 0;
}