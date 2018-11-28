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
#define frr(i, n) for(int i = 0; i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

int R;
const int M = 100;
bool a[M][M];

void read(ifstream &fin)
{
 int x1, x2, y1, y2;

 _cl(a);

 fin >> R;
 frr(r, R) {
  fin >> x1 >> y1 >> x2 >> y2;
  
  for(int x = x1; x <= x2; ++x)
   for(int y = y1; y <= y2; ++y)
    a[y - 1][x - 1] = true;
 }
}

bool empty() {
 frr(y, M) frr(x, M)
  if(a[y][x]) return false;

 return true;
}

void create() {
 for(int y = M - 1; y >= 1; --y)
  for(int x = M - 1; x >= 1; --x)
   if(a[y - 1][x] && a[y][x - 1])
    a[y][x] = true;
}

void die() {
 for(int y = M - 1; y >= 0; --y)
  for(int x = M - 1; x >= 0; --x)
   if((y == 0 || !a[y-1][x]) && (x == 0 || !a[y][x-1]))
    a[y][x] = false;

 for(int x = M - 1; x >= 0; --x)
  a[0][x] = false;
}

void proc(ofstream &fout)
{
 int d;

 for(d = 0; true; ++d) {
  if(empty())
   break;

  create();
  die();
 }

 fout << d << endl;
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
