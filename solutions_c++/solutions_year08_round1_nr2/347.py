#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;


//small
int main(){
  int C; cin >> C;
  for(int c=0;c<C;++c){
    int N, M; cin >> N >> M;
    vector<vector<pair<int, int> > > cus(M);
    for(int i=0;i<M;++i){
      int T; cin >> T;
      for(int t=0;t<T;++t){
	int f, m; cin >> f >> m;
	cus[i].push_back(make_pair(f-1, m));
      }
    }

    int min_cnt = 11;
    int min_pat = 0;
    for(int f=0;f<2<<10;++f){
      int cnt = 0;
      for(int i=0;i<N;++i)
	if(f&(1<<i)) ++cnt;
      if(cnt >= min_cnt) continue;

      for(int j=0;j<M;++j){
	for(int k=0;k<cus[j].size();++k){
	  int m = 0;
	  if(f&(1<<cus[j][k].first)) m = 1;

	  if(cus[j][k].second == m) goto ok;
	}
	goto next;
      ok:;
      }
      min_cnt = cnt;
      min_pat = f;

    next:;
    }

    cout << "Case #" << (c+1) << ":" ;
    if(min_cnt == 11){
	cout << " IMPOSSIBLE" << endl;
    }else{
      for(int i=0;i<N;++i){
	if(min_pat&(1<<i))
	  cout << " " << 1;
	else
	  cout << " " << 0;
      }
      cout << endl;
    }

    
  }
}
