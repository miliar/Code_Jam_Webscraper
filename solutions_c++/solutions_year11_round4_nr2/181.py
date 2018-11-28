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

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

int R, C, D;
int a[1000][1000];
int sum_col[1000][1000], sum_row[1000][1000];
int mul_col[1000][1000], mul_row[1000][1000];
int weight[1000][1000];
int ans;

void read(ifstream &fin)
{
 fin >> R >> C >> D;
 frr(i, R) {
  string s;
  fin >> s;
  frr(j, C)
   a[i][j] = s[j];
 }
}

int getSumRow(int r, int c1, int c2) {
 int s1 = c1 < 0 ? 0 : sum_row[r][c1];
 int s2 = c2 < 0 ? 0 : sum_row[r][c2];
 return s2 - s1;
}

int getSumCol(int c, int r1, int r2) {
 int s1 = r1 < 0 ? 0 : sum_col[c][r1];
 int s2 = r2 < 0 ? 0 : sum_col[c][r2];
 return s2 - s1;
}

int getMulRow(int r, int c1, int c2) {
 int s1 = c1 < 0 ? 0 : mul_row[r][c1];
 int s2 = c2 < 0 ? 0 : mul_row[r][c2];
 return s2 - s1;
}

int getMulCol(int c, int r1, int r2) {
 int s1 = r1 < 0 ? 0 : mul_col[c][r1];
 int s2 = r2 < 0 ? 0 : mul_col[c][r2];
 return s2 - s1;
}

int getWeight(int r, int c) {
 if(r < 0 || c < 0) return 0;
 return weight[r][c];
}

void cal(int r, int c) {
 int mx = 0, my = 0;
 for(int k = 2; ; ++k) {
  if(r + k >= R || c + k >= C) break;
  mx += a[r + k - 1][c] // BL
      + (2 * k - 1) * a[r + k - 1][c + k - 1] // BR
      + (2 * k - 1) * a[r][c + k - 1] // TR
      + (2 * k + 1) * getSumCol(c + k, r, r + k - 1) // RIGHT
      + getMulRow(r + k, c, c + k - 1) - getSumRow(r + k, c, c + k - 1) * (2 * c);

  my += a[r][c + k - 1] // TR
      + (2 * k - 1) * a[r + k - 1][c + k - 1] // BR
      + (2 * k - 1) * a[r + k - 1][c] // BL
      + (2 * k + 1) * getSumRow(r + k, c, c + k - 1) // BOTTOM 
      + getMulCol(c + k, r, r + k - 1) - getSumCol(c + k, r, r + k - 1) * (2 * r);
      
  int tot_weight = getWeight(r + k, c + k) 
                 - getWeight(r - 1, c + k)
                 - getWeight(r + k, c - 1)
                 + getWeight(r - 1, c - 1)
                 - a[r][c] - a[r][c + k] - a[r + k][c] - a[r + k][c + k];

  if(mx == tot_weight * (k + 1) && my == tot_weight * (k + 1))
   ans = max(ans, k + 1);
 }
}

void proc(ofstream &fout)
{
 frr(r, R) {
  frr(c, C) {
   sum_row[r][c] = (c == 0 ? 0 : sum_row[r][c-1]) + a[r][c];
   mul_row[r][c] = (c == 0 ? 0 : mul_row[r][c-1]) + a[r][c] * (2 * c + 1); 
  }
 }

 frr(c, C) {
  frr(r, R) {
   sum_col[c][r] = (r == 0 ? 0 : sum_col[c][r-1]) + a[r][c];
   mul_col[c][r] = (r == 0 ? 0 : mul_col[c][r-1]) + a[r][c] * (2 * r + 1);
  }
 }

 frr(r, R) frr(c, C) {
  weight[r][c] = getWeight(r - 1, c - 1)
               + getSumCol(c, -1, r - 1)
               + getSumRow(r, -1, c - 1)
               + a[r][c];
 }

 ans = 0;
 frr(r, R) frr(c, C)
  cal(r, c);

 if(ans >= 3)
  fout << ans << endl;
 else
  fout << "IMPOSSIBLE" << endl;
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
