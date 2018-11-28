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

int N;
ll x[1000], y[1000];

void read(ifstream &fin)
{
 int i;

 fin >> N;

 fr(i, N)
  fin >> x[i];

 fr(i, N)
  fin >> y[i];
}

void proc(ofstream &fout)
{
 ll tot = 0;
 int i;

 sort(x, x + N);
 sort(y, y + N);
 reverse(y, y + N);

 fr(i, N)
  tot += x[i] * y[i];

 fout << tot << endl;
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
