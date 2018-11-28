#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    int r,k,n;scanf("%d%d%d",&r,&k,&n);
    int g[1111];
    REP(i,n)scanf("%d",&g[i]);
    int to[1111], pl[1111];
    REP(i,n){
      int sum=g[i];
      int index=(i+1)%n;
      while(index != i && sum + g[index] <= k){
        sum += g[index];
        index++;
        index%=n;
      }
      to[i]=index;
      pl[i]=sum;
    }
    int kde=0;
    int vis[1111];
    memset(vis,-1,sizeof(vis));
    int rounds=0;
    ll tot=0;
    while(rounds<r){
      if(vis[kde]!=-1){
        int len=rounds-vis[kde];
        ll csum = 0;
        REP(i,len){
          csum+=pl[kde];
          kde=to[kde];
        }
        int kr=(r-rounds)/len;
        tot += (ll)kr * csum;
        rounds += kr * len;
        memset(vis,-1,sizeof(vis));
        continue;
      }
      vis[kde] = rounds;
      tot+=pl[kde];
      kde=to[kde];
      rounds++;
    }
    cout<<" "<<tot<<endl;
  }
  return 0;
}
