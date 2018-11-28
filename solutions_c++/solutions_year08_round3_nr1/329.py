#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <ctime>
#include <math.h>
using namespace std;
typedef long long LL;
int NN;
int main(){
  string in;
  getline(cin,in);
  istringstream(in)>>NN;
  for(int II=1;II<=NN;++II){
    int P,K,L;
    getline(cin,in);
    istringstream(in)>>P>>K>>L;
    vector<int>v;
    {
      getline(cin,in);
      istringstream ss(in);
      int a;
      while(ss>>a){
        if(a)v.push_back(a);
      }
    }
    if(v.size()>P*K){
      cout<<"Case #"<<II<<": Impossible"<<endl;
      continue;
    }
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());
    int res=0;
    for(int i=0;i<v.size();++i){
      res+=((i/K)+1)*v[i];
    }
    cout<<"Case #"<<II<<": "<<res<<endl;
  }
  return 0;
}
