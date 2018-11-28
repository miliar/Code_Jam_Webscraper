#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>
#include <cmath>

using namespace std;

void proses() {
  ifstream input("input.txt");
  ofstream output("output.txt");
  int kasus = 0;
  input >> kasus;
  for (int i=0; i < kasus; i++) {
	  unsigned long iterasi = 0;
	  input >> iterasi;
	  unsigned long maximum = 0;
	  input >> maximum;
	  int penumpang = 0;
	  input >> penumpang;
	  unsigned long data[1100];
	  for (int j=0; j <penumpang; j++) {
		  input >> data[j];
	  }
	  unsigned long titerasi = 0;
	  unsigned long money = 0;
	  unsigned long tpenumpang = 0;
	  int pos = 0;
	  int jumP = 0;
	  while (titerasi < iterasi) {
		  if (jumP < penumpang) {
			  if (tpenumpang + data[pos] <= maximum) {
				  tpenumpang += data[pos];
				  jumP++;
			  } else {
				  jumP = 0;
				  money += tpenumpang;
				  tpenumpang = data[pos];
				  titerasi += 1;
			  }
			  pos++;
			  if (pos == penumpang) {
				  pos = 0;
			  }
		  } else {
			  jumP = 1;
			  money += tpenumpang;
			  tpenumpang = data[pos];
			  pos++;
			  if (pos == penumpang) {
				  pos = 0;
			  }
			  titerasi += 1;
		  }
	  }
	  output << "Case #" << i+1 << ": " << money << "\n";
  }
  input.close();
  output.close();
}

int main(int argc, char *argv[])
{
    proses();
    return EXIT_SUCCESS;
}