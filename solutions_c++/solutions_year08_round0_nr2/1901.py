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

int Z;
int T,NA,NB;

typedef pair<int,int>P;

int main(){
  string s;
  getline(cin,s);
  istringstream(s)>>Z;
  for(int n=1;n<=Z;++n){
    {getline(cin,s);istringstream(s)>>T;}
    {getline(cin,s);istringstream(s)>>NA>>NB;}
    priority_queue<P,vector<P>,greater<P> >Q[2];
    for(int i=0;i<NA;++i){
      int a[2],b[2];char c;
      getline(cin,s);istringstream(s)>>a[0]>>c>>a[1]>>b[0]>>c>>b[1];
      Q[0].push(P(a[0]*3600+a[1],b[0]*3600+b[1]));
    }
    for(int i=0;i<NB;++i){
      int a[2],b[2];char c;
      getline(cin,s);istringstream(s)>>a[0]>>c>>a[1]>>b[0]>>c>>b[1];
      Q[1].push(P(a[0]*3600+a[1],b[0]*3600+b[1]));
    }
    int R[2]={0,0},i;
    priority_queue<int,vector<int>,greater<int> >C[2];

    while(Q[0].size()||Q[1].size()){
      if(Q[0].size()&&Q[1].size()) i=Q[0].top().first<=Q[1].top().first?0:1;
      else if(Q[0].size()) i=0;
      else i=1;
      if(C[i].size()&&C[i].top()<=Q[i].top().first)
        C[i].pop();
      else
        R[i]++;
      C[(i+1)%2].push(Q[i].top().second+T);
      Q[i].pop();

    }
    cout<<"Case #"<<n<<": "<<R[0]<<" "<<R[1]<<endl;
  }
  return 0;
}
