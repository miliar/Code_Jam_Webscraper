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

string s;
string a = "welcome to code jam";
int dp[1000][100];
const int MOD = 10000;

void read(ifstream &fin)
{
 getline(fin, s);
}

int rec(int n, int l)
{
 if(l >= sz(a)) return 1;
 if(n >= sz(s)) return 0;
 
 int &r = dp[n][l];

 if(r >= 0) return r;

 r = rec(n + 1, l);

 if(s[n] == a[l])
  r += rec(n + 1, l + 1);

 r %= MOD;

 return r;
}

void proc(ofstream &fout)
{
 _rs(dp);

 fout << setw(4) << setfill('0') << rec(0, 0) << endl;
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
