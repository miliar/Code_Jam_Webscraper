#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <list>
#include <sstream>

using namespace std;

#define DEBUG true

#define f(i,j,k) for(int i = j; i < k; i++)
#define fd(i,j,k) for(int i = j; i >= k; i--)
#define pb push_back
#define sz size
#define vs vector<string>
#define vi vector<int>
#define deb(x...)  if(DEBUG) printf(x)

template <typename T>
void printv(vector<T>& v){
	int n = v.sz();
	printf("[");
	for(int i = 0; i < n; i++){
		cout << v[i] << ", ";
	}
	printf("]\n");
}

vs split(const string& s, const string delim){
	vs res;
	string at;
	int n = s.sz();

	for(int i = 0; i < n; i++){
		char c = s[i];
		if(delim.find(c) != string::npos){
			if(at.sz() > 0){
				res.pb(at);
			}
			at = "";
		} else {
			at.pb(c);
		}
	}
	if(at.sz() > 0){
		res.pb(at);
	}

	return res;
}

template <typename S, typename T>
T convert(const S var){
	T res;
	stringstream ss;
	ss << var;
	ss >> res;

	return res;

}

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define foreach(x...) _foreach(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;
_inline(int cmp)(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

template <class T>
struct index_lt {
	T& v;
	index_lt(T& v): v(v) {}
	_inline(bool operator ())(int i, int j) {
		return (v[i] != v[j]) ? (v[i] < v[j]) : (i < j);
	}
};
template <class T> index_lt<T> make_index_lt(T& v) { return index_lt<T>(v); }
bool cmp_eq(double x, double y) { return cmp(x, y) == 0; }
bool cmp_lt(double x, double y) { return cmp(x, y) < 0; }
int safe_gets(char*& s) { // depois de usar, free(s);
	return scanf("%a[^\r\n]%*[\r\n]", &s);
}


struct point {
	double x, y;
	point(double x = 0, double y = 0): x(x), y(y) {}
	point operator +(point q) { return point(x + q.x, y + q.y); }
	point operator -(point q) { return point(x - q.x, y - q.y); }
	point operator *(double t) { return point(x * t, y * t); }
	point operator /(double t) { return point(x / t, y / t); }
	double operator *(point q) { return x * q.x + y * q.y; }
	double operator %(point q) { return x * q.y - y * q.x; }
	int cmp(point q) const {
		if (int t = ::cmp(x, q.x)) return t;
		return ::cmp(y, q.y);
	}
	bool operator ==(point q) const { return cmp(q) == 0; }
	bool operator !=(point q) const { return cmp(q) != 0; }
	bool operator < (point q) const { return cmp(q) < 0; }
	friend ostream& operator <<(ostream& o, point p) {
		return o << "(" << p.x << ", " << p.y << ")";
	}
	static point pivot;
};
point point::pivot;
double abs(point p) { return hypot(p.x, p.y); }
double arg(point p) { return atan2(p.y, p.x); }
typedef vector<point> polygon;

_inline(int ccw)(point p, point q, point r) {
	return cmp((p - r) % (q - r));
}
_inline(double angle)(point p, point q, point r) {
	point u = p - q, v = r - q;
	return atan2(u % v, u * v);
}
////////////////////////////////////////////////////////////////////////////////
// Decide se q está sobre o segmento fechado pr.
//
bool between(point p, point q, point r) {
	return ccw(p, q, r) == 0 && cmp((p - q) * (r - q)) <= 0;
}
////////////////////////////////////////////////////////////////////////////////
// Decide se os segmentos fechados pq e rs têm pontos em comum.
//
bool seg_intersect(point p, point q, point r, point s) {
	point A = q - p, B = s - r, C = r - p, D = s - q;
	int a = cmp(A % C) + 2 * cmp(A % D);
	int b = cmp(B % C) + 2 * cmp(B % D);
	if (a == 3 || a == -3 || b == 3 || b == -3) return false;
	if (a || b || p == r || p == s || q == r || q == s) return true;
	int t = (p < r) + (p < s) + (q < r) + (q < s);
	return t != 0 && t != 4;
}
////////////////////////////////////////////////////////////////////////////////
// Calcula a distância do ponto r ao segmento pq.
//
double seg_distance(point p, point q, point r) {
	point A = r - q, B = r - p, C = q - p;
	double a = A * A, b = B * B, c = C * C;
	if (cmp(b, a + c) >= 0) return sqrt(a);
	else if (cmp(a, b + c) >= 0) return sqrt(b);
	else return fabs(A % B) / sqrt(c);
}
////////////////////////////////////////////////////////////////////////////////
// Classifica o ponto p em relação ao polígono T.
//
// Retorna 0, -1 ou 1 dependendo se p está no exterior, na fronteira
// ou no interior de T, respectivamente.
//
int in_poly(point p, polygon& T) {
	double a = 0; int N = T.size();
	for (int i = 0; i < N; i++) {
		if (between(T[i], p, T[(i+1) % N])) return -1;
		a += angle(T[i], p, T[(i+1) % N]);
	}
	return cmp(a) != 0;
}


typedef pair<point, double> circle;
bool in_circle(circle C, point p){
	return cmp(abs(p - C.first), C.second) <= 0;
}
point circumcenter(point p, point q, point r) {
	point a = p - r, b = q - r, c = point(a * (p + r) / 2, b * (q + r) / 2);
	return point(c % point(a.y, b.y), point(a.x, b.x) % c) / (a % b);
}
circle spanning_circle(vector<point>& T) {
	int n = T.size();
	random_shuffle(all(T));
	circle C(point(), -INFINITY);
	for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
		C = circle(T[i], 0);
		for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
			C = circle((T[i] + T[j]) / 2, abs(T[i] - T[j]) / 2);
			for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
				point o = circumcenter(T[i], T[j], T[k]);
				C = circle(o, abs(o - T[k]));
			}
		}
	}
	return C;
}

