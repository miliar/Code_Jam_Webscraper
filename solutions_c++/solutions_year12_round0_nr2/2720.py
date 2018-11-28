#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cctype>
#include <algorithm>

std::map<char, char> charMap;
std::map<int, std::string> lines;

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

void parseLine(int lineNumber, const std::string& line){
	std::stringstream lineStream(line);
	int result = 0;
	int numberOfGooglers = 0;
	int numberOfSurprises = 0;
	int delimiter = 0;
	lineStream >> numberOfGooglers;
	lineStream >> numberOfSurprises;
	lineStream >> delimiter;
	std::vector<int> scores;
	for( int i = 0; i < numberOfGooglers; i++){
		int score = 0;
		lineStream >> score;
		scores.push_back(score);
	}
	
	std::sort(scores.begin(), scores.end());
	std::reverse(scores.begin(), scores.end());
	std::vector<int>::iterator it;
	for( it = scores.begin(); it != scores.end(); it++){
		int res = *it / 3;
		int mod = *it % 3;
		
		if( res < delimiter ){
			if( mod == 1 ){
				res++;
			}else if( mod == 2){
				if( res == delimiter - 2 && numberOfSurprises > 0 ){
					res+=2;
					numberOfSurprises--;
				}else if( res == delimiter-1){
					res++;
				}
			}else{
				if( res == delimiter -1 && numberOfSurprises > 0 && res > 0 ){
					res++;
					numberOfSurprises--;
				}
			}
		}
		
		if( res >= delimiter ){
			result++;
		}
	}
	
	std::cout << "Case #" << lineNumber+1 <<": " << result << std::endl;
}