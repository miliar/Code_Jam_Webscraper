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

template<typename T>
inline int nread(vector<T> &a)
{
	int n;
	cin >> n;
	a.clear();
	a.resize(n);
	for (int i=0;i<n;i++) cin >> a[i];
	return n;
}

#define TASKNAME "a"

int main () {
//	freopen(TASKNAME".in","r",stdin);
//	freopen(TASKNAME".out","w",stdout);
  int tst;
  cin >> tst;
  for (int ntst=0;ntst<tst;ntst++) {
    int n,s,p;
    cin >> n >> s >> p;
    int ok0=0, ok1=0,fl=0;
    for (int i=0;i<n;i++) {
      int t;
      cin >> t;
      if (t>=p+max(0,p-1)+max(0,p-1)) ok0++;
      else if (t>=p+max(0,p-2)+max(0,p-2)) ok1++;
      else fl++;
    }
    cout << "Case #" << ntst+1 << ": " << ok0 + min(ok1,s) << endl;
  }
}
