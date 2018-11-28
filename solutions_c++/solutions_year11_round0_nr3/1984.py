#include<iostream>
#include<cassert>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
template <class T> void pp(T &a,int p){for(int i=0;i<p;i++)cout << a[i]<<" ";  cout << endl;}

main(){
  int te;
  cin>>te;
  for(int tc=1;tc<=te;tc++){
    int n,in[15];
    cin>>n;
    for(int i=0;i<n;i++)cin>>in[i];
    int ans=-1;
    int cnt=0;
    for(int i=1;i<(1<<n)-1;i++){
      int a=0,b=0,asum=0;
      for(int j=0;j<n;j++)
	if ((1<<j)&i)a^=in[j],asum+=in[j];
	else b^=in[j];
      if (a == b)ans=max(asum,ans),cnt++;
    }
    int tmp=0;
    for(int i=0;i<n;i++)tmp=tmp^in[i];
    cout <<"Case #" << tc << ": ";
    if (ans == -1)cout<< "NO" << endl;
    else cout << ans << endl;
  }
  return false;
}
