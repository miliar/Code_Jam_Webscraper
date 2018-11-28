/* 
 * File:   main.cpp
 * Author: maul
 *
 * Created on 2009. szeptember 3., 0:14
 *
 * //cee - welcome to he---- code jam
 */


#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <iomanip>
//#include <pair>

/*
 * 
 */

const std::string codejam("welcome to code jam");

void count(const std::string & input, unsigned int& counter, unsigned int textpos, unsigned int jampos)
{

	if (textpos == input.length()) return;
	if (jampos == codejam.length()) return;

	//std::cout << textpos << " " << jampos << " " <<input[textpos] << " "<<codejam[jampos] <<" "<<counter <<"\n";

	if (input[textpos] == codejam[jampos]) {
		if (jampos == codejam.length() - 1) {
			counter++;
			counter = counter % 9999;
		}
		count(input, counter, textpos, jampos + 1);
	}

	count(input, counter, textpos + 1, jampos);

}

int main(int argc, char** argv)
{


	unsigned int N;
	std::cin >> N;
	std::cin.get();


	std::cout.setf(std::ios::showpos);
	std::cout.fill('0');
	std::cout.width(4);
	

	for (unsigned int n = 0; n < N; n++) {
		char input[501];

		std::cin.getline(input, 501);
		std::string line(input);

		unsigned int counter = 0;

		count(line, counter, 0, 0);

		std::cout <<  "Case #" << n + 1 << ": ";
		std::cout << std::setw(4) << counter << "\n";
	}


	return(EXIT_SUCCESS);
}

