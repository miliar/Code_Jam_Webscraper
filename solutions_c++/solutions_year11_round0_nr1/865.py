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
int O, B;
int op[1000], bp[1000];
int on[1000], bn[1000];

void read(ifstream &fin)
{
 char ch;

 O = 0, B = 0;

 fin >> N;
 frr(i, N) {
  fin >> ch;
  if(ch == 'O') {
   fin >> op[O];
   on[O] = i;
   ++O;
  } else {
   fin >> bp[B];
   bn[B] = i;
   ++B;
  }
 }
}

void proc(ofstream &fout)
{
 int i = 0, j = 0;
 int to = 0, tb = 0;
 int po = 1, pb = 1;

 for(int n = 0; i < O || j < B; ++n) {
  if(i < O && on[i] == n) {
   to += abs(po - op[i]) + 1;
   to = max(to, tb  + 1);
   po = op[i];
   ++i;
  } else {
   tb += abs(pb - bp[j]) + 1;
   tb = max(tb, to + 1);
   pb = bp[j];
   ++j;
  }
 }

 fout << max(to, tb) << endl;
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
