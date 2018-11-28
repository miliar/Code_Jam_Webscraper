#include <iostream>
#include <vector>
using namespace std;

#define MOD 10007

int main(){
  int N;
  cin>>N;
  for(int n=1; n<=N; n++){
    cout<<"Case #"<<n<<": ";
    int W,H,R;
    cin>>W>>H>>R;
    vector<int> w(R), h(R);
    int map[128][128]={0};
    for(int i=0; i<R; i++){
      cin>>w[i]>>h[i];
      map[w[i]+1][h[i]+1]=-1;
    }
    for(int i=1; i<=W; i++){
      for(int j=1; j<=H; j++){
	if(i+j==2){
	  map[i+1][j+1]=1;
	  continue;
	}else if(map[i+1][j+1]==-1){
	  map[i+1][j+1]=0;
	  continue;
	}else{
	  map[i+1][j+1]=(map[i-1][j]+map[i][j-1])%MOD;
	}
      }
    }
    cout<<map[W+1][H+1]<<endl;
  }
  return 0;
}

