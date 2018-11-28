#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <map>
#include <set>
using namespace std;

#define INF 1000000000
// 1e9 < INT_MAX/2

#define M 10000

void tos(){
  int N;
  cin>>N;
  vector<int> A(N),B(N),C(N);
  for(int i=0; i<N; i++){
    cin>>A[i]>>B[i]>>C[i];
  }
  int res=0;
  for(int i=0; i<N; i++){
    int a=A[i];
    vector<pair<int,int> > seg;
    for(int j=0; j<N; j++){
      if(a<A[j]) continue;
      int bm=B[j];
      int bM=M-a-C[j];
      if(bm>bM) continue;
      seg.push_back(make_pair(bm,0));
      seg.push_back(make_pair(bM,1));
    }
    sort(seg.begin(),seg.end());
    int cnt=0;
    for(int j=0; j<seg.size(); j++){
      if(seg[j].second==0){
	cnt++;
      }else{
	cnt--;
      }
      res=max(res,cnt);
    }
  }
  cout<<res<<endl;
}

int main(){
  int nCases;
  cin>>nCases;
  for(int c=1; c<=nCases; c++){
    cout<<"Case #"<<c<<": ";
    tos();
  }
  return 0;
}
