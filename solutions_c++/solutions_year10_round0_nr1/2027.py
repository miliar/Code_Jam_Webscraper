#include <vector>
#include <list>
#include <map>
#include <set>
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

int main(){
      freopen("a_large.in" , "rt" , stdin);
      freopen("a_large.out" , "wt" , stdout);
      int tst , kase = 1 , n , k;
      scanf("%d" , &tst);
      while(tst--){
            scanf("%d%d" , &n , &k);
            int ret = (1<<n);
            k++;
            if(k % ret == 0) cout << "Case #" << kase++ << ": ON" << endl;
            else cout << "Case #" << kase++ << ": OFF" << endl;
      }
	return 0;
}
