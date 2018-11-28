#include <iostream>
#include <cmath>
using namespace std;
#define max(x,y) (((x)>(y))?(x):(y))
#define min(x,y) (((x)>(y))?(y):(x))
double dist(int x,int y,int z,int w){
  return sqrt((x-z)*(x-z)+(y-w)*(y-w));
}

int main(){
  int t;
  
  cin >> t;
  for (int ncas = 1; ncas<= t; ++ncas){
    int n;
    
    cin >> n;
    double ans = 0;
    int x[3],y[3],r[3];
    for (int i = 0; i < n; ++i)
      cin >> x[i]>> y[i]>>r[i];
    cout <<"Case #"<<ncas<<": ";
    if (n==1)
      cout << r[0]<<endl;
    else
      if (n==2)
	cout << max(r[0],r[1])<<endl;
      else{
	ans = max(dist(x[0],y[0],x[1],y[1])+r[0]+r[1],r[2]*2);
	ans = min(ans,max((dist(x[1],y[1],x[2],y[2])+r[1]+r[2]),r[0]*2));
	ans = min(ans,max((dist(x[2],y[2],x[0],y[0])+r[2]+r[0]),r[1]*2));
	cout << ans/2 <<endl;
      }    
  }
}
