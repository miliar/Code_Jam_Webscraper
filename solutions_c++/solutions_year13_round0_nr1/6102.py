#include <iostream>
#include <string>
using namespace std;

const string stat[] = {"X won","O won","Draw","Game has not completed"};

int col(char arr[4][4],int j){
  char ch = arr[0][j];
  if(ch == 'T')
      ch = arr[1][j];
  
  for(int i=0 ; i<4 ; ++i){
    if(arr[i][j] == 'T')
	continue;
      if(arr[i][j] != ch || arr[i][j] == '.')
	return -1;
  }
  
  return ((ch == 'O') ? 1 : 0);
}

int row(char arr[4][4],int i){
  char ch = arr[i][0];
  if(ch == 'T')
      ch = arr[i][1];
  
  for(int j=0 ; j<4 ; ++j){
    if(arr[i][j] == 'T')
	continue;
      if(arr[i][j] != ch || arr[i][j] == '.')
	return -1;
  }
  
  return ((ch == 'O') ? 1 : 0);
}

int di1(char arr[4][4]){
  char ch = arr[0][0];
  if(ch == 'T')
      ch = arr[1][1];
  
  for(int i=0 ; i<4 ; ++i){
    if(arr[i][i] == 'T')
	continue;
      if(arr[i][i] != ch || arr[i][i] == '.')
	return -1;
  }
  
  return ((ch == 'O') ? 1 : 0);
}

int di2(char arr[4][4]){
  char ch = arr[0][3];
  if(ch == 'T')
      ch = arr[1][2];
  
  int j = 3;
  for(int i=0 ; i<4 ; ++i,--j){
      if(arr[i][j] == 'T')
	continue;
      if(arr[i][j] != ch || arr[i][j] == '.')
	return -1;
  }
  
  return ((ch == 'O') ? 1 : 0);
}

int main(){
  int t;
  cin >> t;
  char arr[4][4];
  
  for(int tc=1; tc<=t ; ++tc){
    int win = 0;
    bool done = false;
    
    for(int i=0 ; i<4 ; ++i)
      for(int j=0 ; j<4 ; ++j)
	cin >> arr[i][j];
    
    
    for(int i=0 ; i<4 ; ++i){
      int a = row(arr,i);
      if(a != -1){
	  cout << "Case #" << tc << ": " << stat[a] << endl;
	  done = true;
	  break;
      }
      a = col(arr,i);
      if(a != -1){
	  cout << "Case #" << tc << ": " << stat[a] << endl;
	  done = true;
	  break;
      }
    }
    if(done)
      continue;
    
    int a = di1(arr);
    if(a != -1){
	cout << "Case #" << tc << ": " << stat[a] << endl;
	continue;
    }
    
    a = di2(arr);
    if(a != -1){
	cout << "Case #" << tc << ": " << stat[a] << endl;
	continue;
    }
    
    a = 0;
    for(int i=0 ; i<4 ; ++i){
      for(int j=0 ; j<4 ; ++j){
	if(arr[i][j] == '.'){
	  a = 1;
	  break;
	}
      }
    }
    
    if(a)
      cout << "Case #" << tc << ": " << stat[3] << endl;
    else
      cout << "Case #" << tc << ": " << stat[2] << endl;
  }
  return 0;
}