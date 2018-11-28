#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>
#include <cmath>

using namespace std;

int gcd(int a, int b)
{
	if(b == 0)
    {
		return a;
    }
    else
    {
         return gcd(b, a % b);
    }
}

void proses() {
  ifstream input("input.txt");
  ofstream output("output.txt");
  int jumCase = 0;
  input >> jumCase;
  for (int i=0; i<jumCase; i++) {
	  int jumAngka = 0;
	  input >> jumAngka;
	  unsigned long long data[1000];
	  unsigned long long terkecil = 0;
	  for (int j=0; j<jumAngka; j++) {
		  input >> data[j];
		  if (j==0) {
			  terkecil = data[j];
		  } else {
			  if (terkecil > data[j]) {
				  terkecil = data[j];
			  }
		  }
	  }
	  unsigned long long selisihData[1000];
	  int jumSelisih = 0;
	  int tempAngka = 0;
	  while (tempAngka < jumAngka-1) {
		  if (data[tempAngka] > data[tempAngka+1]) {
			  selisihData[jumSelisih] = data[tempAngka] - data[tempAngka+1];
		  } else {
			  selisihData[jumSelisih] = data[tempAngka+1] - data[tempAngka];
		  }
		  tempAngka += 1;
		  jumSelisih++;
	  }
	  unsigned long long fpb = 0;
	  unsigned long long param1 = 0;
	  unsigned long long param2 = 0;
	  int tempSelisih=0;
	  while (jumSelisih > 0) {
		  if (jumSelisih == 1) {
			  fpb = selisihData[0];
			  jumSelisih = 0;
		  } else {
			  param1 = selisihData[jumSelisih-1];
			  param2 = selisihData[jumSelisih-2];
			  if (param1 > param2) {
				  fpb = gcd(param1,param2);
			  } else {
				  fpb = gcd(param2,param1);
			  }
			  selisihData[jumSelisih-2] = fpb;
			  jumSelisih -= 1;
		  }
	  }
	  bool kel = false;
	  while (!kel) {
		  if (terkecil > fpb) {
			  terkecil -= fpb;
		  } else {
			  terkecil = fpb - terkecil;
			  kel = true;
		  }
	  }
	  output << "Case #" << i+1 << ": " << terkecil << "\n";
  }
  input.close();
  output.close();
}

int main(int argc, char *argv[])
{
    proses();
    return EXIT_SUCCESS;
}