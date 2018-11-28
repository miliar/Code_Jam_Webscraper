#include <iostream>
#include <vector>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=1; t<=T; t++){
    int K;
    cin>>K;
    vector<int> ans(K+1);
    int pos=0;
    for(int i=1; i<=K; i++){
      int cnt=i;
      while(1){
	if(ans[pos]==0){
	  cnt--;
	  if(cnt==0) break;
	}
	pos++;
	if(pos==K) pos=0;
      }
      ans[pos]=i;
    }
    cout<<"Case #"<<t<<":";
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
      int ind;
      cin>>ind;
      cout<<" "<<ans[ind-1];
    }
    cout<<endl;
  }
  return 0;
}


