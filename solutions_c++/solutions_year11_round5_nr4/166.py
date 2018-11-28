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

string S;

void read(ifstream &fin)
{
 fin >> S;
}

bool check(ll n) {
 ll s = (ll)sqrt((long double)n);
 while(s * s <= n) {
  if(s * s == n)
   return true;
  s++;
 }

 return false;
}

void print(long long n) {
 frr(i, sz(S)) {
  if(S[i] == '?') {
   if(n & (1LL << i))
    S[i] = '1';
   else
    S[i] = '0';
  }
 }

 reverse(all(S));
}

void proc(ofstream &fout)
{
 ll m = 0, n = 0;

 reverse(all(S));

 frr(i, sz(S)) {
  if(S[i] == '?')
   m |= 1LL << i;
  else if(S[i] == '1')
   n |= 1LL << i;
 }

 if(check(n)) {
  print(n);
  fout << S << endl;
  return;
 }

 for(ll i = m; i > 0; i = (i - 1) & m) {
  if(check(n | i)) {
   print(n | i);
   fout << S << endl;
   return;
  }
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
