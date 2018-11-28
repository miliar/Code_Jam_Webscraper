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

ll X, W, R;
double T;
int N;
pair<ll, ll> a[1100];

void read(ifstream &fin)
{
 ll e, s, w;

 fin >> X >> W >> R >> T >> N;

 frr(i, N) {
  fin >> s >> e >> w;
  a[i] = mp(w + W, e - s);
  X -= e - s;
 }

 R -= W;
 a[N] = mp(W, X);
 N++;
}

void proc(ofstream &fout)
{
 double ans = 0;

 sort(a, a + N);

 frr(i, N) {
  double d = (R + a[i].first) * T;
  if(d < a[i].second) {
   ans += T;
   T = 0;
   ans += double(a[i].second - d) / a[i].first;
  } else {
   ans += double(a[i].second) / (R + a[i].first);
   T -= double(a[i].second) / (R + a[i].first);
  }
 }

 cout << T << " " << ans << endl;
 fout << setiosflags(ios::fixed) << setprecision(7) << ans << endl;
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
