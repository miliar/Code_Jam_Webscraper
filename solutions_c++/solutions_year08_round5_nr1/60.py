#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
  int N;
  cin>>N;
  for(int n=1; n<=N; n++){
    cout<<"Case #"<<n<<": ";
    vector<vector<int> > l(256,256);
    vector<vector<int> > u(256,256);
    int X=128, Y=128;
    int L;
    cin>>L;
    int v=0;
    while(L--){
      string S;
      int T;
      cin>>S>>T;
      for(int i=0; i<T; i++){
	for(int j=0; j<S.size(); j++){
	  if(S[j]=='L'){
	    v++;
	    if(v==4) v=0;
	  }else if(S[j]=='R'){
	    if(v==0) v=4;
	    v--;
	  }else if(S[j]=='F'){
	    switch(v){
	      case 0:
		u[X][Y]=1;
		X++;
		break;
	      case 1:
		l[X][Y]=1;
		Y++;
		break;
	      case 2:
		X--;
		u[X][Y]=1;
		break;
	      case 3:
		Y--;
		l[X][Y]=1;
	    }
	  }
	}
      }
    }
    vector<vector<int> > cnt1(256,256);
    vector<vector<int> > cnt2(256,256);
    for(int i=0; i<256; i++){
      int f=2;
      for(int j=0; j<256; j++){
	if(u[i][j]) f=(f+1)%2;
	cnt1[i][j]=f;
      }
      if(f==0){
	for(int j=256; j-->0; ){
	  if(cnt1[i][j]) break;
	  cnt1[i][j]=2;
	}
      }
    }
    for(int j=0; j<256; j++){
      int f=2;
      for(int i=0; i<256; i++){
	if(l[i][j]) f=(f+1)%2;
	cnt2[i][j]=f;
      }
      if(f==0){
	for(int i=256; i-->0; ){
	  if(cnt2[i][j]) break;
	  cnt2[i][j]=2;
	}
      }
    }
    int res=0;
    for(int i=0; i<256; i++){
      for(int j=0; j<256; j++){
	if(cnt1[i][j]==0||cnt2[i][j]==0) res++;
      }
    }
  //for(int i=-35; i<35; i++){
    //cout<<endl;
    //for(int j=-35; j<35; j++){
      //cout<<cnt[128+i][128+j];
    //}
  //}

    cout<<res<<endl;
  }
  return 0;
}

