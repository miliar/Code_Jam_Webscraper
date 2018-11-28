#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cctype>
#include <algorithm>
#include <set>

void parseLine(int, const std::string& line);

int main(int argc, char **argv) {
	std::ifstream stream("test.txt");

	if( stream ){
		char buf[255];
		stream.getline(buf, 255);
		std::stringstream numberStream(buf);
		int lines = 0;
		numberStream >> lines;
		int count = 0;
		while( !stream.eof()  && count < lines ){
			stream.getline(buf, 255);
			parseLine(count, buf);
			count++;
		}
	}
	
    return 0;
}

int findNumberOfPermutations( int start, int end, std::set<int> results){
	int sum = 0;
	std::stringstream tmp;
	tmp << start;
	
	std::string value;
	tmp >> value;
	
	for( int i=1; i<value.length(); i++){
		std::string res = value.substr(i, value.length()) + value.substr(0, i);
		std::stringstream tmp2;
		tmp2<< res;
		int val  = 0;
		tmp2 >> val;
		if( val > start && val <= end){
			if(  results.find(val) == results.end() ){
				results.insert(val);
				sum++;
			}
		}
	}
	
	return sum;
}

void parseLine(int lineNumber, const std::string& line){
	std::stringstream lineStream(line);
	int first = 0;
	int second = 0;
	lineStream >> first;
	lineStream >> second;
	
	int sum = 0;
	std::set<int> results;
	for( int i = first; i < second; i++ ){
		sum+= findNumberOfPermutations(i, second, results);
	}
	
	std::cout << "Case #" << lineNumber+1 << ": " << sum << std::endl;
}