/* -*- c++ -*-
   ID: dirtysalt
   PROG: 
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <numeric>
#include <algorithm>

using namespace std;
typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < double >VD;
typedef pair < int, int >PII;
#define SZ(v) ((int)((sizeof(v))/sizeof(*(v))))
#define PV(v) do {						\
    cout<<#v<<endl;						\
    for(int i=0;i<(int)(v).size();i++)cout<<(v)[i]<<" ";	\
    cout<<endl; \
  }while(0)
#define PA(v) do{							\
    cout<<#v<<endl;							\
    for(int i=0;i<(int)(sizeof(v)/sizeof(*(v)));i++)cout<<(v)[i]<<" ";	\
    cout<<endl;								\
  }while(0)
#define FUNC() do{					\
    cout<<"=========="<<__func__<<"=========="<<endl;	\
  }while(0)
const int INF=0x1fffffff;
const double EPS=1e-6;
double x[40];
double y[40];
double r[40];
int n;
double dist(double x1,double y1,double x2,double y2)
{
  //cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<endl;
  double r=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
  //cout<<r<<endl;
  return r;
}

bool test(double m)
{
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      for(int k=j+1;k<n;k++){
	double d1=dist(x[i],y[i],x[j],y[j])+r[i]+r[j];
	double d2=dist(x[i],y[i],x[k],y[k])+r[i]+r[k];
	double d3=dist(x[j],y[j],x[k],y[k])+r[j]+r[k];
	if(d1>2*m && d2>2*m && d3>2*m){
	  //cout<<d1<<" "<<d2<<" "<<d3<<endl;
	  return false;
	}
      }
    }
  }
  return true;
}

int main()
{
  int casn;
  cin>>casn;
  for(int t=1;t<=casn;t++){    
    cin>>n;
    for(int i=0;i<n;i++){
      cin>>x[i]>>y[i]>>r[i];
      //cout<<x[i]<<" "<<y[i]<<" "<<r[i]<<endl;
    }
    double l,h,m;
    if(n==1)m=r[0];
    else if(n==2){
      m=max(r[0],r[1]);
    }else{
      l=0.0;
      h=20000.0;
      for(int k=1;k<=1000;k++){
	m=(l+h)/2;
	if(test(m)){
	  h=m;
	}else{
	l=m;
	}
      }
    }
    printf("Case #%d: %.7lf\n",t,m);
  }
}
