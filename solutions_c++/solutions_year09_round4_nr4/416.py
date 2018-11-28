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

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define fr2(i, s, n) for(i = (s); i < (n); i++)
#define _sq(x) ((x)*(x))
typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

double x[5], y[5], r[5];
int C;

void read(ifstream &fin)
{
 int i;

 fin >> C;

 fr(i, C)
  fin >> x[i] >> y[i] >> r[i];
}

double dis(int i, int j)
{
 return (sqrt(_sq(x[i] - x[j]) + _sq(y[i] - y[j])) + r[i] + r[j]) / 2.0;
}

void proc(ofstream &fout)
{
  double ans = 1e10;
 if(C == 1)
  ans = r[0];
 else if(C == 2)
  ans = max(r[0], r[1]);
 else
 {

  ans = min(ans, max(dis(0, 1), r[2]));
  ans = min(ans, max(dis(1, 2), r[0]));
  ans = min(ans, max(dis(2, 0), r[1]));
 }

 fout << setiosflags(ios::fixed) << setprecision(7) << ans << endl;
}

int main()
{
 int i;
 int NT;

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
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
