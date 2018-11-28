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
  int c;

  scanf("%d",&c);
  for(int i=0;i<c;i++){
    int n, a[20000], b[20000];
    scanf("%d",&n);
    int ans=0;
    for(int j=0;j<n;j++)scanf("%d%d",&a[j],&b[j]);
    for(int j=0;j<n-1;j++){
      for(int k=j+1;k<n;k++){
	if(a[j]<a[k]&&b[j]>b[k])ans++;
	else if(a[j]>a[k]&&b[j]<b[k])ans++;
      }
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}
