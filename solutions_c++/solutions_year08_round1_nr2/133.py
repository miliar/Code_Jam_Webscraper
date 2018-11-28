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

int N, M;
bool a[3000][3000];
int m[3000];
bool t[3000];
int c[3000];

void read(ifstream &fin)
{
 int i, j, x, y;
 int T;

 _cl(a);
 _rs(m);

 fin >> N;
 fin >> M;

 fr(i, M)
 {
  fin >> T;

  fr(j, T)
  {
   fin >> x >> y;
   x--;
   if(y)
    m[i] = x;
   else
    a[i][x] = true;
  }
 }
}

bool calc()
{
 int i, j;

 while(true)
 {
  fr(i, M)
   if(c[i] == 0 && (m[i] == -1 || !t[m[i]]))
   {
    if(m[i] == -1)
     return false;

    t[m[i]] = true;

    fr(j, M)
     if(a[j][m[i]])
      c[j]--;

    break;
   }

  if(i >= M)
   return true;
 }
}

void proc(ofstream &fout)
{
 int i, j;

 _cl(t);
 _cl(c);

 fr(i, M)
  fr(j, N)
   c[i] += a[i][j];

 if(!calc())
  fout << "IMPOSSIBLE" << endl;
 else
 {
  fr(i, N)
   fout << (t[i] ? '1' : '0') << ' ';

  fout << endl;
 }
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
  proc(fout);
 }

 return 0;
}
