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

const int inf = 1 << 20;

int D, I, M, N;
int dp[300][300];
int a[300];
int mn, mx;

void read(ifstream &fin)
{
 fin >> D >> I >> M >> N;
 frr(i, N)
  fin >> a[i];
}

int cal(int n, int k) {
 int &r = dp[n + 1][k];

 if(r != -1)
  return r;

 r = D * (N - n - 1);

 if(n == N - 1)
  return (r = 0);

 for(int i = n + 1; i < N; ++i)
  for(int v = mn; v <= mx; ++v) {
   int d = abs(v - k);

   if(M > 0) {
    int ins = (d - 1) / M;
    if(d == 0)
     ins = 0;
    int c = D * (i - n - 1) + ins * I + abs(v - a[i]) + cal(i, v);
    r = min(r, c);
   } else if(v == k) {
    int c = D * (i - n - 1) + abs(v - a[i]) + cal(i, v);
    r = min(r, c);
   }
  }

 return r;
}

void proc(ofstream &fout)
{
 _rs(dp);

 int r = inf;

 mn = a[0], mx = a[0];

 frr(i, N)
  mn = min(mn, a[i]), mx = max(mx, a[i]);

 for(int v = 0; v <= 255; ++v) {
  r = min(r, cal(-1, v));
 }

 fout << r << endl;
}

int main()
{
 int i;
 int NT;

 ifstream fin("input.txt");
 ofstream fout("output2.txt");
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
