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

const int MAX = 10100;

int N;
int v[MAX];
int a[MAX];
int m[MAX];

void read(ifstream &fin)
{
 fin >> N;
 frr(i, N)
  fin >> a[i];
}

void proc(ofstream &fout)
{
 _cl(v);

 if(N == 0) {
  fout << 0 << endl;
  return;
 }

 frr(i, N)
  v[a[i]]++;

 int E = 0, S = 0;
 int res = 1 << 30;

 frr(i, MAX) {
  if(v[i] < v[i + 1]) {
   frr(j, v[i + 1] - v[i]) {
    m[E] = i + 1;
    ++E;
   }
  } else if(v[i] > v[i + 1]) {
   frr(j, v[i] - v[i + 1]) {
    res = min(res, i + 1 - m[S]);
    S++;
   }
  }
 }

 fout << res << endl;
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
