#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	int T;
	cin >> T;
  int d[10000],l[10000],mx[10000];
	for(int c=1;c<=T;c++) {
    int N,D;
    cin >> N;
    for(int i=0;i<N;i++) {
      cin >> d[i] >> l[i];

      mx[i] = 0;
    }
    cin >> D;
    if(l[0]<d[0]) {
      cout << "Case #" << c << ": " << "NO"  << endl;
      continue;
    }
    mx[0] = d[0]+min(d[0],l[0]);
    if(mx[0]>=D) {
      cout << "Case #" << c << ": " << "YES"  << endl;
      continue;
    }
    int st=1;
    bool flag=false;
    for(int i=0;!flag && i<N;i++) {
      int j=st;
      while(!flag && j<N && d[j]<=mx[i]) {
        mx[j] = d[j]+min(d[j]-d[i],l[j]);
        if(mx[j] >= D) {
          cout << "Case #" << c << ": " << "YES"  << endl;
          flag=true;
        }
        st=++j;
      }
    }
    if(!flag)
      cout << "Case #" << c << ": " << "NO"  << endl;
	}
	return 0;
}
