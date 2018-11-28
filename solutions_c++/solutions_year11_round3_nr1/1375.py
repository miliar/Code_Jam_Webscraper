#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;


#define SMALL_NON_ZERO 0.00000001 /* or something else small */
double ABS(double a)
{
   return ((a)<0?-(a):a);
}

int tiles[55][55];

int main() {
  int cases;

  cin >> cases;

  for(int cas = 1; cas <= cases; cas++) {
    int r, c;
    
    cin >> r >> c;
    
    for(int j = 0; j <= c; j++)
      tiles[0][j] = 0;
    
    for(int i = 1; i <= r; i++) {
      string temp;
      cin >> temp;
      for(int j = 0; j < c; j++) {
	  tiles[i][j] = (temp[j]=='#') ? 1 : 0;
      }
      tiles[i][c] = 12;
    }
    
    for(int j = 0; j <= c; j++)
      tiles[r+1][j] = 0;
    
    bool impossible = false;
    for(int i = 1; i <= r; i++) {
      for(int j = 0; j < c; j++) {
	if(tiles[i][j] == 1 && tiles[i][j+1] == 1){
	    if(tiles[i+1][j] == 1 && tiles[i+1][j+1] == 1) {
	      tiles[i][j] = 2;
	      tiles[i][j+1] = 3;
	      tiles[i+1][j] = 3;
	      tiles[i+1][j+1] = 2;
	    }else{
	      impossible =true;
	      break;
	    }
	}else if(tiles[i][j] == 1 && tiles[i][j+1] != 1){
	  impossible = true;
	  break;
	}
      }
    }
    
    if(impossible)
      cout << "Case #" << cas << ":" << endl <<"Impossible" << endl;
    else {
      cout << "Case #" << cas << ":" << endl;
      for(int i = 1; i <= r; i++) {
	for(int j = 0; j < c; j++) {
	  if(tiles[i][j] == 0)
	    cout << ".";
	  else if(tiles[i][j] == 2)
	    cout << "/";
	  else
	    cout << "\\";
	}
	cout << endl;
      }
    }
  }
  
  return 0;
}