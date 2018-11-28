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
#define frr(i, n) for(int i = 0; i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

const int MP = 12;

const ll inf = 1LL << 50;

int N, P;
ll dp[MP][1 << MP][MP];
ll p[MP][1 << MP];
int miss[1 << MP];

void read(ifstream &fin)
{
 fin >> P;
 N = 1 << P;

 frr(i, N)
  fin >> miss[i];

 for(int i = P - 1; i >= 0; --i)
  for(int j = 0; j < (1 << i); ++j)
   fin >> p[i][j];
}

ll cal(int l, int n, int t)
{
 int m = 1 << (P - l);
 int s = m * n;

 ll &r = dp[l][n][t];
 if(r != -1)
  return r;

 for(int i = s; i < s + m; ++i)
  if(l - t > miss[i])
   return (r = inf);

 if(P == l)
  return (r = 0);

 r = min(inf,
   cal(l + 1, n * 2, t) + cal(l + 1, n * 2 + 1, t));

 r = min(r, p[l][n] + 
   cal(l + 1, n * 2, t + 1) + cal(l + 1, n * 2 + 1, t + 1));

 return r;
}

void proc(ofstream &fout)
{
 _rs(dp);

 fout << cal(0, 0, 0) << endl;
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
