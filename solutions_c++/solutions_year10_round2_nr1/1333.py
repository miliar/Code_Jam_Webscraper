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
	  int jumList = 0;
	  int jumFind = 0;
	  input >> jumList;
	  input >> jumFind;
	  char data[1000][200];
	  char temp[200];
	  int posData[1000];
	  int jumData = 0;
	  for (int j=0; j< jumList; j++) {
		  input >> temp;
		  char tempIsi[200] = "";
		  int indexTempIsi = 0;
		  int posIsi = -1;
		  for (int k=0; k< strlen(temp); k++) {
			  if (k==0) {
				  posIsi = -1;
			  } else {
				  if (temp[k] == '/') {
					  bool ada = false;
					  for (int l=0; l<jumData; l++) {
						  if (strcmp(data[l],tempIsi) == 0 && !ada) {
							  if (posData[l] == posIsi) {
								  ada = true;
								  posIsi = l;
								  //posIsi++;
							  }
						  }
					  }
					  if (!ada) {
						  strcpy(data[jumData],tempIsi);
						  posData[jumData] = posIsi;
						  posIsi = jumData;
						  jumData++;
					  }
					  indexTempIsi = 0;
				  } else {
					  tempIsi[indexTempIsi] = temp[k];
					  indexTempIsi++;
					  tempIsi[indexTempIsi] = '\0';
				  }
			  }
		  }
		  bool ada = false;
		  for (int l=0; l<jumData; l++) {
			  if (strcmp(data[l],tempIsi) == 0 && !ada) {
				  if (posData[l] == posIsi) {
					  ada = true;
				  }
			  }
		  }
		  if (!ada) {
			  strcpy(data[jumData],tempIsi);
			  posData[jumData] = posIsi;
			  jumData++;
		  }
	  }
	  int jumlahBuat = 0;
	  for (int j=0; j< jumFind; j++) {
		  input >> temp;
		  char tempIsi[200] = "";
		  int indexTempIsi = 0;
		  int posIsi = -1;
		  for (int k=0; k< strlen(temp); k++) {
			  if (k==0) {
				  posIsi = -1;
			  } else {
				  if (temp[k] == '/') {
					  bool ada = false;
					  for (int l=0; l<jumData; l++) {
						  if (strcmp(data[l],tempIsi) == 0 && !ada) {
							  if (posData[l] == posIsi) {
								  ada = true;
								  posIsi = l;
								  //posIsi++;
							  }
						  }
					  }
					  if (!ada) {
						  jumlahBuat++;
						  strcpy(data[jumData],tempIsi);
						  posData[jumData] = posIsi;
						  posIsi = jumData;
						  jumData++;
					  }
					  indexTempIsi = 0;
				  } else {
					  tempIsi[indexTempIsi] = temp[k];
					  indexTempIsi++;
					  tempIsi[indexTempIsi] = '\0';
				  }
			  }
		  }
		  bool ada = false;
		  for (int l=0; l<jumData; l++) {
			  if (strcmp(data[l],tempIsi) == 0 && !ada) {
				  if (posData[l] == posIsi) {
					  ada = true;
				  }
			  }
		  }
		  if (!ada) {
			  jumlahBuat++;
			  strcpy(data[jumData],tempIsi);
			  posData[jumData] = posIsi;
			  jumData++;
		  }
	  }
	  output << "Case #" << i+1 << ": " << jumlahBuat <<"\n";
  }
  input.close();
  output.close();
}

int main(int argc, char *argv[])
{
    proses();
    return EXIT_SUCCESS;
}