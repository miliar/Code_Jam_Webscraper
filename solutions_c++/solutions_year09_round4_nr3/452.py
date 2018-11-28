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

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

vector<VI> v;
VI b;
int N, K;
int ans;

void read(ifstream &fin)
{
 int i, j;
 int x;

 fin >> N >> K;

 v.clear();

 fr(i, N)
 {
  VI t;

  fr(j, K)
  {
   fin >> x;
   t.pb(x);
  }

  v.pb(t);
 }
}

bool cut(VI &x, VI &y)
{
 int i;

 fr(i, K)
  if(x[i] >= y[i])
   return true;

 return false;
}

void rec(int n)
{
 int i;

 if(n == N)
 {
  ans = min(sz(b), ans);

  return;
 }

 if(sz(b) >= ans)
  return;

 fr(i, sz(b))
  if(!cut(v[b[i]], v[n]))
  {
   int t = b[i];
   b[i] = n;
   rec(n + 1);
   b[i] = t;
  }

 b.push_back(n);
 rec(n + 1);
 b.pop_back();
}

void proc(ofstream &fout)
{
 b.clear();

 sort(all(v));

 ans = 1 << 20;

 rec(0);

 fout << ans << endl;
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
