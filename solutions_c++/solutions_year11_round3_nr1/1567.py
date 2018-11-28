#include<iostream>
using namespace std;

int main(){
  int t,r,c;
  char map[50][50];

  cin >> t;
  for(int i=0;i<t;i++){
    cin >> r >> c;
    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
	cin >> map[j][k];
      }
    }

    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
	if(map[j][k]=='#' && map[j+1][k]=='#' &&map[j][k+1]=='#' &&map[j+1][k+1]=='#'){
	  map[j][k] = '/';
	  map[j+1][k] = '\\';
	  map[j][k+1] = '\\';
	  map[j+1][k+1] = '/';
	}
      }
    }
    int flag = 1;
    for(int j=0;j<r;j++){
      for(int k=0;k<c;k++){
	if(map[j][k]=='#')flag = 0;
      }
    }
    
    cout << "Case #" << i+1 << ": " << endl;
    if(flag){   
      for(int j=0;j<r;j++){
	for(int k=0;k<c;k++){
	  cout << map[j][k];
	}
	cout << endl;
      }
    }else{
      cout << "Impossible" << endl;
    }
  }
}
