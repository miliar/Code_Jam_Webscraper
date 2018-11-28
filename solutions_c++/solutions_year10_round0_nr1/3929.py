#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main() {
  string input_line;
  string buf;
  int count, switches;
  
  getline(cin, input_line);
  int max=atoi(input_line.c_str());
  
  int i=0;
  while(i++<max) {
	  getline(cin, input_line);
    
	  stringstream ss(input_line);
	
	  ss >> buf;
	  count = atoi(buf.c_str());
	  
	  ss >> buf;
	  switches = atoi(buf.c_str());
	
    if(pow(2, count)-1 == switches % (int) pow(2, count)){
      printf("Case #%i: ON\n", i);
    }else{
      printf("Case #%i: OFF\n", i);
    }
  }
}
