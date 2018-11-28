#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <gmp.h>
using namespace std;


  

int main(int argc, char *argv[]){
  ifstream ifs(argv[1]);
  string str;

  //  ifs >> str;
  //  cout << str << endl;

  ifs >> str;
  int T = atoi(str.c_str());

  for(int i = 0; i < T; i++){
    cout << "Case #" << i+1 << ": ";


    ifs >> str;
    int N = atoi(str.c_str()); 
    
    int t   = 1; // time
    int p_O = 1; // Position of Orange 
    int t_O = 1; // time of Orange
    int p_B = 1; // Position of Blue
    int t_B = 1; // time of Blue

    
    for(int j = 0; j < N; j++){
      ifs >> str;
      string Ri = str;
      ifs >> str;
      int  Pi = atoi(str.c_str());
      
      if(Ri == "O"){
	
	// t いじる
	int now_t = t; // 現在時刻
	
	// 移動
	int mov   = abs(p_O - Pi);
	int fut_t = t_O + mov;
	
	if(t_O == now_t){
	  if(mov == 0){ // 連続で自分のばんで同じところのボタンを押す
	    t = fut_t + 1;
	  }else{
	    t = fut_t + 1;
	  }
	}else if(t_O < now_t && fut_t < now_t){ // 
	  t = now_t + 1;
	}else{
	  t = fut_t + 1;
	}
	p_O = Pi;
	t_O = t;

      }else{
	// t いじる
	int now_t = t; // 現在時刻 
	
	// 移動
	int mov   = abs(p_B - Pi);
	int fut_t = t_B + mov;
	
	if(t_B == now_t){
	  if(mov == 0){ // 連続で自分のばんで同じところのボタンを押す
	    t = fut_t + 1;
	  }else{
	    t = fut_t + 1;
	  }
	}else if(t_B < now_t && fut_t < now_t){
	  t = now_t + 1;
	}else{
	  t = fut_t + 1;
	} 
	p_B = Pi;
	t_B = t;
      } // if(Ri == "O")
     
    } // N
    int temp = t_O < t_B ? t_B : t_O;
    cout << temp-1 << endl;

  } // T
 

  return 0;
}
