#include<iostream>
#include<vector>
#include<algorithm>

#define FOR(i,b,n) for(int i = b; i < n; i++)
#define REP(i,n) FOR(i,0,n)

using namespace std;

int t, r, c;
bool flg;
vector<string> V;

int main(){
  cin >> t;

  REP(Case, t){
    cin >> r >> c;

    V.clear();

    REP(i, r){
      string str;
      cin >> str;
      V.push_back(str);
    }

    flg = 1;

    for(int i = 0; i < r - 1 && flg; i++)
      for(int j = 0; j < c - 1 && flg; j++)
      if(V[i][j] == '#'){
	if(V[i][j] == '#' && V[i + 1][j] == '#' && V[i][j + 1] == '#' && V[i + 1][j + 1] == '#'){
	  V[i][j] = '/';
	  V[i][j + 1] = '\\';
	  V[i + 1][j] = '\\';
	  V[i + 1][j + 1] = '/';
	}else
	  flg = 0;
      }

    REP(i, r) REP(j, c)
      if(V[i][j] == '#')
	flg = 0;

    
    cout << "Case #" << Case + 1 << ":" << endl;
    if(flg)
      REP(i, r)
	cout << V[i] << endl;
    else
      cout << "Impossible" << endl;
  }
  return 0;
}
