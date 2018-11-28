//============================================================================
// Name        : SquareTiles.cpp
// Author      : m1cRo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <sstream>
using namespace std;

std::string solveTest(FILE* fp){
	unsigned int linesNumber=0;
	unsigned int rowsNumber=0;
	fscanf(fp, "%d %d\n",&linesNumber,&rowsNumber);
	std::vector< std::vector<char> > image;
	image.resize(linesNumber);
	for(unsigned int i=0;i<linesNumber;i++){
		image[i].resize(rowsNumber);
	}

	for(unsigned int i=0;i<linesNumber;i++){
		for(unsigned int j=0;j<rowsNumber;j++){
			char ch;
			fscanf(fp,"%c",&ch);
			image[i][j]=ch;
		}

		fscanf(fp, "\n");
	}

	for(unsigned int i=0;i<image.size();i++){
		for(unsigned int j=0;j<image[i].size();j++){
			if(image[i][j]=='#'){
				if(j==image[i].size()-1 || i==image.size()-1){
					return "Impossible\n";
				}else{
					if(image[i][j+1]=='#' && image[i+1][j+1] && image[i+1][j]){
						image[i][j]='/';
						image[i][j+1]='\\';
						image[i+1][j+1]='/';
						image[i+1][j]='\\';
					}else{
						return "Impossible\n";
					}
				}
			}
		}
	}

	std::string result;
	for(unsigned int i=0;i<image.size();i++){
		for(unsigned int j=0;j<image[i].size();j++){
			result+=image[i][j];
		}

		result+='\n';
	}

	return result;
}

int main() {
	FILE* fp=fopen("test.txt","r");
	if(fp==NULL){
		return -1;
	}

	unsigned int numOfTestCases=0;
	fscanf(fp, "%d", &numOfTestCases);
	for(unsigned int i=0;i<numOfTestCases;i++){
		std::string result=solveTest(fp);
		printf("Case #%d:\n", i+1);
		printf("%s",result.c_str());
	}

	fclose(fp);
	return 0;
}
