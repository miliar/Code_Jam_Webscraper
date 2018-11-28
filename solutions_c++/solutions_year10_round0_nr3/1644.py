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
    long long ans=0;
    int R, k, N;
    int a[1001], b[1001], c[1001];
    scanf("%d%d%d",&R,&k,&N);
    for(int j=0;j<N;j++)
      scanf("%d",&a[j]);
    memset(b,-1,sizeof(b));
    memset(c,-1,sizeof(c));
    int idx=0;
    int test=0;
    for(int j=0;j<R;j++){
      int sum=0;
      int cnt=0;
      if(b[idx]==-1){
	test++;
	int tmp=idx;
	while(cnt<N&&sum+a[idx]<=k){
	  cnt++;
	  ans+=a[idx];
	  sum+=a[idx];
	  if(idx==N-1)idx=0;
	  else idx++;
	}
	b[tmp]=idx;
	c[tmp]=sum;
      }
      else{
	ans+=c[idx];
	idx=b[idx];
      }
    }
    printf("Case #%d: %lld\n",i+1,ans);
  }
  return 0;
}
