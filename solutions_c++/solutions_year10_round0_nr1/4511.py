#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <string.h>
using namespace std;

int main() {
  string line;
  ifstream file ("A-small-attempt0.in");
  ofstream out;
  out.open("answer.out", ios::out);
  if(file.is_open()) {
    getline(file, line);
    int i = atoi(line.c_str());
    int j;
    for(j = 0; j < i; j++) {
      getline(file,line);
      int index = line.find(" ");
      string n1 = line.substr(0,index);
      string k1 = line.substr(index);
      int N = atoi(n1.c_str());
      int K = atoi(k1.c_str());

      //main loopN
      int snappers[N];
      int power[N];
      int z;
      for(z = 0; z < N; z++) { //initialization
	snappers[z] = 0;
	power[z] = 0;
      }
      power[0] = 1;

      int y;
      for(y = 0; y < K; y++) {

	for(z = 0; z < N; z++) {
	  if(power[z] == 1) {
	    if(snappers[z] == 0) {
	      snappers[z] = 1;
	    }
	    else {
	      snappers[z] = 0;
	    }
	  }
	}

	for(z = 0; z < N; z++) {
	  if(snappers[z] == 1 && power[z] == 1) {
	    power[z+1] = 1;
	  }
	  else
	    power[z+1] = 0;
	}

      }
      
      if( snappers[z-1] == 1 && power[z-1] == 1)
	out << "Case #" << j + 1 << ": " << "ON" << endl;
      else
	out << "Case #" << j + 1 << ": " << "OFF" << endl;
    }
  }
  file.close();
  out.close();

  return 0;

}
