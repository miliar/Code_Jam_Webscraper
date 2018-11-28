#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 55;

int main(){
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  string tiles[MAXN];
  
  int r, c;
  for(int test = 0; test < testcases; test++){
    bool gerai = true;
    scanf("%d %d", &r, &c);
    for(int i = 0; i < r; i++)
      cin >> tiles[i];
    
    for(int i = 0; i < r; i++)
      for(int j = 0; j < c; j++)
	if(tiles[i][j] == '#'){
	  if(j + 1 < c && i + 1 < r && tiles[i][j+1] == '#' && tiles[i+1][j] == '#' && tiles[i+1][j+1] == '#' ){
	    tiles[i][j] = '/';
	    tiles[i][j+1] = '\\';
	    tiles[i+1][j] = '\\';
	    tiles[i+1][j+1] = '/';
	  }
	  else
	    gerai = false;
	}
    printf("Case #%d:\n", test+1);
    if(gerai)
      for(int i = 0; i < r; i++)
	cout << tiles[i] << endl;
    else
      cout << "Impossible" << endl;
	
  }
  
  return 0;
}