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
#define MAXN 1000004

int L[MAXN][2];

int mfind(int s,int e,int k){
  int r = MAXN;
  while(s<=e){
   int m = (s+e)/2;
   if(L[m][0]<=k && L[m][0]+L[m][1]-1>=k){
     r = min(r,m);e = m-1;
   }
   else s = m+1;
  }
  return r;
}

int main(){
      // freopen("in.txt","r",stdin);
      freopen("C-small-attempt3.in","r",stdin);
       freopen("out.txt","w",stdout);  
   
  memset(L,0,sizeof(L));
  L[1][0]=1; L[1][1]=1;
  L[2][0]=2; L[2][1]=2;
  for(int i=3;i<=MAXN;++i){
    L[i][0]=i;
    L[i][1]=mfind(1,i-1,i);
  // cout<<L[i][0]<<" "<<L[i][1]<<endl;
  }
  int t;
  scanf("%d",&t);
  for(int k=1;k<=t;++k){
    int a1,a2,b1,b2;
    cin>>a1>>a2>>b1>>b2;
    int total = (a2-a1+1)*(b2-b1+1);
    for(int i=a1;i<=a2;++i)
     for(int j=b1;j<=b2;++j){
        int a,b; a = i;b=j;
        if(a>=b) { int t = b; b = a; a= t;}
        if(b>=L[a][0] && L[a][0]+L[a][1]-1>=b) --total;  
    }
    cout<<"Case #"<<k<<": "<<total<<endl;
  }
  
  return 0;
}
