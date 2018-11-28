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
#include <fstream>
#include <list>

int main(void) {
	std::ifstream inputFile;
	int test_cases =0;
	std::string line;
	std::string result ="";

	inputFile.open("input.txt");
    inputFile >> test_cases ;
    std::getline(inputFile,line);

    std::string letters = "yhesocvxduiglbkrztnwjpfmaq";

    for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){
		std::getline(inputFile,line);
		result = "";

		for(int i = 0; i< line.length();i++){
			if (line[i] == ' ')
				result = result + " ";
			else
				result = result + letters[line[i] - 'a'];
		}
		std::cout << "Case #" << cases_executed << ": " << result  << std::endl;
	}

    inputFile.close();
    return 1;
}
