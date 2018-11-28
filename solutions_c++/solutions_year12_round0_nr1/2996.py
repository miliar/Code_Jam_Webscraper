#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
using namespace std;


int main(int argv, char** args){
	ifstream in;
	in.open("small.in");
	ifstream sample;
	sample.open("sample.in");
	ofstream out;
	out.open("small.out");
	
	
	string s_in,  s_out;
	
	char map[26];
	for (int i = 0; i < 3; i ++){
		getline(sample, s_in);
		getline(sample, s_out);
		for (int j = 0 ; j < s_in.length(); j ++){
			int index = int( s_in[j] - 'a');
			map[index] = s_out[j];
		}
	}
	map['q'-'a'] = 'z';
	map['z'-'a'] = 'q';
	
	/*
	for ( int i = 0 ; i < 26 ; i ++){

		out << char( i+'a') << "->";
		out << map[i] << endl;
	}*/
	int T;
	in >> T;
	string str;
	getline(in, str);
	for ( int i = 0 ; i < T; i++){
		getline(in, str);
		out << "Case #" << i+1 << ": ";
		for ( int j = 0; j < str.length(); j ++)
			out << map[str[j]-'a'];
		out << endl;
	}
}