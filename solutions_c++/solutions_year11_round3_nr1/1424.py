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

#define N 100
#define T 50
#define R 51
#define C 51

using namespace std;

char inputfile[] = "inputfile.txt";
const char outfile[] = "outputfile.txt";

int getscore(char alphabet, char list[]);
int maxVal(const int val[], const int size, int& index, int& max);
//void sortWord(char words[][D], int len);

int main(int argc, char *argv[])
{

	/* Variables */
	ifstream inputfd;
	ofstream outputfd;
	int nCase = 0, r, c;
	char picture[R][C];
	
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
		cout << i << endl;
		int count = 0;


		//read input file
		inputfd >> r;
		inputfd >> c;
		for(int j = 0; j < r; j++){
			for(int k = 0; k < c; k++){
				picture[j][k] = ' ';
			}
		}
		
		cout << r << c << endl;
		for(int j = 0; j < r; j++){
			for(int k = 0; k < c; k++){
				inputfd >> picture[j][k];
				cout << picture[j][k];
				if(picture[j][k] == '#')
					count = count +1;
			}
			cout << endl;
		}

		cout << "count = " << count << endl;
		//process
		bool poss = true;
		if(count == 0){
			outputfd << "Case #" << i + 1 << ": " << endl;
			for(int j = 0; j < r; j++){
				for(int k = 0; k < c; k++){
						outputfd << picture[j][k];
				}
				outputfd << endl;
			}
		}
		else if(count%4 == 0){ // possible
			for(int j = 0; j < r; j++){
				for(int k = 0; k < c; k++){
					if(picture[j][k] == '#' && picture[j][k+1] == '#'){
						if(picture[j+1][k] == '#' && picture[j+1][k+1] == '#'){
							picture[j][k] = '/';
							picture[j][k+1] = '\\';
							picture[j+1][k] = '\\';
							picture[j+1][k+1] = '/';
						}
					}	
				}
			}
			for(int j = 0; j < r; j++){
				for(int k = 0; k < c; k++){
					if(picture[j][k] == '#'){
						poss = false;
						break;
					}
				}
				if(!poss)
					break;
			}
			
			//write output file
			outputfd << "Case #" << i + 1 << ": " << endl;

			if(poss){
				for(int j = 0; j < r; j++){
					for(int k = 0; k < c; k++){
							outputfd << picture[j][k];
					}
					outputfd << endl;
				}
			}else {
				outputfd << "Impossible" << endl;
			}
			
		}else{
			//write output file
			outputfd << "Case #" << i + 1 << ": " << endl;
			outputfd << "Impossible" << endl;

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

void sortWord(char words[][D], int len){
	int i, j, minat;
	char min[D];
	for(i = 0; i<(len-1); i++)
	{
		minat = i;
		strcpy(min, words[i]);

		for(j = i+1; j < len; j++) //select the min of the rest of array
		{
			if(strcmp(min, words[j]) > 0)   //ascending order for descending reverse
			{
				minat = j;  //the position of the min element 
				strcpy(min, words[j]);
			}
		}
		char temp[D];
		strcpy(temp, words[i]);
		strcpy(words[i],words[minat]);  //swap 
		strcpy(words[minat],temp);	
	}
}

*/