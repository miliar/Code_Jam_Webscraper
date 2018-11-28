#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

int main(int argc, char** argv){
	if(argc != 2) {
		std::cerr << "No input file given" << std::endl;
		return 1;
	}
	std::string buffer;
	int t;
	std::istringstream istr;
	std::ifstream inputFile;
	inputFile.open(argv[1]);
	
	getline(inputFile, buffer);
	istr.str(buffer);
	istr >> t;
	istr.clear();
	buffer = "";
	
	int i, n, k, position, solution;
	for(i = 0; i < t; ++i) {
		getline(inputFile, buffer);
		position = buffer.find(' ');
		istr.str(buffer.substr(0, position));
		istr >> n;
		istr.clear();
		istr.str(buffer.substr(position+1));
		istr >> k;
		istr.clear();
		buffer = "";
		
		solution = pow(2, n)-1;
		if(solution == (k&solution)) {
			std::cout << "Case #" << i+1 << ": ON" << std::endl;
		}
		else {
			std::cout << "Case #" << i+1 << ": OFF" << std::endl;
		}
	}
	
	inputFile.close();
	
	
	return 0;
}
