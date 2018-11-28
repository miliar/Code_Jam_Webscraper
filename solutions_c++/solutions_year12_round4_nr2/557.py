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

const int inf = 1 << 28;

int N, W, H;
PII a[1100];
int posx[1100], posy[1100];

void read(ifstream &fin) {
 fin >> N >> W >> H;
 frr(i, N) {
  fin >> a[i].first;
  a[i].second = i;
 }

 sort(a, a + N);
}

void place(int x, int y, int w, int h,
  bool north, bool south, bool east, bool west) {
 int hl = h;
 if(north && south)
  hl = inf;
 if(north ^ south)
  hl = 2 * h;

 int wl = w;
 if(east && west)
  wl = inf;
 if(east ^ west)
  wl = 2 * w;

 int m = min(wl, hl);
 int i;
 
 for(i = 0; i < N && a[i].first * 2 <= m; ++i);
 if(i == 0) return;

 --i;
 int r = a[i].first;
 int n = a[i].second;

 posx[n] = x;
 int xr = r;
 if(!east) {
  posx[n] += r;
  xr += r;
 }
 posy[n] = y;
 int yr = r;
 if(!north) {
  posy[n] += r;
  yr += r;
 }

 a[i] = a[N - 1];
 --N;
 sort(a, a + N);

 if(w - xr < h - yr) {
  place(x, y + yr, w, h - yr,
    false, south, east, west);
  place(x + xr, y, w - xr, yr,
    north, false, false, west);
 } else {
  place(x + xr, y, w - xr, h,
    north, south, false, west);
  place(x, y + yr, xr, h - yr,
    false, south, east, false);
 }
}

void proc(ofstream &fout) {
 int M = N;
 place(0, 0, W, H, true, true, true, true);
 
 frr(i, M) {
  fout << posx[i] << " " << posy[i] << " ";
 }
 fout << endl;
 if(N != 0)
 cout << "SHIIIIIIIIIIIIIIIIIIT" << endl;
}

int main() {
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
