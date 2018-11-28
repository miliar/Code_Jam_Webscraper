#include<iostream>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;

int main(){

  int T;cin>>T;
  for(int t=0;t<T;t++){//# of test;
    double D;cin>>D;//distance;
    int N;cin>>N;//only N=2;
    int A;cin>>A;
    
    double it[2];//time;
    double x[2];//position;
    double a[10];//acceleation;
    for(int i=0;i<N;i++)cin>>it[i]>>x[i];
    for(int i=0;i<A;i++)cin>>a[i];
    
    //the final time of other's car; 
    double v=(x[1]-x[0])/(it[1]-it[0]);
    double ft=(D-x[0])/v;
    if(N==1)ft=0.0;
    double res[10];
    for(int i=0;i<A;i++){
      double rt=sqrt(2.0*D/a[i]);
      res[i]=max(ft, rt);
    }
    
    
    string g="Case #";
    int L=t+1;
    if(L<10)g+=(char)(L+'0');else{g+=(char)(L/10+'0');g+=(char)(L%10+'0');}
    g+=":";
    cout<<g<<endl;;
    for(int i=0;i<A;i++)printf("%f\n",res[i]);
  }
  return 0;
}
