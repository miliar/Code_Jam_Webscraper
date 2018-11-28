#include<iostream>
#include<vector>
using namespace std;
long long a[1000],b[1000];
int main()
{ int T;
  cin>>T;
  for(int k=0;k<T;k++)
  { int n;
    cin>>n;
    for(int i=0;i<n;i++)
    cin>>a[i];
    for(int i=0;i<n;i++)
    cin>>b[i];
    sort(a,a+n);
    sort(b,b+n);
    reverse(b,b+n);
    long long sum=0;
    for(int i=0;i<n;i++)
    sum+=a[i]*b[i];
    cout<<"Case #"<<k+1<<": "<<sum<<"\n";
  }
}
