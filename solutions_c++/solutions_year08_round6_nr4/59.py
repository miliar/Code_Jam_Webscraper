#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    int n;
    cin >> n;
    vector<vector<int> > matrix(n, vector<int>(n,0));
    for(int i=0;i<n-1;i++){
      int a,b;
      cin >> a >> b;
      matrix[a-1][b-1] = 1;
      matrix[b-1][a-1] = 1;
    }
    int m;
    cin >> m;
    vector<vector<int> > matrix2(m, vector<int>(m,0));
    for(int i=0;i<m-1;i++){
      int a,b;
      cin >> a >> b;
      matrix2[a-1][b-1] = 1;
      matrix2[b-1][a-1] = 1;
    }
    vector<int> array(n);
    for(int i=0;i<n;i++){
      array[i] = i;
    }
    bool ok = false;
    do {
      bool can = true;
      for(int i=0;i<m;i++){
	for(int j=0;j<m;j++){
	  if(matrix2[i][j] && !matrix[array[i]][array[j]]){
	    can = false;
	  }
	}
      }
      if(can)ok=true;
    } while(next_permutation(array.begin(), array.end()));
    if(ok)cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
