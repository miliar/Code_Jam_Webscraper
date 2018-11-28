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

int N;
int d[11000];
int len[11000];
bool f[11000][11000];

void read(ifstream &fin) {
 fin >> N;
 frr(i, N)
  fin >> d[i + 1] >> len[i + 1];
 N += 2;
 fin >> d[N - 1];
 len[N - 1] = 0;
 d[0] = 0, len[0] = d[1];
}

void proc(ofstream &fout) {
 for(int p = N - 1; p >= 0; --p)
  for(int n = p + 1; n < N; ++n) {
   if(len[p] + d[p] < d[n]) break;

   f[p][n] = false;
   if(n == N - 1) {
    f[p][n] = true;
    continue;
   }

   int l = min(d[n] - d[p], len[n]);
   for(int i = n + 1; i < N; ++i) {
    if(d[n] + l >= d[i]) {
     if(f[n][i]) {
      f[p][n] = true;
      break;
     }
    } else
     break;
   }
  }

 if(f[0][1])
  fout << "YES" << endl;
 else
  fout << "NO" << endl;
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
