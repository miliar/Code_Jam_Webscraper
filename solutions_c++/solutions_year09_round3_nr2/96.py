#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	cout.precision(10);
	for (int t=1;t<=T;++t) {
		int N;
		cin >> N;
		double x1=0,x2=0,x3=0;
		double v1=0,v2=0,v3=0;
		for (int i=0;i<N;++i) {
			double xx1,xx2,xx3,vv1,vv2,vv3;
			cin >> xx1 >> xx2 >> xx3 >> vv1 >> vv2 >> vv3;
			x1+=xx1;
			x2+=xx2;
			x3+=xx3;
			v1+=vv1;
			v2+=vv2;
			v3+=vv3;
		}
		x1/=N;
		x2/=N;
		x3/=N;
		v1/=N;
		v2/=N;
		v3/=N;
		double xv = x1*v1+x2*v2+x3*v3;
		double vv = v1*v1+v2*v2+v3*v3;
		double lambda = -1;
		if (vv!=0) lambda = -xv/vv;
		double tt,d;
		if (lambda<0) {
			tt=0;
			d=sqrt(x1*x1+x2*x2+x3*x3);
		}
		else {
			tt=lambda;
			double u1,u2,u3;
			u1=x1+lambda*v1;
			u2=x2+lambda*v2;
			u3=x3+lambda*v3;
			d=sqrt(u1*u1+u2*u2+u3*u3);
		}
		cout << "Case #" << t << ": " << d << " " << tt << endl;
	}
}
