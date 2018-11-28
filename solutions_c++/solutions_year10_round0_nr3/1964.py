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

int r , k , n , flag[1002];
long long arr[1002] , res[1002];

int main(){
      freopen("c_large.in" , "rt" , stdin);
      freopen("c_large.out" , "wt" , stdout);
      int tst , i , kase = 1 , cnt , queptr;
      scanf("%d" , &tst);
      while(tst--){
            scanf("%d%d%d" , &r , &k , &n);
            for(i = 0;i<n;i++) cin >> arr[i];
            long long ret = 0 , tmp;
            queptr = cnt = 0;
            memset(flag , -1 , sizeof(flag));
            while(cnt < r){

                  if(flag[queptr] != -1) {
                        break;
                  }
                  else flag[queptr] = cnt;

                  tmp = arr[queptr];
                  i = queptr+1;
                  while(i%n != queptr){
                        i %= n;
                        if(tmp+arr[i] <= k) tmp += arr[i];
                        else break;
                        i++;
                  }
                  ret += tmp;
                  queptr = i%n;
                  res[cnt] = tmp;
                  cnt++;
            }
            if(cnt < r){
                  long long sm = 0 , p , c = 0;
                  for(i = flag[queptr];i<cnt;i++ , c++) sm += res[i];
                  //cout << ret << '@' << cnt << '@' << c << '@' << sm << endl;
                  p = r-cnt;
                  ret += ((p/c)*sm);
                  //cout<< p<< '@' << ret << endl;
                  p %= c;
                  for(i = flag[queptr] , c = 0;c<p;i++ , c++)
                        ret += res[i];
            }
            cout << "Case #" << kase++ << ": " << ret << endl;
      }
	return 0;
}
