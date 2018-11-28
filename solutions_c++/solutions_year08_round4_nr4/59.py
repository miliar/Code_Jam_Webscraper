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

int K, N;
string S;
int dp[20][1 << 17][20];
int cnt[20][20];
int rcnt[20][20];

void read(ifstream &fin)
{
 fin >> K;
 fin >> S;
 N = sz(S);
}

void proc(ofstream &fout)
{
 _cl(dp);
 _cl(cnt);
 _cl(rcnt);

 int x, y;
 fr(x, K) fr(y, K)
 {
  for(int i = 0; i + K <= N; i+= K)
   if(S[i + x] == S[i + y])
    cnt[x][y]++;

  for(int i = 0; i + 2 * K <= N; i += K)
   if(S[i + y] == S[i + K + x])
    rcnt[x][y]++;
 }

 int C = 1 << K;

 int m, p, n, f;
 fr(m, C)
  fr(f, K) if(((1 << f) & m) == 0)
   fr(p, K)
    if((m + (1 << f) + 1 == C || p != f) && ((1 << p) & m) == 0)
     fr(n, K) if((1 << n) & m)
     {
      if(m - (1 << n) == 0)
       dp[f][m][p] = max(dp[f][m][p], cnt[p][n] + rcnt[f][n]);
      else
       dp[f][m][p] = max(dp[f][m][p], dp[f][m - (1 << n)][n] + cnt[p][n]);
     }

 int res = 0;
 fr(p, K)
  res = max(res, dp[p][C - 1 - (1 << p)][p]);

 fout << (N - res) << endl;
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
