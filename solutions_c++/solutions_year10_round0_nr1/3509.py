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

int main() {

  int T; scanf("%d",&T); for(int t=1;t<=T;t++){

    int n,k; scanf("%d %d",&n,&k);

    int m=1<<n;
    int p=k%m;
    int q=p==m-1;

    printf("Case #%d: %s\n",t,(q==0)?"OFF":"ON");

  }
}
