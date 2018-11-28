#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

typedef long long lli;

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int i,j,n;
    lli rv=0;
    cin>>n;
    vector<int> v1(n),v2(n);
    for(i=0;i<n;++i) cin>>v1[i];
    for(i=0;i<n;++i) cin>>v2[i];
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    reverse(v2.begin(),v2.end());
    for(i=0;i<n;++i) rv+=1LL*v1[i]*v2[i];
    cout<<"Case #"<<ci<<": "<<rv<<endl;
  }
}
