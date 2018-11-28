#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

inline double abs(double a){
  return a>0?a:-a;
}

int main(){
  int T;
  cin>>T;
  for(int t=1; t<=T; t++){
    int N;
    cin>>N;
    vector<double> x(N),y(N),z(N),p(N);
    for(int i=0; i<N; i++){
      cin>>x[i]>>y[i]>>z[i]>>p[i];
    }
    /*
    double X,Y,Z;
    X=Y=Z=0.;
    */
    double res = 0.;
    for(int i=0; i<N; i++){
      for(int j=0; j<i; j++){
	double d=abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j]);
	d/=(p[i]+p[j]);
	if(d>res) res=d;
      }
    }
    //cout<<"Case #"<<t<<": ";
    //cout<<res<<endl;
    printf("Case #%d: %.8f\n", t, res);
  }
  return 0;
}
