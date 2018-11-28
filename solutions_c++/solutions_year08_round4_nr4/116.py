#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main(){
  int N;
  cin>>N;
  for(int nn=1; nn<=N; nn++){
    cout<<"Case #"<<nn<<": ";
    int K;
    string S;
    cin>>K>>S;
    int Sl=S.size();
    int res=Sl+1;
    vector<int> A(K);
    for(int i=0; i<K; i++){
      A[i]=i;
    }
    do{
      string T;
      T.resize(Sl);
      for(int i=0; i<Sl; i++){
	int q=i/K;
	int r=i%K;
	T[i]=S[q*K+A[r]];
      }
      int cnt=1;
      for(int i=1; i<Sl; i++){
	if(T[i]!=T[i-1]){
	  cnt++;
	}
      }
      if(cnt<res) res=cnt;
    }while(next_permutation(A.begin(), A.end()));
    cout<<res<<endl;
  }
  return 0;
}
