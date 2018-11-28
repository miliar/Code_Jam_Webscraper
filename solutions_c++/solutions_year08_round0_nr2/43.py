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

const int INF = 1 << 20;

struct Trip { int s, e; bool side; };

int NT;
int T, N, NA, NB;
int TRIPS;
Trip a[500];
bool vtrip[500];
Trip t[500];
bool vtrain[500];
int res[2];

inline int readtime(string s)
{
 return ((s[0] - '0') * 10 + (s[1] - '0')) * 60
        + (s[3] - '0') * 10 + (s[4] - '0');
}

void readtrips(ifstream &fin, int n, bool side)
{
 int i;
 string s1, s2;

 fr(i, n)
 {
  fin >> s1 >> s2;
  a[N].s = readtime(s1);
  a[N].e = readtime(s2);
  a[N].side = side;
  N++;
 }
}

void read(ifstream &fin)
{
 fin >> T;
 fin >> NA >> NB;
 N = 0;
 readtrips(fin, NA, 0);
 readtrips(fin, NB, 1);
}

void proc(ofstream &fout)
{
 int i;

 _cl(vtrip);
 _cl(vtrain);
 _cl(res);
 TRIPS = 0;

 while(true)
 {
  int mn = INF, n = -1;

  fr(i, N) if(!vtrip[i] && mn > a[i].s)
   mn = a[i].s, n = i;

  if(n == -1)
   break;

  vtrip[n] = true;

  fr(i, TRIPS)
   if(!vtrain[i] && t[i].side == a[n].side && t[i].s <= a[n].s)
    break;

  if(i < TRIPS)
   vtrain[i] = true;
  else
   res[a[n].side]++;

  t[TRIPS].s = a[n].e + T;
  t[TRIPS].side = !a[n].side;
  TRIPS++;
 }

 fout << res[0] << " " << res[1] << endl;
}

int main()
{
 int i;

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
