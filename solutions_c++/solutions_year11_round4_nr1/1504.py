#include <cstring>
#include <string>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long int64;

int tcase;
int X,S,R,t,N;
int A[105];

int main(){
  cin>>tcase;
  for(int tc=1;tc<=tcase;++tc){
    cin>>X>>S>>R>>t>>N;
    memset(A,0,sizeof(A));
    for(int i=0;i<N;++i){
       int a,b,x;  cin>>a>>b>>x;
       for(int j=a+1;j<=b;++j) A[j]=x;
    }
    vector < pair < double , int  > >  d;
    for(int i=1;i<=X;++i){
      double t1 = 1.0/(S+A[i]);
      double t2 = 1.0/(R+A[i]);
      d.push_back(make_pair(t1-t2,i)); 
    }
    sort(d.begin(),d.end());
    reverse(d.begin(),d.end());
    double tm  = 0; double tt = 0;    
    for(int i=0;i<d.size();++i){
       if(tm<t) {
          double tx = 1.0/(A[d[i].second]+R); 
          if(tm+tx<=t) { tm += tx; tt += tx; }
          else {
             tx = min(tx,t-tm);  tm += tx; tt += tx; 
             double rm = 1-tx*(A[d[i].second]+R);
             tt += rm*1.0/(A[d[i].second]+S); 
          }  
       }
       else {
           tt += 1.0/(A[d[i].second]+S);
       }
    }
    cout<<"Case #"<<tc<<": ";
    printf("%.6lf\n",tt);
  }    

  return 0;
}
