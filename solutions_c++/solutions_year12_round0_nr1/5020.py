// GCJ1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <string>
#include<iostream>
#include<fstream>
#include <vector>

char change(char in) {
	switch (in)
{
      case 'a':
                return 'y';
            case 'b':
                return 'h';
            case 'c':
                return 'e';
            case 'd':
                return 's';
            case 'e':
                return 'o';
            case 'f':
                return 'c';
            case 'g':
                return 'v';
            case 'h':
                return 'x';
            case 'i':
                return 'd';
            case 'j':
                return 'u';
            case 'k':
                return 'i';
            case 'l':
                return 'g';
            case 'm':
                return 'l';
            case 'n':
                return 'b';
            case 'o':
                return 'k';
            case 'p':
                return 'r';
            case 'q':
                return 'z';
            case 'r':
                return 't';
            case 's':
                return 'n';
            case 't':
                return 'w';
            case 'u':
                return 'j';
            case 'v':
                return 'p';
            case 'w':
                return 'f';
            case 'x':
                return 'm';
            case 'y':
                return 'a';
            case 'z':
                return 'q';
	}
};
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

			//std::cout << "\n" << buffer[i] << std::endl;

			char* out_char = new char[buffer[i].length() +1];
			char* in_char = new char[buffer[i].length() +1];
			strcpy(in_char, buffer[i].c_str());

			for(int j=0; j<buffer[i].length(); ++j) {
				out_char[j] = change(in_char[j]);
			}
			out_char[buffer[i].length()] = 0;

			out.push_back(out_char);

			std::cout  << "Case #"<< i<<": " << out[i-1] << std::endl;
			 myfile << "Case #"<< i<<": " << out[i-1] << std::endl;
			delete [] out_char;
			delete [] in_char;
	};


	
 
  myfile.close();
	return 0;
}

