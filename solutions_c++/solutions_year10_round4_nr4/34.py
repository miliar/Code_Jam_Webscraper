#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

int main()
{
	int T;
	cin >> T;
	cout.precision(20);
	for (int I=0;I<T;I++){
		cout << "Case #" << I+1 << ":";
		int n,m;
		cin >> n >> m;
		double x1,y1,x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;
		double qx,qy;
		for (int i=0;i<m;i++){
			double S=0.0;
			cin >> qx >> qy;
			double px,py;
			double vx,vy;
			vx=((qx-x1)*(x2-x1)+(qy-y1)*(y2-y1))/(sqr(x2-x1)+sqr(y2-y1))*(x2-x1);
			vy=((qx-x1)*(x2-x1)+(qy-y1)*(y2-y1))/(sqr(x2-x1)+sqr(y2-y1))*(y2-y1);
			px=x1+vx-(qx-x1-vx);
			py=y1+vy-(qy-y1-vy);
			if ((px-x1)*(y2-y1)-(x2-x1)*(py-y1)<0.0){
				double w=px;
				px=qx;
				qx=w;
				w=py;
				py=qy;
				qy=w;
			}
			/*cerr << px << ' ' << py << endl << qx << ' ' << qy << endl;
			cerr << (px-x1)*(qy-y1)-(qx-x1)*(py-y1) << endl;
			cerr << (px-x1)*(qx-x1)+(qy-y1)*(py-y1) << endl;*/
			double a1=atan2((px-x1)*(qy-y1)-(qx-x1)*(py-y1),(px-x1)*(qx-x1)+(qy-y1)*(py-y1));if (a1<0.0)a1=a1+2.0*M_PI;
			double a2=atan2((px-x2)*(qy-y2)-(qx-x2)*(py-y2),(px-x2)*(qx-x2)+(qy-y2)*(py-y2));if (a2>0.0)a2=a2-2.0*M_PI;
			//cerr << atan2((px-x1)*(qy-y1)-(qx-x1)*(py-y1),(px-x1)*(qx-x1)+(qy-y1)*(py-y1)) << endl; return 0;
			S+=0.5*(sqr(qx-x1)+sqr(qy-y1))*a1-0.5*((px-x1)*(qy-y1)-(qx-x1)*(py-y1));
			S-=0.5*(sqr(qx-x2)+sqr(qy-y2))*a2-0.5*((px-x2)*(qy-y2)-(qx-x2)*(py-y2));
			cout << " " << S;
		}
		cout << endl;
		
	}
	return 0;
}
