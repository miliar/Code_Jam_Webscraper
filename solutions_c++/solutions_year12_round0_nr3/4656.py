#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stdio.h"
#include <math.h>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include<fstream>
#include <list>

template <class T>
inline std::string to_stringM(const T& t) {
std::stringstream ss;
ss << t;
return ss.str();
}

bool is_valid_recicled(long A, long B, long number, std::string str_eval){
long evaluate = atol(str_eval.c_str());

	if (evaluate < A)
		return false;
	if (evaluate > B)
		return false;
	if (number == evaluate)
		return false;
	if (str_eval.c_str()[0] =='0')
		return false;
return true;
}

void add_possi(std::string number,long possi[]){
	for(int i=0;i<9;i++){
		if (possi[i] == 0)
			possi[i] = atol(number.c_str());
		if (possi[i] == atol(number.c_str()))
			return;
	}
return;
}

void calculate_possibilities(std::string str_number,long possi[]) {
	int len = str_number.length();

	for(int x=0;x<9;x++)
	   possi[x]=0;

	for(int i=1;i<(len); i++){
		std::string aux = str_number.substr(len-i,len-1) + str_number.substr(0,len-i);
		add_possi(aux,possi);
		//std::cout << "Calculate: " << aux << std::endl;
	}

return;
}

long count_possibilities(long A, long B, long number){
	long ret=0;
	std::string str_num = to_stringM(number);
	long possi[9];

	calculate_possibilities(str_num,possi);

	for(int i=0;possi[i]!=0;i++){
		std::string aux = to_stringM(possi[i]);
		if (is_valid_recicled(A,B,number,aux))
			ret++;
	}

return ret;
}

int main(void) {
	std::ifstream inputFile;
	int test_cases =0;

	inputFile.open("input.txt");
    inputFile >> test_cases ;

	for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
    	long A,B;
    	long result = 0;
    	inputFile >> A;
    	inputFile >> B;

    	for(long i = A;i<=B;i++){
    		result = result + count_possibilities(A,B,i);
    	}

		std::cout << "Case #" << cases_executed << ": " << result/2  << std::endl;
	}

    inputFile.close();
    return 1;
}
