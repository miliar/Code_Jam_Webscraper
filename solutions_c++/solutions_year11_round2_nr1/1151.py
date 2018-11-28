#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iomanip>
#include <cstdio>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

#define MAXN 110

string games[MAXN];

int N;

int played[MAXN];
int won[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];

void read()
{
 cin >> N;
 frr (i, N)
  cin >> games[i];
}

void proc()
{
 _cl(played);
 _cl(won);

 frr (i, N) { 
  frr (j, N) {
   played[i] += (games[i][j] == '1' || games[i][j] == '0') ? 1 : 0;
   won[i] += (games[i][j] == '1') ? 1 : 0;
  }
 }

 frr (i, N) 
  wp[i] = won[i] / (double)played[i];

 frr (i, N) {
  vector<double> l;
  frr (j, N) {
   if (games[i][j] != '.') {
    l.pb((won[j]-(games[j][i]=='1'?1:0)) / ((double) (played[j]-1)));
   }
  }
  double tt = 0;
  frr (j, sz(l))
   tt += l[j];
  tt /= sz(l);
  owp[i] = tt;
 }

 frr (i, N) {
  double t=0;
  int cnt = 0;
  frr (j, N)
   if (games[i][j] != '.') {
    t += owp[j];
    cnt++;
   }
  t /= cnt;
  oowp[i] = t;
 }

 frr (i, N) {
  //cout << wp[i] << " " << owp[i] << " " <<  oowp[i] << " ";
  cout <<  (0.25*wp[i] + .5 * owp[i] + .25*oowp[i]) << endl;
 }
}

int main()
{
	int T;

	cin >> T;

	frr(i, T)
	{
		read();
  cout << "Case #" << (i+1) << ":" << endl;
		proc();
	}

	return 0;
}

