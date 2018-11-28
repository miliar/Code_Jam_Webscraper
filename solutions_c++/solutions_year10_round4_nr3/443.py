#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
#define REP(i,N) for (int i = 0; i<(N); i++) 
#define ll long long

int N;
int x1[1000],x2[1000],y1[1000],y2[1000];
bool table[1000][1000];
vector<int> v[1000];
bool check[1000];
int lt, r, b;
int ans;

bool isconnect( int a, int b){
  return ( x1[a] <= x2[b]+1 && x1[b] <= x2[a]+1 &&
    y1[a] <= y2[b] && y1[b] <= y2[a] ) ||
    ( x1[a] <= x2[b] && x1[b] <= x2[a] &&
      y1[a] <= y2[b]+1 && y1[b] <= y2[a]+1 ) ||
    (x1[a] == x2[b]+1 && y2[a] == y1[b]-1) || 
    (x1[b] == x2[a]+1 && y2[b] == y1[a]-1);
    
}

void rec( int n){
  //  cout << "n "<<n<<endl;
  lt = min( lt, x1[n] + y1[n]);
  r = max( r, x2[n]);
  b = max( b, y2[n]);

  for (int i=0; i<v[n].size(); i++){
    if (check[v[n][i]]){
      check[v[n][i]] = false;
      rec (v[n][i]);
    }
  }
}

void makeAns(){
  ans = 0;
  fill (check, check+1000, true);
  for (int i=0; i<N; i++){
    if( check[i]){
      //      cout << "i "<< i << endl;
      lt = x1[i] + y1[i];
      r = x2[i];
      b = y2[i];
      check[i] = false;
      rec(i);
      ans = max (ans, r+b -lt);
    }
  }
}

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    cin >> N;
    REP(i,1000) v[i].clear();
    for (int i=0; i<N; i++){
      cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    }
    for (int i=0; i<N; i++){
      for (int j=0; j<N; j++){
	if (isconnect( i,j)){
	  v[i].push_back(j);
	}
	//	table[i][j] = isconnect[i][j];
      }
    }
    /*
    for (int i=0; i<N; i++){
      cout << i << " " ;
      for (int j=0; j<v[i].size(); j++){
	cout<<v[i][j] << " ";
      }cout << endl;
    }
    */
    makeAns();
    printf("Case #%d: %d\n",iii+1, ans+1);
  }
    
    
  return 0;
}
