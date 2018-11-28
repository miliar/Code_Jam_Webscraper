#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

const double EPS = 1e-8;

double a[1000010];

bool test(double* a,int n, double t, double d) {
  double init = a[0]-d;
    bool ans=true;
  for (int i = 1; i < n; ++i) {
    //cout<<x<<" "<<a[i]<<" "<<d<<endl;
    if (a[i]+d<init+t)
        ans=false;;
    init = max(a[i]-d,init+t);
  }
  return ans;
}

int main() {
  freopen("B-small-attempt0.in","r",stdin);
  freopen("Bs.txt","w",stdout);
  int cnum;
  //scanf("%d", &cnum);
  cin>>cnum;
  for(int I=0;I<cnum;++I) {
      printf("Case #%d: ",I+1);
    int n;
    double t;
    cin>>n>>t;

    //scanf("%d %lf", &n, &t);
    //cout<<t<<endl;
    int aa,b,p=0;
    for (int i = 0; i < n; ++i)
    {   cin>>aa>>b;
        for(int j=0;j<b;++j)
            a[p++]=aa;
    }
//    for(int i=0;i<n;++i)cout<<a[i]<<" ";
    n=p;
    //cout<<n<<endl;
    sort(a,a+n);
    double low = 0.0, high = 1.0;
    while (!test(a,n, t, high)) high *= 2;
    //cout<<hi<<endl;
    while (low+EPS<high) {
      double mid = (low+high)/2;
      if (test(a,n,t,mid)) high = mid;
      else low = mid;
      //cout<<lo<<" "<<hi<<endl;
    }
    printf("%.8lf\n", low);
  }
}
