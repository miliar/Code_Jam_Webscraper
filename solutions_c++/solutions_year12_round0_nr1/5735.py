#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main () {
	ifstream fileIn ("A-small-attempt0.in");
	ofstream fileOut ("A-small-attempt0.out");
	string line;
	getline (fileIn,line);
char old_char[26] =  {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        char new_char[26] =  {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int line_size;
	int casel = 1;
	while(!fileIn.eof()){
	getline (fileIn,line);
	line_size = line.size();
	for(int i=0;i<line_size;i++){
            if (!isspace(line[i])){
		int j = 0;
		while(line[i] != old_char[j])
			j++;
		line[i] = new_char[j];
	}
	}
	if (!fileIn.eof()){
	fileOut<<"Case #"<<casel<<": "<<line<<"\n";
	casel++;}
	}
	fileIn.close();
	fileOut.close();
  return 0;
}

