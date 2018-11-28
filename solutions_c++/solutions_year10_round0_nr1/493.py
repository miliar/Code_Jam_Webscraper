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

main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    int64 n,k,m;
    cin>>n>>k;
    m=(1LL<<n)-1;
    cout<<"Case #"<<c<<": "<<(((k&m)==m)?"ON":"OFF")<<endl;
  }
}
