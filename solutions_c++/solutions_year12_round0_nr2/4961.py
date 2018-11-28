#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(){
  
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);

  int t;
  cin >> t;

  for(int ncase=1;ncase<=t;ncase++){
    int res = 0;
    int n,s,p;
    cin >> n >> s >> p;
    for(int i=0;i<n;i++){
      int ti;
      cin >> ti;
      if(ti%3==0){
        int mx = ti/3;
        if(mx>=p) res++;
        else if(ti && s && (mx+1)>=p){ res++; s--; }
      }else if(ti%3==2){
        int mx = ti/3 + 1;
        if(mx>=p) res++;
        else if(s && (mx+1)>=p){ res++; s--; }
      }
      else if(ti%3 == 1){
        int mx = ti/3 + 1;
        if(mx>=p) res++;
      }
      }
    cout << "Case #" << ncase << ": " << res << endl;
  }
  
  return 0;
}

