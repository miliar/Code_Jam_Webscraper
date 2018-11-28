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

int x[1000];
int y[1000];

int main() {

  int T; scanf("%d",&T); for(int t=1;t<=T;t++){

    printf("Case #%d: ",t);

    int n; scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%d %d",&x[i],&y[i]);

    int r=0;
    for(int i=0;i<n;i++)
      for(int j=i+1;j<n;j++)
	if(x[i]<x[j] && y[i]>y[j])
	  r++;
	else if(x[i]>x[j] && y[i]<y[j])
	  r++;

    printf("%d\n",r);

  }
}
