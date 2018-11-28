#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <climits>
#include <sstream>

using namespace std;

#define MAXN 100
typedef long long ll;
ll step[MAXN];
int tcase;

int main(){
    
   freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
  step[1]=1;
  for(int i=2;i<MAXN;++i) step[i] = 2*step[i-1]+1;
  //cerr<<step[30]<<endl;
  scanf("%d",&tcase);
  for(int i=1;i<=tcase;++i){
    int n,d;  scanf("%d%d",&n,&d);
    string ans;
    if(d-step[n]>=0 && (d-step[n])%(step[n]+1)==0) ans = "ON";
    else ans = "OFF";
    printf("Case #%d: %s\n",i,ans.c_str());
  }
    
  
  return 0;
}
