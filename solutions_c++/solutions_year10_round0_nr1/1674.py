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

int main(){
  int t;
  scanf("%d",&t);
  for(int i=0;i<t;i++){
    long long n, k, x, y;
    scanf("%lld%lld",&n,&k);
    printf("Case #%d: ",i+1);
    x=(1<<n)-1;
    y=1<<n;
    if(x<=k&&k%y==x)puts("ON");
    else puts("OFF");
  }
  return 0;
}
