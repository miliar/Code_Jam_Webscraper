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
#define _rng(x, a, b) ((a) <= (x) && (x) <= (b))

const string BIRD = "BIRD";
const string NBIRD = "NOT BIRD";
const string UNK = "UNKNOWN";

int N, M;
int h[1100];
int w[1100];
bool b[1100];

const int INF = 2100100;

void read(ifstream &fin)
{
 int i;
 string s;

 fin >> N;

 fr(i, N)
 {
  fin >> w[i] >> h[i] >> s;

  b[i] = s == BIRD;

  if(!b[i])
   fin >> s;
 }
}

void proc(ifstream &fin, ofstream &fout)
{
 int i, j;
 int W, H;

 int hbmin = INF, wbmin = INF;
 int hbmax = -1, wbmax = -1;

 int hnmin = INF, wnmin = INF;
 int hnmax = -1, wnmax = -1;

 fr(i, N) if(b[i])
 {
  wbmin = min(wbmin, w[i]);
  wbmax = max(wbmax, w[i]);

  hbmin = min(hbmin, h[i]);
  hbmax = max(hbmax, h[i]);
 }

 fr(i, N) if(!b[i])
 {
  if(_rng(w[i], wbmin, wbmax))
  {
   if(h[i] < hbmin)
    hnmax = max(h[i], hnmax);
   else
    hnmin = min(h[i], hnmin);
  }
  else if(_rng(h[i], hbmin, hbmax))
  {
   if(w[i] < wbmin)
    wnmax = max(w[i], wnmax);
   else
    wnmin = min(w[i], wnmin);
  }
 }

 fin >> M;

 fout << endl;

 fr(i, M)
 {
  fin >> W >> H;

  fr(j, N)
   if(w[j] == W && h[j] == H)
    break;

  if(j < N)
  {
   if(b[j])
    fout << BIRD << endl;
   else
    fout << NBIRD << endl;

   continue;
  }

  if(_rng(W, wbmin, wbmax) && _rng(H, hbmin, hbmax))
  {
   fout << BIRD << endl;
   continue;
  }

  if(W <= wnmax || W >= wnmin || H <= hnmax || H >= hnmin)
  {
   fout << NBIRD << endl;
   continue;
  }

  fout << UNK << endl;
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
  cout << "Case #" << i + 1 << endl;
  proc(fin, fout);
 }

 return 0;
}
