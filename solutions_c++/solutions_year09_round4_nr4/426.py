#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <math.h>
using namespace std;

#define all(V) (V).begin(),(V).end()
#define rall(V) (V).rbegin(),(V).rend()
#define _foreach(it, a, b) for (typeof(a) it = a; it != b; ++it)
#define foreach(x...) _foreach(x)
#define fu(a, b) foreach(a, 0, b)
#define MSET(a, b) memset(a, b, sizeof(a))
int cmp(double a, double b=0) {
  if (fabs(a-b) < 1.e-9)
    return 0;
  if (a < b)
    return -1;
  return 1;
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
	bool operator < (point q) const { return cmp(q) <  0; }
	
	friend ostream& operator <<(ostream& o, point p) {
		return o << "(" << p.x << ", " << p.y << ")";
	}
	
	static point pivot;
};

point point::pivot;

double abs(point p) { return hypot(p.x, p.y); }
double arg(point p) { return atan2(p.y, p.x); }

typedef vector<point> polygon;

ostream& operator <<(ostream& o, polygon T) {
	o << "polygon[";
	for (unsigned i = 0; i < T.size(); i++) {
		if (i) o << ", ";
		o << T[i];
	}
	return o << "]";
}

int ccw(point p, point q, point r) {
	return cmp((p - r) % (q - r));
}

double angle(point p, point q, point r) {
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

////////////////////////////////////////////////////////////////////////////////
// Comparação radial.
//

bool radial_lt(point p, point q) {
	point P = p - point::pivot, Q = q - point::pivot;
	double R = P % Q;
	if (cmp(R)) return R > 0;
	return cmp(P * P, Q * Q) < 0;
}

////////////////////////////////////////////////////////////////////////////////
// Determina o fecho convexo de um conjunto de pontos no plano.
//
// Destrói a lista de pontos T.
// 

polygon convex_hull(vector<point>& T) {
	int j = 0, k, n = T.size(); polygon U(n);

	point::pivot = *min_element(all(T));
	sort(all(T), radial_lt);
	for (k = n-2; k >= 0 && ccw(T[0], T[n-1], T[k]) == 0; k--);
	reverse((k+1) + all(T));

	for (int i = 0; i < n; i++) {
		// troque o >= por > para manter pontos colineares
		while (j > 1 && ccw(U[j-1], U[j-2], T[i]) >= 0) j--;
		U[j++] = T[i];
	}
	U.erase(j + all(U));
	return U;
}

////////////////////////////////////////////////////////////////////////////////
// Calcula a área orientada do polígono T.
//

double poly_area(polygon& T) {
	double s = 0; int n = T.size();
	for (int i = 0; i < n; i++)
		s += T[i] % T[(i+1) % n];
	return s / 2;
}

////////////////////////////////////////////////////////////////////////////////
// Encontra o ponto de interseção das retas pq e rs.
//

point line_intersect(point p, point q, point r, point s) {
	point a = q - p, b = s - r, c = point(p % q, r % s);
	return point(point(a.x, b.x) % c, point(a.y, b.y) % c) / (a % b);
}

////////////////////////////////////////////////////////////////////////////////
// Encontra o menor círculo que contém todos os pontos dados.
//

typedef pair<point, double> circle;

bool in_circle(circle C, circle p){
	return cmp(abs(p.first - C.first) + p.second, C.second) <= 0;
}
#define SQR(x) ((x)*(x))
point circumcenter(circle p, circle q, circle r) {
  double a = 2*(p.first.x - q.first.x);
  double b = 2*(p.first.y - q.first.y);
  double c = 2*(q.second - p.second);
  double d = (p.first*p.first - SQR(p.second)) - (q.first*q.first - SQR(q.second));

  double a2 = 2*(p.first.x - r.first.x);
  double b2 = 2*(p.first.y - r.first.y);
  double c2 = 2*(r.second - p.second);
  double d2 = (p.first*p.first - SQR(p.second)) - (r.first*r.first - SQR(r.second));
  double A = (SQR(-b2*c + b*c2) + SQR(a2*c - a*c2))/SQR(a*b2-a2*b) - 1;
  double B = (2*(b2*d-b*d2)*(-b2*c+b*c2) + 2*(-a2*d+a*d2)*(a2*c-a*c2))/SQR(a*b2 - a2*b) - (2*p.first.x*(-b2*c + b*c2) - 2*p.first.y*(a2*c - a*c2))/(a*b2-a2*b)-2*p.second;
  double C = (SQR(b2*d-b*d2) + SQR(-a2*d+a*d2))/SQR(a*b2-a2*b) - (2*p.first.x*(b2*d-b*d2) - 2*p.first.y*(-a2*d+a*d2))/(a*b2-a2*b) + p.first*p.first - p.second*p.second;
  double delta = sqrt(B*B-4*A*C);
  double R = (-B+delta)/(2*A);
  double x = (b2*d-b*d2-b2*c*R+b*c2*R)/(a*b2-b*a2);
  double y = (-a2*d+a*d2+a2*c*R-a*c2*R)/(a*b2-a2*b);
  return point(x, y);
}

circle circulo(circle p, circle q) {
  circle P = circle(point(), p.second);
  circle Q = circle(q.first-p.first, q.second);
  double theta = atan2(Q.first.y, Q.first.x);
  double co = cos(theta);
  double si = sin(theta);
  circle Q2 = circle(abs(P.first - Q.first), Q.second);
  double x1 = (-P.second + Q2.first.x + Q2.second)/2.;
  double y1 = 0.;
  double x2 = co*x1 + -si*y1 + p.first.x;
  double y2 = si*x1 + co*y1 + p.first.y;
  return circle(point(x2, y2), abs(point(x2,y2) - p.first) + p.second);
}

circle spanning_circle(vector<circle>& T) {
	int n = T.size();
	random_shuffle(all(T));
	circle C(point(), -INFINITY);
	for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
		C = T[i];
		for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
			C = circulo(T[i], T[j]);
			for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
				point o = circumcenter(T[i], T[j], T[k]);
				C = circle(o, abs(o - T[k].first) + T[k].second);
			}
		}
	}
	return C;
}

vector<circle> V;
int main() {
  int _42;
  scanf("%d", &_42);
  fu(_41, _42) {
    printf("Case #%d: ", _41+1);
    int N;
    scanf("%d", &N);
    V.clear();
    fu(i, N) {
      int X, Y, R;
      scanf("%d %d %d", &X, &Y, &R);
      V.push_back(circle(point(X, Y), R));
    }
    if (N == 1) {
      printf("%.6lf\n", V[0].second);
      continue;
    } else if (N == 2) {
      printf("%.6lf\n", max(V[0].second, V[1].second));
      continue;
    }
    double best = INFINITY;
    fu(i, N) {
      foreach(j, i+1, N) {
        foreach(k, j, N) {
          vector<circle> v1;
          v1.push_back(V[i]);
          v1.push_back(V[j]);
          v1.push_back(V[k]);
          circle c1 = spanning_circle(v1);
          vector<circle> v2;
          fu(p, N) if (!in_circle(c1, V[p]))
            v2.push_back(V[p]);
          circle c2 = spanning_circle(v2);
          best = min(best, max(c1.second, c2.second));
        }
      }
    }
    printf("%.6lf\n", best);
  }
  return 0;
}
