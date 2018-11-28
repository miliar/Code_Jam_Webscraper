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

int R, C, A;

void read(ifstream &fin)
{
 fin >> C >> R >> A;
 C++, R++;
}

void proc(ofstream &fout)
{
 int x1, x2, y1, y2;

 fr(x1, C) fr(x2, C)
  fr(y1, R) fr(y2, R)
   if(A == abs(x1 * y2 - x2 * y1))
   {
    fout << "0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
    return;
   }

 fout << "IMPOSSIBLE" << endl;
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
