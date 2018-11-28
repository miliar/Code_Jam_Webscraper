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

//#define PRINT

int main (int argc, char * const argv[]) {
//	std::stringstream input;
//	input<< "3\n"
//	<< "4 O 2 B 1 B 2 O 4\n"
//	<< "3 O 5 O 8 B 100\n"
//	<< "2 B 2 B 1\n";
//	file://localhost/Users/Chen/Downloads/A-large.in.txt
	std::ifstream input("/Users/Chen/Downloads/A-large.in.txt");
	std::ofstream ofile("output2");
	
	
	int inputCount;
	input >> inputCount;
	std::cout<< "inputCount:"<< inputCount<< std::endl;

	std::string result;
	input.get();	// \n
	
	for(int i=0;i< inputCount;i++){
		std::string s;
		std::getline(input, s);
		std::cout<< "line: "<< s<< std::endl;
		
		std::vector< std::string > list = tokenize(s, " ");
		
		int seqCount = atoi(list[0].c_str());
		std::vector< int > color;
		std::vector< int > botton;
		for(int j=0;j< seqCount;j++){
			if(list[1+j*2] == "O"){
				color.push_back(0);
			}else if(list[1+j*2] == "B"){
				color.push_back(1);
			}else{
				assert(false);
			}
			botton.push_back(atoi(list[1+j*2+1].c_str()));
		}

		int suppost[2][seqCount];
		memset(suppost[0], 0, sizeof(int)*seqCount);
		memset(suppost[1], 0, sizeof(int)*seqCount);
		for(int j=0;j< color.size();j++){
			suppost[color[j]][j] = botton[j];
		}
		
//		std::cout<< "suppost --- \n";
//		for(int j=0;j< color.size();j++){
//			std::cout<< "color["<< j<< "] = "<< color[j]<< std::endl;
//			std::cout<< suppost[0][j]<< ','<< suppost[1][j]<< std::endl;
//		}

		for(int j=color.size()-2;j>=0;j--){
			if(suppost[0][j] == 0){
				suppost[0][j] = suppost[0][j+1];
			}
			if(suppost[1][j] == 0){
				suppost[1][j] = suppost[1][j+1];
			}
		}
		if(suppost[0][color.size()-1] == 0){
			suppost[0][color.size()-1] = suppost[0][color.size()-2];
		}
		if(suppost[1][color.size()-1] == 0){
			suppost[1][color.size()-1] = suppost[1][color.size()-2];
		}


//		std::cout<< "suppost --- \n";
//		for(int j=0;j< color.size();j++){
//			std::cout<< suppost[0][j]<< ','<< suppost[1][j]<< std::endl;
//		}

		int pos[2];
		pos[0] = 1;
		pos[1] = 1;

		int j = 0;
		int second = 0;
		while(j < seqCount){
			second++;
#ifdef PRINT
			std::cout<< "sec: "<< second<< std::endl;
#endif
			int p0 = pos[0];
			int p1 = pos[1];
			if(pos[0] < suppost[0][j]){
#ifdef PRINT
				std::cout<< "O move\n";
#endif
				pos[0]++;
			}else if(pos[0] > suppost[0][j]){
#ifdef PRINT
				std::cout<< "O move\n";
#endif
				pos[0]--;
			}
			
			if(pos[1] < suppost[1][j]){
#ifdef PRINT
				std::cout<< "B move\n";
#endif
				pos[1]++;
			}else if(pos[1] > suppost[1][j]){
#ifdef PRINT
				std::cout<< "B move\n";
#endif
				pos[1]--;
			}
			
			if(color[j] == 0){
				if(p0 == suppost[0][j]){
#ifdef PRINT
					std::cout<< "O push\n";
#endif
					j++;
					continue;
				}
			}else{
				if(p1 == suppost[1][j]){
#ifdef PRINT
					std::cout<< "B push\n";
#endif
					j++;
				}
			}
		}
		
/*		
		int walk;
		int second = 0;
//		std::cout<< "color.size() = "<< color.size()<< std::endl;
		for(int j=0;j< color.size();j++){
//			std::cout<< "color["<< j<< "] = "<< color[j]<< std::endl;
//			std::cout<< "botton["<< j<< "] = "<< botton[j]<< std::endl;

			walk = fabs(botton[j] - pos[color[j]]);
			second += walk;
			second++;
//			std::cout<< "second: "<< second<< std::endl;

//			std::cout<< "b-p: "<< color[j]<< ','<< botton[j]<< " - "<< pos[color[j]]<< std::endl;
//			std::cout<< "walk: "<< walk<< std::endl;
			pos[color[j]] = botton[j];
			int other = (color[j]+1)%2;

			walk++;
			if(walk > fabs(pos[other] - suppost[other][j])){
				walk = fabs(pos[other] - suppost[other][j]);
			}

			if(pos[other] > suppost[other][j]){
				pos[other] -= walk;
			}else if(pos[other] < suppost[other][j]){
				pos[other] += walk;
			}
		}
*/		
//		std::cout<< "sec: "<< second<< std::endl;
		ofile.setf(ios::fixed, ios::floatfield);
		ofile.precision(8);

		ofile<< "Case #"<< i+1<< ": "<< second<< endl;
		std::cout<< "Case #"<< i+1<< ": "<< second<< endl;		
	}
    return 0;
}
