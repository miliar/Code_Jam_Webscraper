#include <iostream>
#include <string>
#define ABS(x) (((x)>0)?(x):(-(x)))
using namespace std;
int solve(){
  int n;
  string robotColour[100];
  int robotButton[100];
  int ans = 0;
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> robotColour[i] >> robotButton[i];
  int oPos,bPos,oExTime,bExTime,diff,incr;
  oPos=bPos=1;
  oExTime=bExTime=0;
  for (int i = 0; i < n; ++i){
    //    cout << ans << endl;
    if (robotColour[i]=="O"){
      diff=ABS(oPos-robotButton[i]);
      if (oExTime<=diff){
	diff-=oExTime;
	ans+=diff+1;
	bExTime+=(diff+1);
	oExTime=0;
      } else{
	ans+=1;
	bExTime+=1;
	oExTime=0;
      }
      oPos=robotButton[i];
    }else{
      diff=ABS(bPos-robotButton[i]);
      if (bExTime<=diff){
	diff-=bExTime;
	ans+=diff+1;
	oExTime+=(diff+1);
	bExTime=0;
      } else{
	ans+=1;
	oExTime+=1;
	bExTime=0;
      }
      bPos=robotButton[i];
    }
  }
  return ans;
  
}
int main(){
  int t;
  cin >> t;
  int caseNo=0;
  while (t--){
    cout << "Case #" << ++caseNo <<": " <<solve()<<"\n";
  }
}
