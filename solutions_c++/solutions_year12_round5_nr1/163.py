#include<iostream>
#include<iomanip>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>


using namespace std;

vector<double> v;

bool ssort(int a, int b){
  if (v[a]==v[b]) return a<b;
  return v[a]<=v[b];
}

int main(){
  int T; cin>>T;
  for (int tc=1;tc<=T;tc++){
    cout<<"Case #"<<tc<<": ";
    int N; cin>>N;
    vector<double> L(N,0);
    vector<double> P(N,0);
    for (int i=0;i<N;++i)
      cin>>L[i];
    for (int i=0;i<N;++i)
      cin>>P[i];
    v=vector<double>(N,0);
    vector<int> ind(N,0);
    for (int i=0;i<N;++i){
      ind[i]=i;
      v[i]=L[i]/P[i];
    }
    sort(ind.begin(), ind.end(), ssort);
    for (int i=0;i<N;++i){
      cout<<ind[i]<<" ";
    }
    cout<<endl;
      


  }
  return 0;
}