int main(void){
	int T;
	cin >> T;
	f(cas,1,T+1){
		int n;
		cin >> n;
		vector<circle> vc;
		double res = 1e200;
		f(i,0,n){
			double x,y,r;
			cin >> x >> y >> r;
			vc.pb(circle(point(x,y), r));
		}

		if(n==1){
			res = vc[0].second;
		} else if(n==2){
			res = max(vc[0].second, vc[1].second);
			double dist = abs(vc[0].first - vc[1].first) + vc[0].second + vc[1].second;
			res = min(res, dist/2);

		} else if(n==3){
			double dist01, dist02, dist12, distall;
			dist01 = (abs(vc[0].first - vc[1].first) + vc[0].second + vc[1].second)/2;
			dist02 = (abs(vc[0].first - vc[2].first) + vc[0].second + vc[2].second)/2;
			dist12 = (abs(vc[1].first - vc[2].first) + vc[1].second + vc[2].second)/2;
			vector<point> vpp;
			f(i,0,3) vpp.pb(vc[i].first);

			circle sc = spanning_circle(vpp);

			double sdist = 0;
			f(i,0,3){
				sdist = max(sdist, abs(vc[i].first - sc.first) + vc[i].second);
			}
			distall = sdist;

			res = min(res, max(dist01,vc[2].second));
			res = min(res, max(dist02,vc[1].second));
			res = min(res, max(dist12,vc[0].second));
			res = min(res, distall);


		} else {

			f(i,0,n) f(j,i+1,n) f(k,j+1,n){
				vector<point> vp;
				vp.pb(vc[i].first);
				vp.pb(vc[j].first);
				vp.pb(vc[k].first);
				circle c = spanning_circle(vp);
				vector<circle> in, out;
				f(p,0,n){
					if(in_circle(c,vc[p].first)){
						in.pb(vc[p]);
					} else {
						out.pb(vc[p]);
					}

				}

				double resin = 0, resout = 0;
				f(p,0,in.sz()){
					double d = in[p].second + abs(c.first - in[p].first)/2;
					resin = max(resin, d);
				}

				vector<point> outp;
				f(p,0,out.sz()) outp.pb(out[p].first);

				circle c_out = spanning_circle(outp);
				f(p,0,out.sz()){
					double d = out[p].second + abs(c.first - out[p].first)/2;
					resout = max(resout, d);
				}

				res = min(res, max(resin, resout));

			}
		}

		printf("Case #%d: %.7f\n",cas,res);

	}

	return 0;
}
