#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main (int argc, char * argv[]) {
  int testcases;
  ifstream fi(argv[1]);

  fi >> testcases;
 
  for(int i=1; i<=testcases; ++i){
    int N,S,p;
    
    fi >> N;
    fi >> S;
    fi >> p;

    int sol=0;
    int min_no_surp = p*3 -2;
    int min_surp = min_no_surp-1;
    for(int j=0; j<N; ++j){
      int val;
      fi >> val;
      if(val >= min_no_surp ){
	sol++;
      }
      else{
	if(((val == min_surp || val == min_surp-1) && val!=0) && S!=0) {
	  sol++;
	  S--;
	}
      }
    }

//     for(int j=0; j<grades.size(); ++j)    
//             cout << " " << grades[j];
//           cout << endl;
    printf("Case #%d: %d\n",i,sol);
  }
  
}
