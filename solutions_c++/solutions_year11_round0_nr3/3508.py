#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
  int T;
  cin>>T;

  for(int SET=1;SET<=T;SET++){
    int n;
    cin>>n;

    int cal = 0;
    int t[n];

    for(int i=0;i<n;i++){
      cin>>t[i];
      cal ^= t[i];
    }

    if(cal != 0){
      printf("Case #%d: NO\n",SET);
      continue;
    }

    sort(t,t+n);
    long long ans = 0;
    for(int i=1;i<n;i++){
      ans += t[i];
    }
    printf("Case #%d: %lld\n",SET,ans);
  }

  return 0;
}
