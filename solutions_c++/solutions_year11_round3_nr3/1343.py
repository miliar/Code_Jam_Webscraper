/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Jirapong Manit 2011 <jirapong.manit@gmail.com>
 * 
 * CodeJamA1 is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * CodeJamA1 is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>


using namespace std;

char inputfile[] = "inputfile.txt";
const char outfile[] = "outputfile.txt";

int getscore(char alphabet, char list[]);
int maxVal(const int val[], const int size, int& index, int& max);
void SelectionSort(unsigned long A[], int length);

int main(int argc, char *argv[])
{

	/* Variables */
	ifstream inputfd;
	ofstream outputfd;
	int nCase = 0, N;
	unsigned long L, H;
	unsigned long other[10000];
	
	/********************************************/

	if(argc > 1){	   // load the input file
		cout << "Read input from argc '" << argv[1] << "'" << endl;
		strcpy(argv[1], inputfile);	
	}else {
		cout << "Automatically read from '" << inputfile << "'" << endl;
	}

	inputfd.open(inputfile, fstream::in);

	if(inputfd.fail()){
		cerr << "error: cannot read file '" << inputfile << "'\n";
		inputfd.close();
		return -1;
	}
	
	outputfd.open(outfile);

	if(outputfd.fail()){
		cerr << "error: cannot create file '" << outfile << "'\n";
		outputfd.close();
		return -1;
	}

	inputfd >> nCase;	   //read case number
	cout << "There is " << nCase << " cases." << endl;

	for(int i = 0; i < nCase; i++){

		//read input file
		inputfd >> N;
		inputfd >> L;
		inputfd >> H;

		cout << N  << " " << " " <<  L << " " << H << endl;
		for(int j = 0; j < N; j++){
			inputfd >>  other[j];
		}
		
		//process
		SelectionSort(other, N);
		for(int j = 0; j < N; j++){
			cout <<   other[j] << " ";
		}
		cout << endl;
		int poss = 0;
		int note = 0;
		for(int j = L; j <= H; j++){
			poss = 0;
			for(int k = 0; k < N; k ++){
				if((other[k] % j==0) || (j%other[k] ==0)){
					poss = poss+1;
				}
			}
			if(poss == N){
				note = j;
				break;
			}
		}
			
		//write output file
		outputfd << "Case #" << i + 1 << ": ";
		if(poss == N){
			outputfd << note << endl;
		}
		else{
			outputfd << "NO" << endl;
		}
	}

	cout << endl;
	
	inputfd.close();
	outputfd.close();
	return 0;
}

/*
int maxVal(const int val[], const int size, int& index, int& max){
	int temp = 0;
	int r = 0;
	for(int i =0; i < size; i++){
		if(temp == val[i])
			r = 1;
		if(temp < val[i]){
			temp = val[i];
			index = i;
		}

	}
	return r;
}
*/
void SelectionSort(unsigned long A[], int length)
{
    int i, j, min, minat;
	for(i = 0; i<(length-1); i++)
	{
		minat = i;
		min = A[i];

      for(j = i+1;j < length; j++) //select the min of the rest of array
	  {
		  if(min > A[j])   //ascending order for descending reverse
		  {
			  minat = j;  //the position of the min element 
			  min = A[j];
		  }
	  }
	  int temp = A[i];
	  A[i] = A[minat];  //swap 
	  A[minat]=temp;	
	}
}//end selection sort