#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main(){
  int T;

  cin >> T;
  for(int test=1;test<=T;test++){
    int N,ans;
    int ps[2],sk[2];
    ps[0]=ps[1]=1;
    sk[0]=sk[1]=ans=0;
    cin >> N;
    for(int i=0;i<N;i++){
      string r;
      int p;
      cin >> r >> p;
      int x;
      if(r=="B") x=1;
      else x=0;
      int mv;
      mv = (abs(ps[x]-p))-sk[x];
      sk[x]=0;
      ps[x]=p;
      if(mv<0)mv=1;
      else mv+=1;
      sk[!x]+=mv;
      ans+=mv;

    }
    cout << "Case #" << test << ": " << ans << endl;
  }
  return 0;
}
