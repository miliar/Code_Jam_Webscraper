#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>
#include <cmath>

using namespace std;

unsigned long dua_pangkat(int x) {
	unsigned long temp=1;
	for (int i=0; i <x; i++) {
		temp *= 2;
	}
	return temp;
}

void proses() {
  ifstream input("input.txt");
  ofstream output("output.txt");
  int jum = 0;
  input >> jum;
  for (int i=0; i < jum; i++) {
	  int scap = 0;
	  input >> scap;
	  unsigned long klip = 0;
	  input >> klip;
	  unsigned long tJum = 0;
	  tJum = dua_pangkat(scap) - 1;
	  unsigned long counter = 0;
	  counter = tJum+1;
	  unsigned long nyala = 0;
	  nyala = klip - tJum;
	  nyala = nyala % counter;
	  if (klip == 0) {
		  output << "Case #" << i+1 << ": OFF\n";
	  } else {
		  if (nyala == 0) {
			  output << "Case #" << i+1 << ": ON\n";
		  } else {
			  output << "Case #" << i+1 << ": OFF\n";
		  }
	  }
  }
  input.close();
  output.close();
}

int main(int argc, char *argv[])
{
    proses();
    return EXIT_SUCCESS;
}