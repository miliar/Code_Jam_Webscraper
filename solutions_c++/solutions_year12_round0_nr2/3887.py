#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	
  scanf("%d\n", &T);
	
	for (int t=1; t<=T; t++) { 
  	int i;
  	int N, S, p;
  	
  	scanf("%d %d %d", &N, &S, &p);
  	
  	int total[101];
  	
  	int count = 0;
  	
    for (int n=0; n<N; n++) { 
      scanf("%d", &total[n]);
      
      if (total[n] % 3 == 0) {
        if (total[n]/3 >= p)
          count++;
        else if ((total[n] > 0) && (S > 0) && (total[n]/3 + 1 >= p)) {
          S--;
          count++;
        }
      }
      else if (total[n] % 3 == 1) {
        if (total[n]/3 + 1 >= p)
          count++;
      }
      else if (total[n] % 3 == 2) {
        if (total[n]/3 + 1 >= p)
          count++;
        else if ((S > 0) && (total[n]/3 + 2 >= p)) {
          S--;
          count++;
        }
      }      
    }
    
	  cout << "Case #" << t << ": " << count << endl;
	}
	
  return 0;
}
