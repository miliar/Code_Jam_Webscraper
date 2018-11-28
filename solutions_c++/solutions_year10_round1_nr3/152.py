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

int A1, A2, B1, B2;

void read(ifstream &fin)
{
 fin >> A1 >> A2 >> B1 >> B2;
}

int cal(int a, int b)
{
 int l = 0;

 while(a > 0 && b / a == 1) {
  ++l;
  int t = a;
  a = b - a;
  b = t;
 }

 if(l % 2 == 0)
  return 1;
 else
  return 0;
}

void proc(ofstream &fout)
{
 int r = 0;

 for(int a = A1; a <= A2; ++a)
  for(int b = B1; b <= B2; ++b)
   r += cal(min(a, b), max(a, b));

 fout << r << endl;
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
