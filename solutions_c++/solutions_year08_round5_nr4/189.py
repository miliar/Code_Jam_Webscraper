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
typedef pair<int, int> PII;

const int MOD = 10007;

int R, C;
int N;
set<PII> s;
int dp[1000][1000];

void read(ifstream &fin)
{
 int i;
 int r, c;

 s.clear();

 fin >> R >> C;

 fin >> N;

 fr(i, N)
 {
  fin >> r >> c;

  s.insert(mp(r - 1, c - 1));
 }
}

int cal(int r, int c)
{
 if(r >= R || c >= C)
  return 0;

 int &res = dp[r][c];

 if(res != -1) return res;

 if(r == R - 1 && c == C - 1)
  res = 1;
 else if(s.count(mp(r, c)))
  res = 0;
 else
  res = cal(r + 2, c + 1) + cal(r + 1, c + 2);

 res %= MOD;

 return res;
}

void proc(ofstream &fout)
{
 _rs(dp);

 fout << cal(0, 0) << endl;
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
