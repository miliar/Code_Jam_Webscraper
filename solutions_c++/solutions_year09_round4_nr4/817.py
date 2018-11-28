#include <vector>
#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

double dist(int x1,int y1,int x2,int y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}

bool cumple(vector<int> x,vector<int> y,vector<int> r,int N,double rad){
 
 if(N==1) return r[0]<=rad;
 if(N==2) return max(r[0],r[1])<=rad;
 else{
    double d1=dist(x[0],y[0],x[1],y[1])+r[0]+r[1];
    double d2=dist(x[1],y[1],x[2],y[2])+r[1]+r[2];
    double d3=dist(x[0],y[0],x[2],y[2])+r[0]+r[2];
   
    if(d1<=2*rad||d2<=2*rad||d3<=2*rad) return true;
    else return false;
 }
}

int main(){
 int C,N;
 cin>>C;
 
 for(int t=1;t<=C;t++){
  cin>>N;
  vector<int> x(N);
  vector<int> y(N);
  vector<int> r(N);
  for(int i=0;i<N;i++) cin>>x[i]>>y[i]>>r[i];
  
  double izq=*max_element(r.begin(),r.end()),der=2000;
  while(fabs(izq-der)>1e-12){
   double mid=(izq+der)/2;
   if(cumple(x,y,r,N,mid)) der=mid;
   else izq=mid;
  }
  
  cout<<"Case #"<<t<<": "<<(izq+der)/2<<endl; 
 }
}