#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

const double eps = 1e-12;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

int N[2];
int P;
int W, G;
vector<double> p;
double x[2][1000];
double y[2][1000];

double gety(int n, int m, double gx) {
 if(N[n] == m + 1)
  return y[n][m];

 return y[n][m] + (gx - x[n][m]) * (y[n][m+1] - y[n][m]) / (x[n][m+1] - x[n][m]);
}

double get_areax(int n0, int n1, double h, double xp, double area) {
 double m0 = (y[0][n0+1] - y[0][n0]) / (x[0][n0+1] - x[0][n0]);
 double m1 = (y[1][n1+1] - y[1][n1]) / (x[1][n1+1] - x[1][n1]);
 double m = m1 - m0;
 double k = h - m1 * x[1][n1] + m0 * x[0][n0] + y[1][n1] - y[0][n0];
 double a = m;
 double b = k - m * xp;
 double c = - area - k * xp;
 double d = sqrt(b * b - 4 * a * c);

 if(abs(a) < eps)
  return -c / b;

 double r1 = (-b - d) / (2 * a);
 double r2 = (-b + d) / (2 * a);

 if(r2 < r1)
  swap(r1, r2);

 if(r1 < xp) return r2;
 else return r1;
}

void read(ifstream &fin)
{
 p.clear();
 fin >> W >> N[0] >> N[1] >> G;
 frr(n, 2) {
  frr(i, N[n]) {
   fin >> x[n][i] >> y[n][i];
   p.pb(x[n][i]);
  }
 }
}

void proc(ofstream &fout)
{
 sort(all(p));
 P = sz(p);

 double prev = 0;
 double h = 0;
 int i0 = 0, i1 = 0;

 double area = 0;

 frr(i, P) {
  double y0 = gety(0, i0, p[i]);
  if(i0 + 1 < N[0] && p[i] == x[0][i0 + 1]) i0++;
  double y1 = gety(1, i1, p[i]);
  if(i1 + 1 < N[1] && p[i] == x[1][i1 + 1]) i1++;

  area += (h + y1 - y0) * (p[i] - prev);
  h = y1 - y0;
  prev = p[i];
 }

 double slice = area / G;

 h = 0, prev = 0;
 i0 = 0, i1 = 0;
 area = 0;
 frr(i, P) {
  double y0 = gety(0, i0, p[i]);
  double y1 = gety(1, i1, p[i]);

  double t = (h + y1 - y0) * (p[i] - prev);
  if(t + area >= slice) {
   double gx = get_areax(i0, i1, h, prev, slice - area);
   h = gety(1, i1, gx) - gety(0, i0, gx);
   fout << setiosflags(ios::fixed) << setprecision(7) << gx << endl;
   prev = gx;
   area = 0;

   G--;
   if(G == 1)
    break;
   --i;
   continue;
  }

  if(i0 + 1 < N[0] && p[i] == x[0][i0 + 1]) i0++;
  if(i1 + 1 < N[1] && p[i] == x[1][i1 + 1]) i1++;

  area += (h + y1 - y0) * (p[i] - prev);
  h = y1 - y0;
  prev = p[i];
 }
}

int main()
{
 int i;
 int NT;

 ifstream fin("in");
 ofstream fout("out");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ":" << endl;
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
