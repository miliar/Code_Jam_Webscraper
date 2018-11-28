#include <iostream>
#include <iomanip>
#include <vector>
#include <complex>
using namespace std;

typedef complex<double> pt;

int main()
{
  cout<<setiosflags(ios::fixed)<<setprecision(10);

  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int n; cin>>n;
    vector<pt> ps(n);
    vector<double> rs(n);

    for (int i=0;i<n;i++)
      cin>>ps[i].real()>>ps[i].imag()>>rs[i];

    double ans=0;
    for (int i=0;i<n;i++)
      ans=max(ans, rs[i]);

    if (n>=3){
      double aa=1e10;
      for (int i=0;i<n;i++){
	for (int j=i+1;j<n;j++){
	  aa=min(aa, (abs(ps[i]-ps[j])+rs[i]+rs[j])/2);
	}
      }
      ans=max(ans, aa);
    }

    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
