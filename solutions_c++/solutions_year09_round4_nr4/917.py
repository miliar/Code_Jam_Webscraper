
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define fori(i,n) for(int i = 0; i < (n); i++)
#define forr(i,a,b) for(int i = (a); i <= (b); i++)

#define EPS 1e-8
#define PI 3.1415926535897932

typedef struct _point {
	double x, y, r;

	_point(double px = 0, double py = 0) {
		x = px;
		y = py;
	}

	_point operator +(_point q) {
		return _point(x+q.x, y+q.y);
	}

	double operator *(_point q) {
		return x*q.x + y*q.y;
	}
	double operator %(_point q) {
		return x*q.y - y*q.x;
	}

	_point operator -(_point q) {
		return _point(x-q.x, y-q.y);
	}
	
	_point operator /(double q) {
		return _point(x/q, y/q);
	}
	_point operator *(double q) {
		return _point(x*q, y*q);
	}
} point;

typedef struct _circle {
	point center;
	double R;
	
	_circle(point c = _point(), double r = 0) {
		center = c;
		R = r;
	}
} circle;

point circumcenter(point p, point q, point r) {
	point a = p - r,
		  b = q - r,
		  c = point(a * (p + r) / 2, b * (q + r) / 2);

	return point(c % point(a.y, b.y), point(a.x, b.x) % c) / (a % b);
}

double abs(point p) {
 return hypot(p.x, p.y);
}

bool in_circle(circle C, point p) {
	double dist = (p.x-C.center.x)*(p.x-C.center.x) + (p.y-C.center.y)*(p.y-C.center.y);
	if( C.R > p.r) return (dist < (C.R-p.r)*(C.R-p.r)+EPS);
	else return false;
}

circle spanning_circle(vector<point>& T) {
	circle C;
	int n = T.size();
	for (int i = 0; i < n; i++) 
		if (!in_circle(C, T[i])) {
			C = circle(T[i], T[i].r);
			for (int j = 0; j < i; j++)
				if (!in_circle(C, T[j])) {
					C = circle((T[i] + T[j]) / 2, abs(T[i] - T[j]) / 2);
					point v = T[i]-T[j];
					double absv = abs(v);
					v = v / absv;
					C.center = C.center + v * (T[i].r *0.5);
					C.center = C.center - v * (T[j].r *0.5);
					C.R = C.R+T[i].r*0.5+T[j].r*0.5;

					for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
						point o = circumcenter(T[i], T[j], T[k]);
						C = circle(o, abs(o - T[k]));
						point vi, vj, vk;
						vi = T[i]-o; vi = vi / abs(vi);
						vj = T[j]-o; vj = vj / abs(vj);
						vk = T[k]-o; vk = vk / abs(vk);
						point newcenter = o + vi*T[i].r + vj*T[j].r + vk*T[k].r;
						C.center = newcenter;

						double newray = abs(newcenter-T[i]) + T[i].r;
						C.R = newray;
					}
			}
		}
	
	//cout << "spanning for points:" << endl;
	//fori(i,T.size()) {
//		cout << T[i].x << " " << T[i].y << " " << T[i].r << endl;
	//}
	//cout << "circle " << C.center.x << " " << C.center.y << " " << C.R << endl;
	return C;
}


circle mspn(vector<point> &T) {
	circle c;
	c = spanning_circle(T);
	return c;
}

circle msp1(point p1) {
	circle c;
	vector<point> ps;
	ps.push_back(p1);
	c = mspn(ps);
	return c;
}

circle msp2(point p1, point p2) {
	circle c;
	vector<point> ps;
	ps.push_back(p1);
	ps.push_back(p2);
	c = mspn(ps);
	return c;
}

circle msp3(point p1, point p2, point p3) {
	circle c;
	vector<point> ps;
	ps.push_back(p1);
	ps.push_back(p2);
	ps.push_back(p3);
	c = mspn(ps);
	return c;
}


int main() {
	int T, C;
	cout.precision(6);
	cout << fixed;
	cin >> T;
	for(C = 1; C <= T; C++) {
		int N;
		cin >> N;
		vector< point > points(N);
		fori(i,N) {
			int x, y, r;
			cin >> x >> y >> r;
			points[i].x = x;
			points[i].y = y;
			points[i].r = r;
			//cout << x << " " << y << " " << r << endl;
		}
		double min = 1.0e20;

		forr(i,0,N-1) {
				//cout << ">>>>>> C1" << endl;
				circle c = msp1(points[i]);
				vector<point> remain;
				fori(k,N) {
					if( k != i ) {
						point p = points[k];
						if( !in_circle(c, p) ) {
							remain.push_back(p);
						}
					}
				}
				//cout << ">>>>>> C2" << endl;
				circle c2 = mspn(remain);
				double r = max(c.R, c2.R);
				if( r < min ) min = r;
		}
			//cout << "########### TWO POINTS #############" << endl;
		forr(i,0,N-1) {
			forr(j,i+1,N-1) {
				//cout << ">>>>>> C1" << endl;
				circle c = msp2(points[i], points[j]);
				vector<point> remain;
				fori(k,N) {
					if( k != i && k != j ) {
						point p = points[k];
						if( !in_circle(c, p) ) {
							remain.push_back(p);
						}
					}
				}
				//cout << ">>>>>> C2" << endl;
				circle c2 = mspn(remain);
				double r = max(c.R, c2.R);
				if( r < min ) min = r;
			}
		}
		
		//cout << "############ THREE POINTS ##########" << endl;
		forr(i,0,N-1) {
			forr(j,i+1,N-1) {
				forr(l,j+1,N-1) {
				//cout << ">>>>>> C1" << endl;
					circle c = msp3(points[i], points[j], points[l]);
					vector<point> remain;
					fori(k,N) {
						if( k != i && k != j && k != l ) {
							point p = points[k];
							if( !in_circle(c, p) ) {
								remain.push_back(p);
							}
						}
					}
				//cout << ">>>>>> C2" << endl;
					circle c2 = mspn(remain);
					double r = max(c.R, c2.R);
					if( r < min ) min = r;
				}
			}
		}
		if( N == 1 ) min = points[0].r;

		cout << "Case #" << C << ": " << min << endl;
	
	}
}

	
