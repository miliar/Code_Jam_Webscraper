#include <iostream>
#include <vector>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()

class A{
vector< vector<int> > g;
int n, m;
 
vector<bool> visited;
vector<int> matching;
 
bool augment(int left) {
    if (left < 0)
        return true;
    if (visited[left])
        return false;
    visited[left] = true;
    REP(i, g[left].size()) {
        int right = g[left][i];
        if (augment(matching[right])) {
            matching[right] = left;
            return true;
        }
    }
    return false;
}
int match() {
    matching.assign(m, -1);
    int matches = 0;
    REP(left, n) {
        visited.assign(n, false);
        if (augment(left))
            matches++;
    }
    return matches;
}
public:
int solve(){
  int M,N;
  cin>>M>>N;
  vector<vector<int> > data(M,N);
  int cnt[2]={0};
  for(int i=0; i<M; i++){
    for(int j=0; j<N; j++){
      char ch;
      cin>>ch;
      if(ch=='.'){
	data[i][j]=cnt[j%2]++;
      }
      else{
	data[i][j]=-1;
      }
    }
  }
  g.resize(cnt[0]);
  n=cnt[0];
  m=cnt[1];
  for(int j=0; j<N-1; j++){
    for(int i=0; ; i++){
      if(data[i][j]>=0&&data[i][j+1]>=0){
	if(j%2==0) g[data[i][j]].push_back(data[i][j+1]);
	else g[data[i][j+1]].push_back(data[i][j]);
      }
      if(i==M-1) break;
      if(data[i][j]>=0&&data[i+1][j+1]>=0){
	if(j%2==0) g[data[i][j]].push_back(data[i+1][j+1]);
	else g[data[i+1][j+1]].push_back(data[i][j]);
      }
      if(data[i+1][j]>=0&&data[i][j+1]>=0){
	if(j%2==0) g[data[i+1][j]].push_back(data[i][j+1]);
	else g[data[i][j+1]].push_back(data[i+1][j]);
      }
    }
  }
  //for(int i=0; i<4; i++){
    //for(int j=0; j<g[i].size(); j++){
      //cout<<g[i][j]<<" ";
    //}
    //cout<<endl;
  //}
  return cnt[0]+cnt[1]-match();
}
};

int main(){
  int C;
  cin>>C;
  for(int c=1; c<=C; c++){
    cout<<"Case #"<<c<<": ";
    A a;
    cout<<a.solve()<<endl;
  }
  return 0;
}

