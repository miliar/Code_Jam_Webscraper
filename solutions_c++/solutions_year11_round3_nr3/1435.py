#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <gmp.h>
#include <vector>
using namespace std;


  

int main(int argc, char *argv[]){
  ifstream ifs(argv[1]);
  string str;

  ifs >> str;
  int T = atoi(str.c_str());

  for(int i = 0; i < T; i++){
    cout << "Case #" << i+1 << ": ";
    
    ifs >> str;
    int N = atoi(str.c_str());
    ifs >> str;
    int L = atoi(str.c_str());
    ifs >> str;
    int H = atoi(str.c_str());
    vector<int> hz(H+1,1);

    int chk = -1;

    

    for(int k = 0; k < N; k++){

      ifs >> str;
      int temp = atoi(str.c_str());
      for(int j = L; j <= H; j++){    
	if(hz[j] == 1 && ( j % temp == 0 || temp % j == 0)){
	}else{
	  hz[j] = 0;
	}
      }

    }

    for(int j = L; j <= H; j++){
      if(hz[j] == 1){
	chk = j;
	break;
      }
    }
    if(chk == -1){
      cout << "NO" << endl;
    }else{
      cout << chk << endl;
    }
	  
	  
    



  } // T
 

  return 0;
}
