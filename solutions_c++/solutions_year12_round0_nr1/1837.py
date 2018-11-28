// read in text file
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;
int main ()
{
  FILE * pFile;
  char inputText[4000];
  char numCasesChar[2];
  char c;
  int n = 0;
  int i;
  int j;

  int numCases;


  pFile=fopen ("A-small-attempt0.in","r");
  if (pFile==NULL) perror ("Error opening file");
  else
  {
    do {
	  c = fgetc (pFile);
	  inputText[n]=c;
	  n++;
    } while (c != EOF);
    fclose (pFile);

  }

  numCasesChar[0] = inputText[0];
  numCasesChar[1] = inputText[1];

  numCases = atoi(numCasesChar);

  j=1;
  if (inputText[j]!=10) {
	  j++;
  }
  j++;
  
  // open file to write
  ofstream myfile ("output.txt");


  for (i=0;i<numCases;i++) {
	  myfile << "Case #" << i+1 << ": ";
	  while ((inputText[j]!='\n')&(inputText[j]!=EOF)) {
		  c = inputText[j];
		  if (c==' ') {
			myfile << ' ';
		  }
		  if (c=='a') {
			  myfile << 'y';
		  }
		  if (c=='b') {
			  myfile << 'h';
		  }
		  if (c=='c') {
			  myfile << 'e';
		  }
		if (c=='d') {
			  myfile << 's';
		  }
		if (c=='e') {
			  myfile << 'o';
		  }
		if (c=='f') {
			  myfile << 'c';
		  }
		if (c=='g') {
			  myfile << 'v';
		  }
		if (c=='h') {
			  myfile << 'x';
		  }
		if (c=='i') {
			  myfile << 'd';
		  }
		if (c=='j') {
			  myfile << 'u';
		  }
		if (c=='k') {
			  myfile << 'i';
		  }
		if (c=='l') {
			  myfile << 'g';
		  }
		if (c=='m') {
			  myfile << 'l';
		  }
		if (c=='n') {
			  myfile << 'b';
		  }
		if (c=='o') {
			  myfile << 'k';
		  }
		if (c=='p') {
			  myfile << 'r';
		  }
		if (c=='q') {
			  myfile << 'z';
		  }
		if (c=='r') {
			  myfile << 't';
		  }
		if (c=='s') {
			  myfile << 'n';
		  }
		if (c=='t') {
			  myfile << 'w';
		  }
		if (c=='u') {
			  myfile << 'j';
		  }
		if (c=='v') {
			  myfile << 'p';
		  }
		if (c=='w') {
			  myfile << 'f';
		  }
		if (c=='x') {
			  myfile << 'm';
		  }
		if (c=='y') {
			  myfile << 'a';
		  }
		if (c=='z') {
			  myfile << 'q';
		  }
		  j++;
	  }
	  j++;
	  myfile << '\n';
  }
	


  return 0;
}

