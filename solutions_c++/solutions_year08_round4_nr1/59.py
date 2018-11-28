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

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

const bool AND = true;
const bool OR = false;
const int INF = 1000000;
const int MAX = 20100;

int N, V, G;
int dp[MAX][2];
bool g[MAX];
bool c[MAX];

void read(ifstream &fin)
{
 int i;

 fin >> N >> V;
 G = (N - 1) / 2;

 fr(i, G)
  fin >> g[i + 1] >> c[i + 1];

 for(; i < N; i++)
 {
  bool x;
  fin >> x;
  dp[i + 1][x] = 0;
  dp[i + 1][!x] = INF;
 }
}

int and(int r, int n1, int n2)
{
 int i, j;
 int v = INF;

 fr(i, 2) fr(j, 2) if((i & j) == r)
  v = min(v, dp[n1][i] + dp[n2][j]);

 return v;
}

int or(int r, int n1, int n2)
{
 int i, j;
 int v = INF;

 fr(i, 2) fr(j, 2) if((i | j) == r)
  v = min(v, dp[n1][i] + dp[n2][j]);

 return v;
}

void proc(ofstream &fout)
{
 for(int i = G; i > 0; i--)
  for(int r = 0; r <= 1; r++)
  {
   int x = and(r, i * 2, i * 2 + 1);
   int y = or(r, i * 2, i * 2 + 1);

   if(g[i] == AND)
    dp[i][r] = min(x, c[i] ? (y + 1) : INF);
   else
    dp[i][r] = min(c[i] ? (x + 1) : INF, y);
  }

 if(dp[1][V] >= INF)
  fout << "IMPOSSIBLE" << endl;
 else
  fout << dp[1][V] << endl;
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
