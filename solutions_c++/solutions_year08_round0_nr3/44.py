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

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define fr2(i, s, n) for(i = (s); i < (n); i++)
#define sq(x) ((x)*(x))
const double PI = 3.14159265358979323846;

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))
const double EPS = (1e-12);

int NT;
double f, R, t, r, g;

void read(ifstream &fin)
{
 fin >> f >> R >> t >> r >> g;
}

inline double add(double x, double y)
{
 double x1 = 0, x2 = 0, y1 = 0, y2 = 0;
 double ar;

 /* x1 */
 if(sq(x + g) + sq(y) <= sq(R))
 {
  x1 = g;
  y2 = max(0.0, min(sqrt(sq(R) - sq(x + g)) - y, g));
 }
 else
  x1 = max(0.0, min(sqrt(sq(R) - sq(y)) - x, g));

 /* y1 */
 if(sq(x) + sq(y + g) <= sq(R))
 {
  y1 = g;
  x2 = max(0.0, min(sqrt(sq(R) - sq(y + g)) - x, g));
 }
 else
  y1 = max(0.0, min(sqrt(sq(R) - sq(x)) - y, g));

 double sector = sqrt(sq(x2 - x1) + sq(y2 - y1));

 if(y1 + EPS > g && x1 + EPS > g)
 {
  ar = sq(g);
  ar -= (g - x2) * (g - y2) / 2;
 }
 else
  ar = (x1 + x2) * (y1 + y2) / 2;

 sector /= 2;
 double theta = asin(sector / R);
 ar += theta * sq(R);

 ar -= sqrt(sq(R) - sq(sector)) * sector; // * 2

 return ar;
}

double cal()
{
 double tot = PI * sq(R);
 double fly = 0;

 r += f;
 g -= 2 * f;
 R -= t + f;

 if(g <= 0)
  return 1;
 if(R <= 0)
  return 1;

 for(double x = r; x < R; x += g + 2 * r)
  for(double y = r; sq(x) + sq(y) < sq(R); y += g + 2 * r)
   fly += add(x, y);

 fly *= 4;

 return 1 - fly / tot;
}

void proc(ofstream &fout)
{
 fout << setiosflags(ios::fixed) << setprecision(6) << cal() << endl;
}

int main()
{
 int i;

 ifstream fin("input.txt");
 ofstream fout("output.txt");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ": ";
  proc(fout);
 }

 return 0;
}
