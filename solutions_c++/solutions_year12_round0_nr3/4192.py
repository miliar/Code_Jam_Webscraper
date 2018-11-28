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
#include <set>


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

	int powers[30];
	for(int a=0; a<30; ++a){
		powers[a]  = pow(10.f,a);
	}
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
		   std::set<std::pair<int,int>> results;
		   int beg;
		   int end;
		   int number;
		   iss >> beg;
		   iss >> end;

		   
		   int l = ((int)log10((float)beg))+1;
		   if(l>1) {
			   for(int i=beg; i<=end; ++i) {
				   l = ((int)log10((float)beg))+1;

				   for(int k =1; k<l; ++k) {
					   int p = powers[k];
					   int q = (i/p);
					   int r = i%p;

					   int i2= r*powers[l-k] +q;

					   if(i>=beg && i<i2 && i2 <= end) {
						   
						   results.insert(std::make_pair(i,i2));
					   }

				   }

			   }
		   }
		   std::cout << "Case #"<< i<<": "<< results.size() <<std::endl;
		   myfile << "Case #"<< i<<": "<< results.size() <<std::endl;

	   };


	

  myfile.close();
  return 0;
}

