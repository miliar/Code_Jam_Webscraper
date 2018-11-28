#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <ctime>
#include <cmath>
#include <memory>
#include <cstring>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef set<int> SI;
typedef map<int,int> MII;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<LL> VL;
typedef vector<VL> VLL;
typedef set<LL> SL;
typedef map<LL,LL> MLL;
typedef pair<LL,LL> LLL;
typedef vector<LD> VD;
typedef vector<VD> VVD;

template<typename T>
inline T sqr(const T &a){return a*a;}

string itoa(int a) {
	string res;
	while (a>0) {
		res+=a%10+'0';
		a/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}

int testcounter=0;
ofstream ouf;

template <typename T>
void print(T s) {
	testcounter++;
	cout << "Case #" << testcounter << ": " << s << endl;
	ouf << "Case #" << testcounter << ": " << s << endl;
}

void precalc() {
}

VVI gr;
VI order, used;
void dfs(int x) {
  if (used[x]) return;
  used[x] = 1;
  for (int i=0;i<gr[x].size();i++) {
    dfs(gr[x][i]);
  }
  order.push_back(x);
}

void solve() {
  int n;
  cin >> n;
  gr.assign(n,VI());
  for (int i=0;i<n;i++) {
    int m;
    cin >> m;
    for (int j=0;j<m;j++) {
      int x;
      cin >> x;
      gr[i].push_back(x-1);
    }
  }
  used.assign(n,0);
  order.clear();
  for (int i=0;i<n;i++)
    if (!used[i])
      dfs(i);
  VVI dyn(n,VI(n,0));
  for (int i=0;i<n;i++) dyn[i][i]=1;
  assert(order.size()==n);
  for (int ii=0;ii<n;ii++) {
    int i = order[ii];
    for (int j=0;j<gr[i].size();j++) {
      for (int k=0;k<n;k++) {
        dyn[i][k]+=dyn[gr[i][j]][k];
        if (dyn[i][k]>1) {
          print("Yes");
          return;
        }
      }
    }
    //cerr << i;
    //for (int j=0;j<n;j++) cerr << ' ' << dyn[i][j];
    //cerr << endl;
  }
  print("No");
  return;
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("input.txt","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	ouf<< fixed << setprecision(20);
	for (int i=0;i<n;i++) solve();
}
