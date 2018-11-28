#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;


int main(){
  int t;
  cin >> t;
  for(int id = 1; id<=t; id++){
    cout << "Case #" << id << ": ";
    int r,k,n;
    vector<int> g; g.clear();

    cin >> r >> k >> n;
    g.resize(n);
    vector< pair<int,int> > vis(n,make_pair(-1,0));
    for(int i=0; i<n; i++){
      cin >> g[i];
    }
    int sum = 0;
    int idx = 0;
    int cr = 0;
    while(1){
      if(vis[idx].first != -1)break;
      if(cr == r) break;
      vis[idx].first = sum;
      vis[idx].second = cr;
      cr++;
      int tmp = 0;
      int sidx = idx;
      while(1){
	if(tmp + g[idx] > k)break;
	tmp += g[idx];
	sum += g[idx];
	idx = (idx + 1) % n;
	if(idx == sidx)break;
      }
    }
    int difr = cr - vis[idx].second;
    int difc = sum - vis[idx].first;
    int rr = r - cr;
    sum += (rr/difr)*difc;
    int l = rr%difr;
    for(int i=0; i<l; i++){
      int tmp = 0;
      int sidx = idx;
      while(1){
	if(tmp + g[idx] > k)break;
	tmp += g[idx];
	sum += g[idx];
	idx = (idx + 1) % n;
	if(idx == sidx)break;
      }
    }
    cout << sum << endl;

  }
  return 0;
}

