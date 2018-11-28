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

int N,M,R,Z;
vector<int> A[100][2];

int main(){
  string s;
  getline(cin,s);
  istringstream(s)>>Z;
  for(int n=1;n<=Z;++n){
    {getline(cin,s);istringstream(s)>>N;}
    vector<string>v1,v2;
    for(int i=0;i<N;++i){
      getline(cin,s);
      v1.push_back(s);
    }
    {getline(cin,s);istringstream(s)>>M;}
    for(int i=0;i<M;++i){
      getline(cin,s);
      v2.push_back(s);
    }
    for(int i=0;i<N;++i){
      int a=0;
      A[i][0].clear();
      A[i][1].clear();
      for(int k=0;k<M;++k){
        if(v1[i]==v2[k]){
          if(k-a>0){
            A[i][0].push_back(a);
            A[i][1].push_back(k-a);
          }
          a=k+1;
        }
      }
      if(M-a>0){
        A[i][0].push_back(a);
        A[i][1].push_back(M-a);
      }
    }
    R=0;
    for(int i=0;i<M;){
      int c=0;
      for(int k=0;k<N;++k){
        for(int j=0;j<A[k][0].size();++j){
          if(A[k][0][j]<=i){
            if(A[k][0][j]+A[k][1][j]<=i)continue;
            int d=A[k][0][j]-i+A[k][1][j];
            if(d>c)c=d;
          }
          break;
        }
      }
      i+=c;
      if(i<M)++R;
    }
    cout<<"Case #"<<n<<": "<<R<<endl;
  }
  return 0;
}

#if 0
#define N 10
#define C ((double)(1e0))
int main(){
  double f=1,R=100,t=1,r=1,g=10;


  double a,c,d,e,l,m,z,x=0,y=0;
  int b;
  for(double i=0;i<N;i++){
    a=sqrt(R*R*(1-(i*i)/(N*N)));
    if(2*a<2*f)break;
    m=(2*a-2*f+C)/C;
    z=0;
    e=2*(a-t-r);
    c=g+2*r;
    b=(int)(e/c);
    l=(e-b*c)/2;
    d=b*(g-2*f+C);
    if(d>0)z+=d/C;
    d=l-2*f+C;
    if(d>0)z+=2*d/C;
    x=z;
    y=(2*a-2*f+C)/C-z;
cout<<(x/m)*100<<" "<<(y/m)*100<<endl;
  }
}
#endif
