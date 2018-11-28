#include "stdio.h"
#include "stdlib.h"
#include "iostream.h"
#include "fstream.h"

//used with qsort to sort from greatest to least
int compare(const void * a, const void * b){
  return ( *(long int*)b - *(long int*)a );
}


int main(int argv, char argc[]){
	char url[] = "Input";
	ifstream input;
	input.open(url);
	if(!input){
		printf("Error opening input file!\n");
		return 1;
	}
	
	ofstream outputFile;
	outputFile.open("output");
	
	char line[256];
	int numCases;
	
	input.getline(line, 256);
	numCases = atoi(line);
	
	for(int c = 0; c < numCases; c++){
		int lettersPerKey;
		int keys;
		int letters;
		input.getline(line, 256);
		sscanf(line, "%i %i %i", &lettersPerKey, &keys, &letters);
		
		long int freq[letters];
		for(int i = 0; i < letters; i++){
			input >> freq[i];
		}
		input.getline(line, 256);
		
		qsort(freq, letters, sizeof(long int), compare);
		
		int spacesUsed[keys];//lettersPerKey used for each key
		for(int i = 0; i < keys; i++){
			spacesUsed[i] = 1;
		}
		int numPress = 0;
		for(int i = 0; i < letters; i++){
			numPress += spacesUsed[i % keys] * freq[i];
			spacesUsed[i % keys]++;
		}
		
		//output
		int outputCase = c + 1;
		printf("Case #%i: %i\n", outputCase, numPress);
		outputFile << "Case #" << outputCase << ": " << numPress << "\n";
	}
	
	return 0;
}
