#include <iostream>
#include <cstdlib>
#include <math.h>
#include <set>
#include <utility>
#include <fstream>
#include <string>

using namespace std;
int main(int argc,char ** argv){

  int A ,B;
  string Aaux;
  int num_digits;
  int result =0;
  int temp1, temp2,temp3,new_m;
  set<pair<int,int> > s;
  ifstream fi(argv[1]);
  
  int T;

  fi >> T;

  for(int k=1;k<=T;k++){
    fi >> Aaux;
    num_digits = Aaux.length();
    A = atoi(Aaux.c_str());
    fi >> B;

    s.clear();

    for(int i=A;i<B;i++){
      for(int j=1;j<=num_digits;j++){
	temp1 = i%((int) pow(10,j));
	temp2 = temp1 * ((int)pow(10,(num_digits-j)));
	temp3 = i/((int) pow(10,j));
      
	new_m = temp2 + temp3;
      
	if(new_m > i && new_m <= B )
	  s.insert(make_pair(i,new_m));
      }
    }

    cout << "Case #" << k << ": " << s.size() << endl;
  }

  fi.close();
 
}
