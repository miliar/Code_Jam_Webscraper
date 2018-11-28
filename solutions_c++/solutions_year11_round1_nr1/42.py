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

template<class T>
 inline T gcd(T m, T n) {  // n <= m
  return n == 0 ? m : gcd(n, m%n);
 }

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

ll N, PD, PG;

void read(ifstream &fin)
{
 fin >> N >> PD >> PG;
}

bool cal() {
 int g;

 if(PD == 100 || PD == 0)
  g = 100;
 else
  g = gcd(PD, 100ll);

 ll d = 100 / g;
 if(100 / g > N)
  return false;
 ll k = PD * g / 100;

 if(PG == 100) {
  if(PD != 100)
   return false;
 } else if(PG == 0) {
  if(PD != 0)
   return false;
 }

 ll g2 = gcd(PG, 100 - PG);
 ll c = abs(100 * k - d * PG);
 ll cg = gcd(g2, c);
 ll z = g2 / cg;
 if(z * d > N)
  return false;

 return true;
}

void proc(ofstream &fout)
{
 if(cal())
  fout << "Possible" << endl;
 else
  fout << "Broken" << endl;
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
  fout << "Case #" << i + 1 << ": ";
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
