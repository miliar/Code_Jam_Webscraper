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

const int _my[] = {-1, 0, 0, 1};
const int _mx[] = {0, -1, 1, 0};

#define within(y, x) ( 0 <= (y) && (y) < R && 0 <= (x) && (x) < C )

int a[200][200];
char m[200][200];
int R, C;
char COL;

void read(ifstream &fin)
{
 int i, j;

 fin >> R >> C;

 fr(i, R) fr(j, C)
  fin >> a[i][j];
}

char color(int r, int c, char col)
{
 int i;

 while(true)
 {
  if(m[r][c]) return m[r][c];

  m[r][c] = col;

  int mn = a[r][c], n = -1;

  fr(i, 4)
  {
   int rr = r + _my[i];
   int cc = c + _mx[i];

   if(within(rr, cc) && mn > a[rr][cc])
    mn = a[rr][cc], n = i;
  }

  if(n == -1)
  {
   if(col)
    return col;
   else
    return COL++;
  }

  r += _my[n];
  c += _mx[n];
 }

 return COL;
}

void proc(ofstream &fout)
{
 int i, j;

 COL = 'a';
 _cl(m);

 fr(i, R) fr(j, C)
  color(i, j, color(i, j, 0));

 fr(i, R)
 {
  fr(j, C)
   fout << m[i][j] << ' ';
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
  fout << "Case #" << i + 1 << ":" << endl;
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
