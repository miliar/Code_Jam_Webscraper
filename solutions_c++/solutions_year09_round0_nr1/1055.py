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

bool v[50][50];
int L, D, N;
string a[5500];

void gen(string s)
{
 int n = 0, i;

 fr(i, sz(s))
 {
  if(s[i] == '(')
   while(s[++i] != ')')
    v[n][s[i] - 'a'] = true;
  else
   v[n][s[i] - 'a'] = true;

  n++;
 }
}

int main()
{
 int i, j, k;
 string s;

 ifstream fin("input.txt");
 ofstream fout("output.txt");

 fin >> L >> D >> N;

 fr(i, D)
  fin >> a[i];

 fr(i, N)
 {
  fin >> s;
  _cl(v);
  gen(s);
  
  int c = 0;
  fr(j, D)
  {
   fr(k, L)
    if(!v[k][a[j][k] - 'a'])
     break;

   if(k == L) c++;
  }

  fout << "Case #" << i + 1 << ": " << c << endl;
 }

 return 0;
}
