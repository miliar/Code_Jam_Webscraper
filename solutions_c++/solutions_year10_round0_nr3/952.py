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

#define MAXN 1008
typedef long long ll;

int tcase;
int R,K,N;
ll G[MAXN];

ll T[MAXN];
int S[MAXN];

set<int> s;

int main(){
  
  freopen("C-large.in","r",stdin);
  freopen("out.txt","w",stdout);
  
  cin>>tcase;
  
  for(int i=1;i<=tcase;++i){
    
    cin>>R>>K>>N;
    for(int j=0;j<N;++j) cin>>G[j];
    int idx = 0;int sidx=0;
    s.clear();
    memset(T,0,sizeof(T));
    memset(S,0,sizeof(S));
    
    while(true){
     
     if(s.find(sidx)!=s.end()) break;
     s.insert(sidx);
     
     S[idx] =  sidx;
    
     ll sm = G[sidx];
     sidx++;
     if(sidx==N) sidx=0;
     while(sidx!=S[idx]){
      
      sm +=G[sidx]; if(sm>K) break; sidx++;  if(sidx==N) sidx=0; 
     }
     if(sidx!=S[idx])
      T[idx]=sm-G[sidx];
     else
      T[idx]=sm;
  //   cout<<S[idx]<<" "<<T[idx]<<endl;
     idx ++;
    }
  


    int index ;
    
    for(int j=0;j<idx;++j)
     if(S[j]==sidx) { index = j; }
    
  //  cout<<index<<endl;
    
    ll ssm = 0; ll tsm = 0;
    for(int j=0;j<index;++j) tsm += T[j];
    for(int j=index;j<idx;++j) ssm += T[j];
    
    ll r =0;

    if(R<=idx){
      for(int j=0;j<R;++j) r += T[j];
    }
    else if(R>idx){
      r += tsm;
      R -= index;
      ll q = R/(idx-index);
      r += q*ssm;
      for(int j=0;j<R%(idx-index);++j)
       r+=T[index+j];
    }
    printf("Case #%d: ",i);
    cout<<r<<endl;  
  }
          

  return 0;
}
