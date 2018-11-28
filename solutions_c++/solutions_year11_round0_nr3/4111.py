#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

main() {
  int N;
  int a[10000];
  cin>>N;
  for(int c=0;c<N;++c) {
    int n,res=0,min=10000001,sum=0;
    cin>>n;
    for(int i=0;i<n;++i) {
      cin>>a[i];
      res ^= a[i];
      if(a[i] < min) min = a[i];
      sum += a[i];
    }

    cout<<"Case #"<<(c+1)<<": ";

    if(res)
      cout<<"NO\n";
    else
      cout<<(sum-min)<<endl;
  }

}
