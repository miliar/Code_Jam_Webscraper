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

typedef pair<int,int> value_type;

int main(){
  int c;
  scanf("%d",&c);
  for(int i=0;i<c;i++){
    int k, b, n, t, x[100], y[100];
    int ans=0, cou=0;
    vector<value_type> v;
    scanf("%d%d%d%d",&n,&k,&b,&t);
    for(int j=0;j<n;j++)scanf("%d",&x[j]);
    for(int j=0;j<n;j++)scanf("%d",&y[j]);
    for(int j=0;j<n;j++)v.push_back(make_pair(x[j],y[j]));
    
    for(int j=n-1;j>=0;j--){
      if(v[j].first+v[j].second*t>=b){
	cou++;
	for(int loop=j+1;loop<n;loop++){
	  if(v[loop].first+v[loop].second*t<b){
	    ans++;
	  }
	}
	if(cou>=k)break;
      }
    }
    printf("Case #%d: ",i+1);
    if(cou<k)puts("IMPOSSIBLE");
    else printf("%d\n",ans);
  }
  return 0;
}
