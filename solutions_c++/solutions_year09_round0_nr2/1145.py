#include<iostream>
#include<vector>
#include<map>

using namespace std;

int dx[] = { 0,-1, 1, 0};
int dy[] = {-1, 0, 0, 1};
int H, W;
int c;
int dfs(const vector<vector<int> >& M, int y, int x, vector<vector<int> >& D){
  if(D[y][x] != 0) return D[y][x];
  int mp = 0;
  for(int i=1;i<4;++i){
    if(M[y+dy[i]][x+dx[i]] < M[y+dy[mp]][x+dx[mp]])
      mp = i;
  }
  if(M[y+dy[mp]][x+dx[mp]] < M[y][x]){
    return D[y][x] = dfs(M, y+dy[mp], x+dx[mp], D);
  }else{
    return D[y][x] = c++;
  }
}

int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
    cin >> H >> W;
    vector<vector<int> > M(H+2, vector<int>(W+2, 20000));
    vector<vector<int> > D(H+2, vector<int>(W+2, 0));
    c = 1;


    
    for(int y=1;y<=H;++y)
      for(int x=1;x<=W;++x)
	cin >> M[y][x];

    for(int y=1;y<=H;++y)
      for(int x=1;x<=W;++x)
	dfs(M, y, x, D);
    
//     for(int y=1;y<=H;++y){
//       for(int x=1;x<=W;++x){
// 	cout << D[y][x] << " ";
//       }
//       cout << endl;
//     }
    

    map<int, char> m;
    char nc = 'a';
    cout << "Case #" << (t+1) << ":" << endl;
    for(int y=1;y<=H;++y){
      for(int x=1;x<=W;++x){
	if(x!=1) cout << ' ';
	if(m.find(D[y][x]) == m.end()){
	  m[D[y][x]] = nc++;
	}
	cout << m[D[y][x]];
      }
      cout << endl;
    }
    
  }
}
