#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#define PI 3.14159265358979323846264338327950288
#define MOD 100003
using namespace std;

vector< vector<char> > ToRedtile(vector< vector<char> > v , int i , int j ) {
  v[i-1][j-1] = '/';
  v[i-1][j] = '\\';
  v[i][j-1] = '\\';
  v[i][j] = '/';
  return v;
}



void cal() {
  int R, C;
  cin>>R>>C;
  vector< vector<char> > tile( R, vector<char>(C) );
  vector< vector<int> > arr(R, vector<int>(C) );
  for(int i = 0 ; i < R; i++)
    for(int j = 0; j < C; j++)
      cin>>tile[i][j];

  //cout<<endl;
  for(int i = 0; i < R; i++) {
    for(int j = 0; j < C; j++) {
      if ( i == 0 || j == 0 ) arr[i][j] = 0;
      else if ( tile[i][j] == '.' ) arr[i][j] = 0;
      else if ( tile[i][j] == '#' && tile[i-1][j] == '#' && tile[i][j-1] == '#' && tile[i-1][j-1] == '#' ) arr[i][j] = 1;
      else arr[i][j] = 0;
      //    cout<<arr[i][j]<<" ";
    }
    //    cout<<endl;
  }

  for(int i = 0; i < R; i++) {
    for(int j = 0; j < C; j++) {
      if ( arr[i][j] == 1 ) {
	tile = ToRedtile(tile, i, j);
	
	for(int k = i-1; k <= min(i+1, R-1); k++) 
	  for(int l = j-1; l <= min(j+1, C-1); l++)
	    arr[k][l] = 0;
      }
    }
  }

  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      if ( tile[i][j] == '#' ) {
	cout<<"Impossible"<<endl;
	return;
      }

  for(int i = 0; i < R; i++) {
    for(int j = 0; j < C; j++)
      cout<<tile[i][j];
    cout<<endl;
  }  

}

int main() {
  
  int T;
  cin>>T;
  for(int i = 1; i <= T; i++) {
    cout<<" Case #"<<i<<": "<<endl;
    cal();
  }

  return 0;
}
