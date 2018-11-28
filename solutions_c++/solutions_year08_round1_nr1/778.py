#include <algorithm>
#include <functional>
#include <utility>
#include <iostream>
#include <cmath>
#include <numeric>
#include <complex>

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iomanip>
#include <sstream>

#include <cctype>
#include <cstring>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>

#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned char uchar;
typedef short int sint;
typedef unsigned short int usint;
typedef unsigned int uint;
typedef long long i64;
typedef unsigned long long ui64;
typedef double dbl;
typedef long double ldbl;

#define pb push_back
#define mp make_pair

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

const long double EPS = 1e-9;
const int iINF = INT_MAX;
const long double ldblINF = 1e100;


int main() {
  int T,n,i,j,result,tmp;
  vector<int> v1,v2;
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> T;
  for(i=0;i<T;i++) {
    cin >> n;
    v1.clear();v2.clear();
    result = 0;
    for(j=0;j<n;j++) {
      cin >> tmp;
      v1.pb(tmp);
    }
    for(j=0;j<n;j++) {
      cin >> tmp;
      v2.pb(tmp);
    }
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    for(j=0;j<v1.size();j++) {
      result += v1[j]*v2[v2.size()-j-1];
    }
    cout << "Case #"<<i+1<<": "<<result<<endl;
  }
  return 0;
}
