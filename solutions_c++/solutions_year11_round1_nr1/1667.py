#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <gmp.h>
#include <vector>
using namespace std;


int gcd( int m, int n )
{
	// 引数に０がある場合は０を返す
	if ( ( 0 == m ) || ( 0 == n ) )
		return 0;
	
	// ユークリッドの方法
	while( m != n )
	{
		if ( m > n ) m = m - n;
		else         n = n - m;
	}
	return m;
}//gcd

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
    ifs >> str;
    int Pd = atoi(str.c_str());
    ifs >> str;
    int Pg = atoi(str.c_str());
    if(Pg == 0 && Pd > 0){
      cout << "Broken" << endl;
      continue;
    }else if(Pg == 100 && Pd != 100){
      cout << "Broken" << endl;
      continue;
    }
      

    int gd = gcd(Pd, 100);
    int d_n = 0;
    int d_d = 0;
    if(gd != 0 ){
      d_n = Pd  / gd;
      d_d = 100 / gd;
    }
    
    if(d_d > N){
      cout << "Broken" << endl;
      continue;
    }

    if((Pg - d_n) > (100 - d_d)){
      cout << "Broken" << endl;
    }else{
      cout << "Possible" << endl;
      }
  
      
  } // T

  return 0;
}
