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
bool a[2][100][100];
bool v[100];
int x[100];

void readset(ifstream &fin, int n, int t)
{
 int i;
 int x, y;

 fr(i, n - 1)
 {
  fin >> x >> y;

  x--, y--;
  a[t][x][y] = a[t][y][x] = true;
 }
}

void read(ifstream &fin)
{
 _cl(a);

 fin >> N;
 readset(fin, N, 1);

 fin >> M;
 readset(fin, M, 0);
}

bool check()
{
 int i, j;

 fr(i, M) fr(j, M)
  if(a[0][i][j] != a[1][x[i]][x[j]])
   return false;

 return true;
}

bool rec(int n)
{
 int i;

 if(n == M)
  return check();

 fr(i, N)
  if(!v[i])
  {
   x[n] = i;
   v[i] = true;
   if(rec(n + 1))
    return true;
   v[i] = false;
  }

 return false;
}

void proc(ofstream &fout)
{
 _cl(x);
 _cl(v);

 if(rec(0))
  fout << "YES" << endl;
 else
  fout << "NO" << endl;
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
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
