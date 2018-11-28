// GCJ1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <string>
#include<iostream>
#include<fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>


int find_output(int surp, int look_for, std::vector<int>& list)  {

	int result =0;
	for(int i =0; i<list.size() ; ++i) {

		int score_sum = list[i];

		if(score_sum%3 ==0) {
			
			if(score_sum/3 >= look_for && score_sum/3 >=0)
				++result;
			else {
				if(score_sum/3+1 >= look_for && surp>0 && score_sum/3-1 >=0) {
					--surp;
					++result;
				}
			}

		}
		else if(score_sum%3 ==1) {
			
			if((score_sum-1)/3+1 >= look_for && (score_sum-1)/3-1 >=0)
				++result;

		}

		else {

			if((score_sum-2)/3+1 >= look_for && (score_sum-2)/3-1 >=0)
				++result;
			else {
				if((score_sum-2)/3+2 >= look_for && surp>0 && (score_sum-2)/3 >=0) {
					--surp;
					++result;
				}
			}
		}

		


	}




	return result;
}
int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream inFile ("C:\\file.txt");

	std::vector<std::string> buffer;
	std::vector<std::string> out;
	buffer.push_back(std::string());
	while(std::getline(inFile, buffer.at(buffer.size()-1))) {

		buffer.push_back(std::string());
	} 

	std::ofstream myfile;
	   myfile.open ("C:\\out.txt");
	for(int i =1; i<buffer.size()-1; ++i) {
		std::istringstream iss(buffer[i]);

		int total;
		int supr;
		int number;
		iss >> total;
		iss >> supr;
		iss >> number;
		std::vector<int> scores_sum;
		while (iss)
		{
			scores_sum.push_back(-1);
			iss >> scores_sum.at(scores_sum.size()-1);

		} 
		scores_sum.resize(scores_sum.size()-1);
		_ASSERT(total == scores_sum.size());
		int out = find_output(supr, number, scores_sum);

		myfile << "Case #"<< i <<": " << out << std::endl;
		std::cout << "Case #"<< i <<": " << out << std::endl;

	};


	

  myfile.close();
	return 0;
}

