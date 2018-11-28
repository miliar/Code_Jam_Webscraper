#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int tc=1; tc<=t; tc++){
    int n;
    cin >> n;
    vector<int> tab(n,0);
    for(int i=0; i<n; i++){
      cin >> tab[i];
    }
    sort(tab.begin(),tab.end());
    int ans = 0;
    int tmp = tab[0];
    for(int i=1; i<n; i++){
      tmp ^= tab[i];
      ans += tab[i];
    }
    printf("Case #%d: ",tc);
    if(tmp != 0)printf("NO\n");
    else printf("%d\n",ans);
  }
  return 0;
}
