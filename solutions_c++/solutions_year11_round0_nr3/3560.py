//============================================================================
// Name        : CandySplittingGoogleCode.cpp
// Author      : m1cRo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

std::string getTestResult(FILE* fp){
	std::vector<unsigned int> values;
	unsigned int numberOfValues=0;
	fscanf(fp, "%d", &numberOfValues);
	for(unsigned int i=0; i< numberOfValues; i++){
		unsigned int value=0;
		fscanf(fp, "%d ", &value);
		values.push_back(value);
	}

	sort(values.begin(), values.end());
	unsigned int sum=0;
	std::vector<unsigned int>::iterator it;
	for(it=values.begin(); it!=values.end();it++){
		sum^=(*it);
	}

	if(sum!=0){
		return "NO";
	}else{
		unsigned int sumI=0;
		for(unsigned int i=0;i<values.size();i++){
			sumI^=values[i];
			unsigned int sumJ=0;
			for(unsigned int j=values.size()-1; j> i; j--){
				sumJ^=values[j];
			}

			if( 0==(sumI^sumJ)){
				unsigned int newSumJ=0;
				for(unsigned int j=values.size()-1; j> i; j--){
					newSumJ+=values[j];
				}

				unsigned int newSumI=0;
				for(unsigned int k=0; k <= i; k++){
					newSumI+=values[k];
				}

				if(newSumI>newSumJ){
					char result[255]={0};
					sprintf(result, "%d", newSumI);
					return result;
				}else{
					char result[255]={0};
					sprintf(result, "%d", newSumJ);
					return result;
				}
			}
		}

		return "YES";
	}
}


int main() {
	FILE* fp=fopen("test.txt","r");
	if(fp==NULL){
		return -1;
	}

	unsigned int numberOfTests=0;
	fscanf(fp, "%d", &numberOfTests);
	for( unsigned int i = 0; i < numberOfTests; i++ ){
		std::string result=getTestResult(fp);
		printf("Case #%d: %s\n", i+1, result.c_str());
	}

	fclose(fp);

	return 0;
}
