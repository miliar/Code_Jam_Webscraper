#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int main(){
  int C;
  cin>>C;
  for (int c=1;c<=C;c++){
    int N,K,B,T;
    cin>>N>>K>>B>>T;
    vector<int> chicks(N);
    vector<int> speeds(N);
    for (int i=0;i<N;i++){
      cin>>chicks[i];
    }
    for (int i=0;i<N;i++){
      cin>>speeds[i];
      if (speeds[i]*T+chicks[i]>=B)
	speeds[i]=1;
      else
	speeds[i]=0;
    }
    int swaps=0;
    int done=0;
    int broken=0;
    for (int j=N-1;j>=0;j--){
      if (speeds[j]){
	done++;
	swaps+=broken;
	if (done==K)
	  break;
      }
      else{
	broken++;
      }
    }
    if (done==K){
      cout<<"Case #"<<c<<": "<<swaps<<endl;
    }
    else
      cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
  }
}
