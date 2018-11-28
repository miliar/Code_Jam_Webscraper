#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

int main(){
	freopen("C-small-attempt1.in","r",stdin);
  freopen("C-small-attempt1.out","w",stdout);
  int t;
  while(cin >> t){
    for(int cas=1; cas<=t; ++cas){
      int n,l,h;
      cin >> n >> l >> h;
      int num[1009];
      for(int i=0; i<n; ++i) cin >> num[i];
      sort(num,num+n);
      int flag=0;
      cout << "Case #" << cas << ": ";
        for(int i=l; i<=h && !flag; ++i){
          int j;
          for( j=0; j<n && !flag; ++j)
            if(num[j]<=i && i%num[j]==0 || num[j]>=i && num[j]%i==0)
              continue;
            else break;
            if(j>=n){
              cout << i << endl;
              flag=1;
              break;
            }
        }
        if(!flag) cout << "NO" << endl;
      }
    }
  return 0;
}
