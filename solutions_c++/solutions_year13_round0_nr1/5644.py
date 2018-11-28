#include <iostream>
#include <fstream>
using namespace std;

int main(int argc , char ** argv){
  ifstream f(argv[1]);
  int T;
  string line;
  char m[4][4];
  //  };
  f >> T;
  for(int i=0;i<T;++i){
    for(int j=0;j<4;j++){
      f >> line;
      for(int k=0;k<4;k++)
	m[j][k] = line[k];
    }
    
    bool found =false;
    for(int j=0;j<4 && !found;j++){
      if( (m[j][0] == 'T' || m[j][0] == 'X') && 
	  (m[j][1] == 'T' || m[j][1] == 'X') &&
	  (m[j][2] == 'T' || m[j][2] == 'X') &&
	  (m[j][3] == 'T' || m[j][3] == 'X')){
	  cout << "Case #" << i+1 << ": X won" << endl;
	  found = true;
      }
      else{
	if( (m[j][0] == 'T' || m[j][0] == 'O') &&
	    (m[j][1] == 'T' || m[j][1] == 'O') &&
	    (m[j][2] == 'T' || m[j][2] == 'O') &&
	    (m[j][3] == 'T' || m[j][3] == 'O')){
	  cout << "Case #" << i+1 << ": O won" << endl;
          found = true;
	}
      }
    }

    for(int j=0;j<4 && !found;j++){
      if( (m[0][j] == 'T' || m[0][j] == 'X') &&
          (m[1][j] == 'T' || m[1][j] == 'X') &&
          (m[2][j] == 'T' || m[2][j] == 'X') &&
          (m[3][j] == 'T' || m[3][j] == 'X')){
	cout << "Case #" << i+1 << ": X won" << endl;
	found = true;
      }
      else{
        if( (m[0][j] == 'T' || m[0][j] == 'O') &&
            (m[1][j] == 'T' || m[1][j] == 'O') &&
            (m[2][j] == 'T' || m[2][j] == 'O') &&
            (m[3][j] == 'T' || m[3][j] == 'O')){
          cout << "Case #" << i+1 << ": O won" << endl;
          found = true;
        }
      }
    }

    if( (m[0][0] == 'T' || m[0][0] == 'X') &&
	(m[1][1] == 'T' || m[1][1] == 'X') &&
	(m[2][2] == 'T' || m[2][2] == 'X') &&
	(m[3][3] == 'T' || m[3][3] == 'X')){
      cout << "Case #" << i+1 << ": X won" << endl;
      found = true;
    }

    if( (m[0][0] == 'T' || m[0][0] == 'O') &&
        (m[1][1] == 'T' || m[1][1] == 'O') &&
        (m[2][2] == 'T' || m[2][2] == 'O') &&
        (m[3][3] == 'T' || m[3][3] == 'O')){
      cout << "Case #" << i+1 << ": O won" << endl;
      found = true;
    }


    if( (m[0][3] == 'T' || m[0][3] == 'X') &&
        (m[1][2] == 'T' || m[1][2] == 'X') &&
        (m[2][1] == 'T' || m[2][1] == 'X') &&
        (m[3][0] == 'T' || m[3][0] == 'X')){
      cout << "Case #" << i+1 << ": X won" << endl;
      found = true;
    }

    if( (m[0][3] == 'T' || m[0][3] == 'O') &&
        (m[1][2] == 'T' || m[1][2] == 'O') &&
        (m[2][1] == 'T' || m[2][1] == 'O') &&
        (m[3][0] == 'T' || m[3][0] == 'O')){
      cout << "Case #" << i+1 << ": O won" << endl;
      found = true;
    }


    if(!found){
      for(int j=0;j<4 && !found;j++){
	for(int k=0;k<4 && !found;k++)
	  if(m[j][k] == '.'){
	    cout << "Case #" << i+1 << ": Game has not completed" << endl;
	    found = true;
	  }
      }      
      if(!found)
	cout << "Case #" << i+1 << ": Draw" << endl;
    }
  }
  
  f.close();
}
