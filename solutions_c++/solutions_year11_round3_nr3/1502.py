//============================================================================
// Name        : PerfectHarmony.cpp
// Author      : m1cRo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>

std::string solveCase(FILE* fp){
	std::string result;
	unsigned int numOfPlayers=0;
	unsigned int lowFreq=0;
	unsigned int highFreq=0;
	if(lowFreq>highFreq){
		unsigned int tmp=lowFreq;
		lowFreq=highFreq;
		highFreq=tmp;
	}

	fscanf(fp, "%d %d %d",&numOfPlayers, &lowFreq, &highFreq);
	std::vector<unsigned int> freqs;
	for(unsigned int i=0;i<numOfPlayers;i++){
		unsigned int freq;
		fscanf(fp,"%d ",&freq);
		freqs.push_back(freq);
	}

	bool failed=false;
	unsigned int validResult=0;
	for(unsigned int i=lowFreq;i<=highFreq;i++){
		failed=false;
		validResult=i;
		for(unsigned int j=0;j<freqs.size();j++){
			int mod=i%freqs[j];
			int mod2=freqs[j]%i;
			if(mod!=0 && mod2!=0){
				failed=true;
				break;
			}
		}

		if(!failed){
			break;
		}
	}

	if(!failed){
		std::stringstream strm;
		strm<<validResult;
		strm>>result;
	}else{
		result="NO";
	}

	return result;
}

int main() {
	FILE* fp=fopen("test.txt", "r");
	if(fp==NULL){
		return -1;
	}

	unsigned int numberOfTests=0;
	fscanf(fp, "%d", &numberOfTests);
	for(unsigned int i=0;i<numberOfTests;i++){
		std::string result=solveCase(fp);
		printf("Case #%d: %s",i+1,result.c_str());
		if(i!=numberOfTests-1){
			printf("\n");
		}
	}

	fclose(fp);
	return 0;
}
