#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
//#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int read_line(char* str, int max) {
  //char* inp = new char[100];
  int len = 0;
  while (len < max -1) {
    char c;
    scanf( "%c", &c);
    if (c == '\n') break;
    str[len++] = c;
  }
  str[len] = '\0';
  return len;
}

int main() {

  

  int num_inputs;
  scanf( "%d\n", &num_inputs );
  for (int cidx = 0; cidx<num_inputs; ++cidx) {
    int num_people, special, target;
    int count = 0;
    scanf("%d %d %d", &num_people, &special, &target);


    //int* a = new int[num_people];
    for (int i = 0 ; i < num_people; ++i) {
      int temp;
      scanf("%d", &temp);

      if ( target == 0 ) {
	count++;
	continue;
      }

      if ( temp == 0 ) {
        continue;
      }

     
      if ( target == 1 ) {
	count++;
	continue;
      }
      
      int targetn_min = target -1;
      
      int targets_min = target -2;

      

      targetn_min *= 2;
      targets_min *= 2;

      targetn_min += target;
      targets_min += target;

      

      if ( temp >= targetn_min ) {
	count++;
	continue;
      }

      if ( temp >= targets_min ) 
	if ( special-- > 0 ) 
           count++;
      

    }

    scanf("\n");

    cout << "Case #" << (cidx+1) << ": " << count << endl;
  }

}

