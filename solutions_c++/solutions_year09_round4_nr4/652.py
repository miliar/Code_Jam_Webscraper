#include <stdio.h>
#include <iostream>
#include <fstream>

#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#define forn(i, n) for (int i = 0; i<(int) n; i++)
using namespace std;
int n;
int r[100], x[100], y[100];
double dist(int i, int j){
  i = i%n; j = j%n;
   double d = sqrt((x[i]-x[j]*1.0)*(x[i]-x[j]*1.0)+ (y[i]-y[j]*1.0)*(y[i]-y[j]*1.0));
//   cout<<d<<endl;
   return d;
}

int main(){
  freopen("d.in", "r", stdin);
  freopen("d.out", "w", stdout);
  int test;
  cin>>test;
  forn(tests, test)
  {
    cin>>n;
    forn(i,n)
      cin>>x[i]>>y[i]>>r[i];
    double ans = 10000000.0;
    if (n==1) ans = r[0];
    else if (n==2) ans = max(r[0], r[1]);
    else
    {
      for(int i = 0; i<3; i++)
        ans = min(ans,max(r[i]*1.0, (dist(i+1,i+2)+ r[(i+1)%3]+r[(i+2)%3])*0.5));
    }
    cout<<"Case #"<<tests+1<<": "<<ans<<endl;
  }
  return 0;
}
