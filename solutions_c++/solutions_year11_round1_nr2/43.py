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
typedef vector<PII> VPI;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

const int inf = 1 << 20;

int N, L, S;
string a[11000];
string lst[150];
string l;
int res, mcst;

void read(ifstream &fin)
{
 fin >> N >> L;
 frr(i, N)
  fin >> a[i];
 frr(i, L)
  fin >> lst[i];
}

void rec(VI &v, int k, int cst) {
 if(sz(v) <= 1) {
  if(sz(v) == 1 && (mcst < cst || (mcst == cst && res > v[0])))
   mcst = cst, res = v[0];
  return;
 }
 if(k >= 26) return;

 VPI s;
 bool found = false;
 frr(i, sz(v)) {
  int n = v[i];
  int m = 0;
  frr(j, S) {
   if(a[n][j] == l[k])
    m |= 1 << j;
  }

  if(m) found = true;
  s.pb(mp(m, n));
 }
 if(!found) {
  rec(v, k + 1, cst);
  return;
 }

 sort(all(s));

 VI t;
 int p = s[0].first;
 frr(i, sz(s)) {
  int n = s[i].second;
  if(p != s[i].first) {
   rec(t, k + 1, cst + (p ? 0 : 1));
   t.clear();
  }
  p = s[i].first;
  t.pb(n);
 }
 rec(t, k + 1, cst + (p ? 0 : 1));
}

void calc() {
 VPI s;

 frr(i, N)
  s.pb(mp(sz(a[i]), i));
 sort(all(s));

 VI t;
 int p = s[0].first;
 frr(i, N) {
  if(s[i].first != p) {
   S = p;
   rec(t, 0, 0);
   t.clear();
  }
  p = s[i].first;
  t.pb(s[i].second);
 }
 S = p;
 rec(t, 0, 0);
}

void proc(ofstream &fout)
{
 frr(i, L) {
  l = lst[i];
  mcst = 0, res = 0;
  calc();
  fout << a[res] << ' ';
 }

 fout << endl;
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
