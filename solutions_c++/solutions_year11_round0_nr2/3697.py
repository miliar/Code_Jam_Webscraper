#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <fstream>
#include <assert.h>

using namespace std;

std::vector< std::string > tokenize(const std::string &_str, const std::string &_delim)
{
	std::vector< std::string > result;
	
	char * pch;
	//	printf ("Splitting string \"%s\" into tokens:\n",str);
	
	char *str = strdup(_str.c_str());
	char *delim = strdup(_delim.c_str());
	pch = strtok(str, delim);
	while (pch != NULL)
	{
		result.push_back(pch);
		//		printf ("%s\n",pch);
		pch = strtok (NULL, delim);
	}
	free(str);
	free(delim);
	
	return result;
}


std::string checkOppos(const std::string elements,
					std::vector< std::string > &opposList)
{
	if(elements.length() == 0) return elements;

	std::string result = elements;
	char last = elements[elements.length()-1];
	for(int i=elements.length()-1;i>=0;i--){
//	for(int i=0;i< elements.length()-1;i++){
		char c = elements[i];
		for(int j=0;j< opposList.size();j++){
			if((c == opposList[j][0] && last == opposList[j][1])
			   || (last == opposList[j][0] && c == opposList[j][1]))
			{
				return "";
				std::cout<< "bf del: "<< result<< std::endl;
				result = std::string(result, 0, i);
				std::cout<< "af del: "<< result<< std::endl;
				return result;
				break;
			}
		}
	}
	return result;
}

std::string combine(const std::string invoke,
					std::vector< std::string > &combineList,
					std::vector< std::string > &opposList)
{
	std::string result;
	if(invoke.length() > 0){
		result += invoke[0];
	}
	for(int i=1;i< invoke.length();i++){
		result += invoke[i];
		
		char c0 = result[result.length()-2];
		char c1 = result[result.length()-1];
		bool comb = false;
		for(int j=0;j< combineList.size();j++){
			if((c0 == combineList[j][0] && c1 == combineList[j][1])
			   || (c1 == combineList[j][0] && c0 == combineList[j][1]))
			{
				result = std::string(result, 0, result.length()-2);	// del last 2 char
				result += combineList[j][2];
				comb = true;
				break;
			}
		}
		if(!comb){
			result = checkOppos(result, opposList);
		}
	}
	return result;
}

//#define PRINT

int main (int argc, char * const argv[]) {
//	std::stringstream input;
//	input<< "5\n	\
//	0 0 2 EA\n	\
//	1 QRI 0 4 RRQR\n	\
//	1 QFT 1 QF 7 FAQFDFQ\n	\
//	1 EEZ 1 QE 7 QEEEERA\n	\
//	0 1 QW 2 QW";
//file://localhost/Users/Chen/Downloads/B-small-attempt0.in.txt

	std::ifstream input("/Users/Chen/Downloads/B-small-attempt2.in.txt");
	std::ofstream ofile("output");
	
	
	int inputCount;
	input >> inputCount;
	std::cout<< "inputCount:"<< inputCount<< std::endl;
	
	std::string result;
	input.get();	// \n
	
	for(int c=0;c< inputCount;c++){
		std::string s;
		std::getline(input, s);
		std::cout<< "line: "<< s<< std::endl;
		
		std::vector< std::string > list = tokenize(s, " ");

		int lpos = 0;
		int combineCount = atoi(list[lpos++].c_str());
		std::vector< std::string > combineList;
		for(int j=0;j< combineCount;j++){
			combineList.push_back(list[lpos++]);
		}
		
		int opposCount = atoi(list[lpos++].c_str());
		std::vector< std::string > oppos;
		for(int j=0;j< opposCount;j++){
			oppos.push_back(list[lpos++]);
		}
		
		int invokeCount = atoi(list[lpos++].c_str());
		std::string invoke = list[lpos++].c_str();
		
//		std::cout<< "invoke: "<< invoke<< std::endl;
		
		// -------------------------------------------------		
		std::string combined = combine(invoke, combineList, oppos);
//		std::cout<< "combined: "<< combined<< std::endl;
		
		// -------------------------------------------------
		ofile.setf(ios::fixed, ios::floatfield);
		ofile.precision(8);

//		ofile<< "Case #"<< c+1<< ": "<< second<< endl;
		std::stringstream ss;
		ss<< "Case #"<< c+1<< ": [";
		for(int j=0;j< combined.length();j++){
			if(j>0){
				ss<< ", ";
			}
			ss<< combined[j];
		}
		ss<< "]\n";
		std::cout<< ss.str();
		ofile<< ss.str();
		
	}
    return 0;
}
