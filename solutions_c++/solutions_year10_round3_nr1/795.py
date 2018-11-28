#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>
#include <cmath>

using namespace std;

void proses() {
  ifstream input("input.txt");
  ofstream output("output.txt");
  int jumlah = 0;
  input >> jumlah;
  for (int  i=0; i<jumlah; i++) {
	  int jumData = 0;
	  input >> jumData;
	  long dataX[1000];
	  long dataY[1000];
	  for (int j=0; j<jumData; j++) {
		  input >> dataX[j];
		  input >> dataY[j];
	  }
	  int Hasil = 0;
	  for (int j=0; j<jumData-1; j++) {
		  for (int k=j+1; k<jumData; k++) {
			  if (dataX[j] <= dataX[k] && dataY[j] >= dataY[k]) {
				  Hasil++;
			  } else if (dataX[j] >= dataX[k] && dataY[j] <= dataY[k]) {
				  Hasil++;
			  }
		  }
	  }
	  output << "Case #" << i+1 << ": " << Hasil << "\n";
  }
  input.close();
  output.close();
}

int main(int argc, char *argv[])
{
    proses();
    return EXIT_SUCCESS;
}