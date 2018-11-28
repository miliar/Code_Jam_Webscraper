#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream myfile;
	
	myfile.open (argv[1]);
	 if(!myfile) { // file couldn't be opened
	 cerr << "Error: file could not be opened" << endl;
	 exit(1);
	 }
	 int no_case;	
	 
	 myfile >> no_case;
	 
	map<char,char> char_map;
	
	char_map.insert(pair<char,char> ('y','a'));
	char_map.insert(pair<char,char> ('n','b'));
	char_map.insert(pair<char,char> ('f','c'));
	char_map.insert(pair<char,char> ('i','d'));
	char_map.insert(pair<char,char> ('c','e'));
	char_map.insert(pair<char,char> ('w','f'));
	char_map.insert(pair<char,char> ('l','g'));
	char_map.insert(pair<char,char> ('b','h'));
	char_map.insert(pair<char,char> ('k','i'));
	char_map.insert(pair<char,char> ('u','j'));
	char_map.insert(pair<char,char> ('o','k'));
	char_map.insert(pair<char,char> ('m','l'));
	char_map.insert(pair<char,char> ('x','m'));
	char_map.insert(pair<char,char> ('s','n'));
	char_map.insert(pair<char,char> ('e','o'));
	char_map.insert(pair<char,char> ('v','p'));
	char_map.insert(pair<char,char> ('z','q'));
	char_map.insert(pair<char,char> ('p','r'));
	char_map.insert(pair<char,char> ('d','s'));
	char_map.insert(pair<char,char> ('r','t'));
	char_map.insert(pair<char,char> ('j','u'));
	char_map.insert(pair<char,char> ('g','v'));
	char_map.insert(pair<char,char> ('t','w'));
	char_map.insert(pair<char,char> ('h','x'));
	char_map.insert(pair<char,char> ('a','y'));
	char_map.insert(pair<char,char> ('q','z'));
	char_map.insert(pair<char,char> (' ',' '));


	string* line = new string[no_case];
	string* output= new string[no_case];
	myfile.ignore(100, '\n');
	for (int i = 0; i < no_case; i++){
		getline (myfile,line[i]);
		output[i].resize(line[i].size());
		for (int j = 0; j < line[i].size();j++){
		output[i].at(j) = char_map[line[i].at(j)];
		}
		cout<< "Case #"<<i+1<<": "<<output[i]<<endl;
	}
}
 
