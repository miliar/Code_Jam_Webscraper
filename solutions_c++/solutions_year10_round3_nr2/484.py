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

int a,b,c;

int main() {

  int T; scanf("%d",&T); for(int t=1;t<=T;t++){

    printf("Case #%d: ",t);

    scanf("%d %d %d",&a,&b,&c);

    int r=-1;
    while(a<b){
      a*=c;
      r++;
    }

    int res=0;
    while(r!=0){
      r>>=1;
      res++;
    }

    printf("%d\n",res);

  }
}
