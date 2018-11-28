#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <cstring>
#include <math.h>
using namespace std;

#define fin(i,T) for(i = 0; i < T; i++)
#define abs(x) (x<0) ? x : -x

int main()
{
	string line;
	int i;
	
	vector<string> words;
	int T;
	
	vector<char> googlerese;
	vector<char> english;
	
	english.push_back('a');
	english.push_back('b');
	english.push_back('c');
	english.push_back('d');
	english.push_back('e');
	english.push_back('f');
	english.push_back('g');
	english.push_back('h');
	english.push_back('i');
	english.push_back('j');
	english.push_back('k');
	english.push_back('l');
	english.push_back('m');
	english.push_back('n');
	english.push_back('o');
	english.push_back('p');
	english.push_back('q');
	english.push_back('r');
	english.push_back('s');
	english.push_back('t');
	english.push_back('u');
	english.push_back('v');
	english.push_back('w');
	english.push_back('x');
	english.push_back('y');
	english.push_back('z');
	
	googlerese.push_back('y');
	googlerese.push_back('n');
	googlerese.push_back('f');
	googlerese.push_back('i');
	googlerese.push_back('c');
	googlerese.push_back('w');
	googlerese.push_back('l');
	googlerese.push_back('b');
	googlerese.push_back('k');
	googlerese.push_back('u');
	googlerese.push_back('o');
	googlerese.push_back('m');
	googlerese.push_back('x');
	googlerese.push_back('s');
	googlerese.push_back('e');
	googlerese.push_back('v');
	googlerese.push_back('z');
	googlerese.push_back('p');
	googlerese.push_back('d');
	googlerese.push_back('r');
	googlerese.push_back('j');
	googlerese.push_back('g');
	googlerese.push_back('t');
	googlerese.push_back('h');
	googlerese.push_back('a');
	googlerese.push_back('q');
	
	map<char, char> translater;
	
	translater[' '] = ' ';
	
	fin(i,26)
	{
		translater[googlerese[i]] = english[i];
	}
	
	
	ifstream infile("A-small-attempt1.in");
	
	ofstream outfile ("output.txt");
	
	if (infile.is_open() && outfile.is_open()) 
	{
		infile >> T;
		getline(infile, line);
		istringstream iss(line);
		
		fin(i,T)
		{
			getline(infile, line);
			istringstream iss(line);
			
			char *cstr = (char*)line.c_str();
			int c;
			fin(c,line.size())
			{
				cstr[c] = translater[cstr[c]];
			}
			
			string newline(cstr);
			outfile << "Case #" << (i+1) <<": " << newline << endl;
		}
		infile.close();
		outfile.close();
	}

	return 0;
}
