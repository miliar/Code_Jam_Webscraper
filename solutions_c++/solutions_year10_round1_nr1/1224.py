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
	  int ukuran = 0;
	  int dimensi = 0;
	  input >> ukuran;
	  input >> dimensi;
	  char data[50][50];
	  for (int j=0; j<ukuran; j++) {
		  for (int k=0; k<ukuran; k++) {
			  input >> data[j][k]; //baris, kolom
		  }
	  }
	  bool keluar = false;
	  int indexX = 0;
	  int indexY = ukuran-1;
	  bool geser = false;
	  int count = 0;
	  while (!keluar) {
		  if (data[indexY][indexX] == '.') {
			  for (int j= indexX; j > 0; j--) {
				  data[indexY][j] = data[indexY][j-1];
			  }
			  data[indexY][0] = '.';
			  geser = true;
			  count++;
			  if (count == indexX+1) {
				  geser = false;
				  count = 0;
			  }
		  } else {
			  geser = false;
			  count = 0;
		  }
		  if (!geser) {
			  indexY--;
			  if (indexY < 0) {
				  indexX++;
				  indexY = ukuran-1;
				  if (indexX >= ukuran) {
					  keluar = true;
				  }
			  }
		  }
	  }
	  //Pengecekan
	  bool menangR = false;
	  bool menangB = false;
	  for (int j=ukuran-1; j>=0; j--) {
		  int hitungRB=0;
		  int hitungBB=0;
		  int hitungRK=0;
		  int hitungBK=0;
		  int hitungRD1=0;
		  int hitungBD1=0;
		  int hitungRD2=0;
		  int hitungBD2=0;
		  for (int k=ukuran-1; k>=0; k--) {
			  //cek kolom
			  if (data[j][k] == 'R') {
				  hitungRK++;
				  if (hitungRK == dimensi) {
					  menangR = true;
				  }
				  hitungBK=0;
			  } else
			  if (data[j][k] == 'B') {
				  hitungBK++;
				  if (hitungBK == dimensi) {
					  menangB = true;
				  }
				  hitungRK=0;
			  } else {
				  if (hitungRK == dimensi) {
					  menangR = true;
				  }
				  if (hitungBK == dimensi) {
					  menangB = true;
				  }
				  hitungRK=0;
				  hitungBK=0;
			  }
			  //cek baris
			  if (data[k][j] == 'R') {
				  hitungRB++;
				  if (hitungRB == dimensi) {
					  menangR = true;
				  }
				  hitungBB=0;
			  } else
			  if (data[k][j] == 'B') {
				  hitungBB++;
				  if (hitungBB == dimensi) {
					  menangB = true;
				  }
				  hitungRB=0;
			  } else {
				  if (hitungRB == dimensi) {
					  menangR = true;
				  }
				  if (hitungBB == dimensi) {
					  menangB = true;
				  }
				  hitungRB=0;
				  hitungBB=0;
			  }
		  }
		  //cek diagonal1
		  if (ukuran-j >= dimensi) {
			  int indexingX =j;
			  int indexingY = ukuran-1;
			  while (indexingX <= ukuran-1) {
				  if (data[indexingY][indexingX] == 'R') {
					  hitungRD2++;
					  if (hitungRD2 == dimensi) {
						  menangR = true;
					  }
					  hitungBD2=0;
				  } else 
				  if (data[indexingY][indexingX] == 'B') {
					  hitungBD2++;
					  if (hitungBD2 == dimensi) {
						  menangB = true;
					  }
					  hitungRD2=0;
				  }	else {
					  if (hitungRD2 == dimensi) {
						  menangR = true;
					  }
					  if (hitungBD2 == dimensi) {
						  menangB = true;
					  }
					  hitungBD2=0;
					  hitungRD2=0;
				  }
				  indexingX++;
				  indexingY--;
			  }
		  }
		  if (j+1 >= dimensi) {
			  int indexingX =j;
			  int indexingY = ukuran-1;
			  while (indexingX >= 0) {
				  if (data[indexingY][indexingX] == 'R') {
					  hitungRD1++;
					  if (hitungRD1 == dimensi) {
						  menangR = true;
					  }
					  hitungBD1=0;
				  } else 
				  if (data[indexingY][indexingX] == 'B') {
					  hitungBD1++;
					  if (hitungBD1 == dimensi) {
						  menangB = true;
					  }
					  hitungRD1=0;
				  }	else {
					  if (hitungRD1 == dimensi) {
						  menangR = true;
					  }
					  if (hitungBD1 == dimensi) {
						  menangB = true;
					  }
					  hitungBD1=0;
					  hitungRD1=0;
				  }
				  indexingX--;
				  indexingY--;
			  }
		  }
	  }
	  if (menangR && menangB) {
		  output << "Case #" << i+1 << ": Both\n";
	  } else if (menangR) {
		  output << "Case #" << i+1 << ": Red\n";
	  } else if (menangB) {
		  output << "Case #" << i+1 << ": Blue\n";
	  } else {
		  output << "Case #" << i+1 << ": Neither\n";
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