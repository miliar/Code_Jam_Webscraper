#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <gmp.h>
#include <vector>
using namespace std;


bool func(vector<string> b){ // bに#が0個ならfalse
  for(int i = 0; i < b.size(); i++){
    string t = b[i];
    for(int j = 0; j < t.size(); j++){
      if(t[j] == '#')
	return true;
    }
  }
  return false;
}

bool func2(vector<string> &b, int j, int k){
  if(j >= b.size() -1 || k >= b[1].size() -1)
    return false;
  if(b[j][k] == '#' && b[j+1][k] == '#' && b[j][k+1] == '#' && b[j+1][k+1] == '#'){
    b[j][k]     = '/';
    b[j+1][k]   = '\\';
    b[j][k+1]   = '\\';
    b[j+1][k+1] = '/';
    return true;
  }
  return false;
}

int main(int argc, char *argv[]){
  
  ifstream ifs(argv[1]);
  string str;

  ifs >> str;
  int T = atoi(str.c_str());

  for(int i = 0; i < T; i++){
    cout << "Case #" << i+1 << ": ";
    
    ifs >> str;
    int R = atoi(str.c_str());
    ifs >> str;
    int C = atoi(str.c_str());
    
    vector<string> brd;  
    for(int j = 0; j < R; j++){
      ifs >> str;
      brd.push_back(str);
    }
    
    /////////
    int chk = -1;


    //while(func(brd) && chk == -1){
      
      for(int j = 0; j < R; j++){
	for(int k = 0; k < C; k++){

	  if(chk == -1 && brd[j][k] == '#'){
	    if(j == R-1 || k == C-1){
	      chk = 100*j + k;
	    }else if(j == 0 && k == 0){
	      if(!func2(brd, j, k))
		chk = 2;
	      continue;
	    }
	    else if(j == 0 && (brd[0][k-1]=='.' || brd[0][k-1]=='/' || brd[0][k-1]=='\\')){
	      if(!func2(brd, j, k))
		chk = 3;
	      continue;
	    }
	    else if(k == 0 && (brd[j-1][0]=='.' || brd[j-1][0]=='/' || brd[j-1][0]=='\\')){
	      if(!func2(brd, j, k))
		chk = 4;
	      continue;
	    }
	    else if((brd[j-1][k]=='.' || brd[j-1][k]=='/' || brd[j-1][k]=='\\')&&( brd[j][k-1]=='.' || brd[j][k-1]=='/' || brd[j][k-1]=='\\')){
	      if(!func2(brd, j, k))
		chk = 5;
	      continue;
	    }
	    else{ 
	      chk = 6;}
	  } // if brd == #

	  if(chk != -1){
	    break;
	  }
	}

	if(chk != -1){
	  break;
	}
      }

      
    cout << endl;
    if(chk == -1){
      for(int j = 0; j < R; j++){
	for(int k = 0; k < C; k++){
	  cout << brd[j][k];
	}
	cout << endl;
      }
    }else{
      cout << "Impossible" << endl;
    }
  } // T
 

  return 0;
}
