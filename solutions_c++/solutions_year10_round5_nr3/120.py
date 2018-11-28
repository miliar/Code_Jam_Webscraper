#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

#define INF 1000000000
#define MAX 110000
int P,a[MAX],b[MAX];
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    cin>>P;
    FOR(i,P)cin>>a[i]>>b[i];
    map<int,int> m;
    FOR(i,P)m[a[i]]+=b[i];    
    int64 r=0;
    while(1){
       bool found=0;
       map<int,int> m2;
       FOREACH(iter,m)if(iter->second>1){
         r+=iter->second/2;
         m2[iter->first-1]+=iter->second/2;
         m2[iter->first+1]+=iter->second/2;
         m2[iter->first]+=iter->second%2;
         found=1;
       }else if(iter->second==1)m2[iter->first]++;
      if(!found)break;
      swap(m,m2);
    }    
    cout<<"Case #"<<c<<": "<<r<<endl;
  }
}
