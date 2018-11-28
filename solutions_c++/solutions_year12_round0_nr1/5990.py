#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <map>
using namespace std;

string reverser(string s){
	map<char,char> ob;
	ob['a'] = 'y'; ob['b'] = 'h';ob['c'] = 'e'; ob['d'] = 's';ob['e'] = 'o'; ob['f'] = 'c';
	ob['g'] = 'v'; ob['h'] = 'x';ob['i'] = 'd'; ob['j'] = 'u';ob['k'] = 'i'; ob['l'] = 'g';
	ob['m'] = 'l'; ob['n'] = 'b';ob['o'] = 'k'; ob['p'] = 'r';ob['q'] = 'z'; ob['r'] = 't';
	ob['s'] = 'n'; ob['t'] = 'w';ob['u'] = 'j'; ob['v'] = 'p';ob['w'] = 'f'; ob['x'] = 'm';
	ob['y'] = 'a'; ob['z'] = 'q';
	
	string temp = s;
	
	for(int i = 0; i < s.length(); i++){ 
		if(temp[i] != ' ')temp[i] = ob[temp[i]];
	}

	return temp;	
}

int main(){
	ifstream f("A-small-attempt2.in");
	ofstream out("test.txt");

	int iterations;
	string temp, trash;
 
	f >> iterations;
 	
	getline(f,trash);
	for(int i = 1; i <= iterations; i++){
		getline(f,temp);
		out << "Case #" << i << ": " << reverser(temp) << endl;	
	}

}
