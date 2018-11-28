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

int N, D, C;
string a;
char c[100][100];
bool d[100][100];
int v[100];

void read(ifstream &fin)
{
 _cl(c);
 _cl(d);
 string s;

 fin >> C;
 frr(i, C) {
  fin >> s;
  c[s[0] - 'A'][s[1] - 'A'] = s[2];
  c[s[1] - 'A'][s[0] - 'A'] = s[2];
 }

 fin >> D;
 frr(i, D) {
  fin >> s;
  d[s[0] - 'A'][s[1] - 'A'] = true;
  d[s[1] - 'A'][s[0] - 'A'] = true;
 }

 fin >> N;
 fin >> a;
}

void proc(ofstream &fout)
{
 _cl(v);

 stack<int> l;

 frr(i, sz(a)) {
  int n = a[i] - 'A';

  if(l.empty()) {
   l.push(n), v[n]++;
  } else if(c[l.top()][n]) {
   int nn = c[l.top()][n] - 'A';
   v[l.top()]--;
   v[nn]++;
   l.pop();
   l.push(nn);
  } else {
   frr(j, 26) if(v[j] && d[j][n]) {
    _cl(v);
    l = stack<int>();
    break;
   }

   if(!l.empty())
    l.push(n), v[n]++;
  }
 }

 VI res;
 while(!l.empty()) {
  res.pb(l.top());
  l.pop();
 }

 reverse(all(res));

 if(res.empty()) {
  fout << "[]" << endl;
 } else {
  fout << "[";
  frr(i, sz(res) - 1)
   fout << (char)(res[i] + 'A') << ", ";
  fout << (char)(res[sz(res) - 1] + 'A') << "]" << endl;
 }
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
