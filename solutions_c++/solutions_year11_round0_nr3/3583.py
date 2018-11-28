/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Jirapong Manit 2011 <jr_manit@>
 * 
 * candy is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * candy is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <fstream>
#include <string.h>

//large dataset
#define N 1000 

using namespace std;

char inputfile[] = "inputfile.txt";
const char outfile[] = "outputfile.txt";

void SelectionSort(unsigned long A[], int length);
unsigned long SumValue(unsigned long arr[], int high, int low);
int main(int argc, char *argv[])
{
	/* Variables */
	ifstream inputfd;
	ofstream outputfd;
	bool poss = false;
	int nCase = 0, n = 0, nCandy = 0;
	unsigned long candy[N];
	unsigned long result;
	
	
	/********************************************/
	
	if(argc > 1){	   // load the input file
		cout << "Read input from argc '" << argv[1] << "'" << endl;
		strcpy(argv[1], inputfile);	
	}else {
		cout << "No input file, read 'inputfile.txt'" << endl;
	}
	
	inputfd.open(inputfile, fstream::in);
	if(inputfd.fail()){
			cout << "error: cannot read file '" << inputfile << "'\n";
			inputfd.close();
			return -1;
	}
	outputfd.open(outfile);
	if(outputfd.fail()){
			cout << "error: cannot create file '" << outfile << "'\n";
			outputfd.close();
			return -1;
	}

	inputfd >> nCase;	   //read case number
	std::cout << "There is " << nCase << " case." << endl;
	
	for(int n = 0; n < nCase; n++){
		
		unsigned long sumVal = 0;
		unsigned long tempVal1 = 0, tempVal2 = 0;
		int index[N];
		
		inputfd >> nCandy;
		cout << nCandy << endl;
		
		for(int i = 0; i < nCandy; i++){
			inputfd >> candy[i];
			cout << candy[i] << " ";
			sumVal = sumVal^candy[i];
		}
		cout << endl;
		cout << "XOR " << sumVal <<endl;

		if(sumVal != 0)
			poss = false;
		else{
			poss = true;
			SelectionSort(candy, nCandy);
			
			for(int k = nCandy-1; k >= 1; k--){
				tempVal1 = SumValue(candy, nCandy-1, k);
				tempVal2 = SumValue(candy, k-1, 0);

				if(tempVal1^tempVal2 == 0){
					result = tempVal1;
				}
			}
		}

		//write output file
		outputfd << "Case #" << n + 1 << ": ";
		if(poss)
			outputfd << result << endl;
		else 
			outputfd << "NO" << endl;
	}
	
	inputfd.close();
	outputfd.close();
	return 0;
}

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


unsigned long SumValue(unsigned long arr[], int high, int low){
	unsigned long temp = 0;

	for(int i = low; i <= high; i++ ){
		temp = temp + arr[i];
	}
	return temp;
}