#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int n; cin>>n;
    vector<int> bd(n);
    for (int i=0;i<n;i++){
      string s; cin>>s;
      int a=0;
      for (int j=0;j<n;j++)
	if (s[j]=='1')
	  a=j;
      bd[i]=a;
    }
    int ans=0;
    for (int i=0;i<n;i++){
      int j=i;
      while(j<n && bd[j]>i) j++;
      assert(j!=n);
      while(j!=i) swap(bd[j], bd[j-1]), j--, ans++;
    }
    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
