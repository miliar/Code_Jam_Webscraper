#include <math.h>
#include <vector>
#include <iostream>

using namespace std;


#define INC 500
#define EPS (1e-10)
const double pi = acos(-1);
#define INF (1e100)


inline int cmp(double a, double b = 0){
  if(fabs(a-b)<=EPS) return 0;
  if(a<b) return -1;
  return 1;
}

struct point {
  double x,y;
  point(double x = 0, double y = 0): x(x), y(y) {}

  point operator +(point q){ return point(x + q.x, y + q.y); }
  point operator -(point q){ return point(x - q.x, y - q.y); }
  point operator *(double t){ return point(x * t, y * t); }
  point operator /(double t){ return point(x / t, y / t); }
  double operator *(point q){ return x * q.x + y * q.y; }
  double operator %(point q){ return x * q.y - y * q.x; }

  int cmp(point q) const {
    if (int t = ::cmp(x, q.x)) return t;
    return ::cmp(y, q.y);
  }
  bool operator ==(point q) const { return cmp(q) == 0; }
  bool operator !=(point q) const { return cmp(q) != 0; }
  bool operator < (point q) const { return cmp(q) < 0; }
};

typedef point vetor;

double norma(vetor v){ return hypot(v.x, v.y); }

vector<point> T,aux, aux2;



#define all(x) (x).begin(),(x).end()
typedef pair<point,double> circle;

bool in_circle(circle C, point p){
  return cmp(norma(p - C.first), C.second) <= 0;
}

bool in_circle2(circle C, int k){
  k *= INC;
  for (int i = 0; i < INC; i++,k++) {
    if (!in_circle(C,T[k])) return false;
  }
  return true;
}

point circumcenter(point p, point q, point r) {
  point a = p - r, b = q - r,
    c = point(a * (p + r) / 2, b * (q + r) / 2);

  return point(c % point(a.y, b.y),point(a.x, b.x) % c) / (a % b);
}

circle spanning_circle(vector<point>& T) {
  int n = T.size();
  //random_shuffle(all(T));

  circle C(point(), -INFINITY);
  for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
    C = circle(T[i], 0);
    for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
      C = circle((T[i] + T[j]) / 2, norma(T[i] - T[j]) / 2);
      for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
        point o = circumcenter(T[i], T[j], T[k]);
        C = circle(o, norma(o - T[k]));
      }
    }
  }

  return C;
}



void poe(vector<point> &v, int n) {
  n*=INC;
  for (int i = 0; i < INC; i++,n++) {
    v.push_back(T[n]);
  }
}

void tira(vector<point> &v) {
  for (int i = 0; i < INC; i++) v.pop_back();
}



int main() {
  int n;
 
  int k;
  scanf("%d",&k);
  for (int kk = 1; kk <= k; kk++) {
    scanf("%d",&n);
    printf("Case #%d: ",kk);
    double y,x,r;
    circle c,c2;
    T.clear();
    aux.clear();
    aux2.clear();
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf %lf",&x,&y,&r);
      double inc = 2.*pi/INC;
      double ang = 0;
      for (int ii = 0; ii < INC; ang+=inc,ii++) {
	double xx = 1.0*r*cos(ang) + x;
	double yy = 1.0*r*sin(ang) + y;
	T.push_back(point(xx,yy));
      }
    }
    double mini = INF;
    //tamanho 1
    for (int i = 0; i < n; i++) {
      poe(aux,i);
      c = spanning_circle(aux);
      for (int k = 0; k < n; k++) {
	if (!in_circle2(c,k)) poe(aux2,k);
      }
      c2 = spanning_circle(aux2);
      mini = min(mini,max(c.second,c2.second));
      aux2.clear();
      tira(aux);
    }
    //tamanho 2
    for (int i = 0; i < n; i++) {
      poe(aux,i);
      for (int j = i+1; j < n; j++) {
	poe(aux,j);
	c = spanning_circle(aux);
	for (int k = 0; k < n; k++) {
	  if (!in_circle2(c,k)) poe(aux2,k);
	}
	c2 = spanning_circle(aux2);
	mini = min(mini,max(c.second,c2.second));
	aux2.clear();
	tira(aux);
      }
      tira(aux);
    }
    
    //tamanho 3
    for (int i = 0; i < n; i++) {
      poe(aux,i);
      for (int j = i+1; j < n; j++) {
	poe(aux,j);
	for (int k = j+1; k < n; k++) {
	  poe(aux,k);
	  c = spanning_circle(aux);
	  for (int z = 0; z < n; z++) {
	    if (!in_circle2(c,z)) poe(aux2,z);
	  }
	  c2 = spanning_circle(aux2);
	  mini = min(mini,max(c.second,c2.second));
	  aux2.clear();
	  tira(aux);
	}

	tira(aux);
      }
      tira(aux);
    }
    printf("%.6lf\n",mini);
  }  
  return 0;
}
