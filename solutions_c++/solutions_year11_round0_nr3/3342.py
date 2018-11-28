#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main () {
  ifstream inFile;
  inFile.open ("example.txt");
 
  int test_cases, num_candy, value, total_value, total, min;

  if (inFile.is_open()) {
    inFile >> test_cases;
    for (int i=1; i <= test_cases;++i) {
      inFile >> num_candy;
      total=0;
      for(int j=1; j<= num_candy;++j){
	inFile >> value;
	
	if(j==1){
	  min = value;
	  total_value=value;
	  total += value;
	  continue;
	}
	total_value ^= value;
	total += value;

	if(value < min)
	  min = value;
      }
      cout << "Case #"<<i<<": ";
      if (total_value != 0)
	cout << "NO" << endl;
      else
	cout << total - min << endl;
    }
}



 inFile.close();

  return 0;
}

