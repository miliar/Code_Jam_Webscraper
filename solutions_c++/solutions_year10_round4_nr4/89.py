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

ld pi=acos(0.0)*2.0;

ld ar(ld x1, ld y1, ld r1, ld x2, ld y2, ld r2){
  x2-=x1;
  y2-=y1;
  ld dst= sqrt(x2*x2+y2*y2);
//  if(r1+r2<dst-1e-9)return 0;
  if(r1>=dst+r2){
    return pi*r2*r2;
  }
  if(r2>=dst+r1){
    return pi*r1*r1;
  }

  ld d=dst;
  ld r=r2;
  ld R=r1;

  ld pr1 = d*d+r*r-R*R;
  ld pr2 = d*d+R*R-r*r;
  ld num1 = 2.0*d*r;
  ld num2 = 2.0*d*R;

  ld cbd = acos(pr1/num1);
  ld cad = acos(pr2/num2);

  ld s1 = r*r*cbd;
  ld s2 = R*R*cad;

//ld p1=sqrt((-d+r+R)*(d+r+R));
//ld p2=sqrt((d+r-R)*(d-r+R));
  return s1+s2-(ld)0.5*r*r*sin((ld)2.0*cbd)-(ld)0.5*R*R*sin((ld)2.0*cad);

}

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    int n,m;
    scanf("%d%d",&n,&m);    
    int x[111],y[111];
    REP(i,n)scanf("%d%d",&x[i],&y[i]);
    REP(i,m){
      int xx,yy;scanf("%d%d",&xx,&yy);
      ld rad[2];
      REP(i,2){
        rad[i] = (x[i]-xx)*(x[i]-xx)+(y[i]-yy)*(y[i]-yy);
        rad[i]=sqrt(rad[i]);
      }
      printf(" %.15Lf",ar(x[0],y[0],rad[0],x[1],y[1],rad[1]));
    }
    printf("\n");
  }
  return 0;
}
