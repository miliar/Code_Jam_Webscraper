#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cctype>

std::map<char, char> charMap;
std::map<int, std::string> lines;

void parseLine(int, const std::string& line);

int main(int argc, char **argv) {
	std::ifstream stream("test.txt");
	lines[0] = "our language is impossible to understand";
	lines[1] =  "there are twenty six factorial possibilities";
	lines[2] = "so it is okay if you want to just give upqz";
	for( char ch = 'a'; ch <='z'; ch++ ){
		charMap.insert(std::make_pair<char, char>(ch, ch));
	}
	
	for( char ch = 'A'; ch <='Z'; ch++ ){
		charMap.insert(std::make_pair<char, char>(ch, ch));
	}
	
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

	std::ifstream inputStream("input.txt");
	if( inputStream ){
		char buf[255];
		inputStream.getline(buf, 255);
		std::stringstream numberStream(buf);
		int lines = 0;
		numberStream >> lines;
		int count = 0;
		while( !inputStream.eof()  && count < lines ){
			inputStream.getline(buf, 255);
			std::string line( buf );
			for( int i = 0; i< line.length(); i++){
				line[i] = charMap[line[i]];
			}
			
			std::cout << "Case #"<<count+1 <<": " << line << std::endl;
			count++;
		}
	}
	
    return 0;
}

void parseLine(int lineNumber, const std::string& line){
	for( int pos = 0; pos < line.length(); pos++ ){
		charMap[ line[pos]  ] =  lines[lineNumber][pos];
		charMap[  toupper(line[pos]) ] = toupper( lines[lineNumber][pos] );
	}
}