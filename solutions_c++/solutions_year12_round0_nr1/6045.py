#include <iostream>
#include <fstream>

using namespace std;

int main() 
{

ifstream infile("input.txt");
ofstream outfile("translated.txt");

string s;
int numTests;
infile >> numTests;



for(int i = 0; i <= numTests; i++){


	outfile << "Case #" << i << ": ";

	getline(infile,s);
	for(int j = 0; j < s.size(); j++){
		if(s.at(j) == 'a')
			outfile << 'y';
		if(s.at(j) == 'b')
			outfile << 'h';
		if(s.at(j) == 'c')
			outfile << 'e';
		if(s.at(j) == 'd')
			outfile << 's';
		if(s.at(j) == 'e')
			outfile << 'o';
		if(s.at(j) == 'f')
			outfile << 'c';
		if(s.at(j) == 'g')
			outfile << 'v';
		if(s.at(j) == 'h')
			outfile << 'x';
		if(s.at(j) == 'i')
			outfile << 'd';
		if(s.at(j) == 'j')
			outfile << 'u';
		if(s.at(j) == 'k')
			outfile << 'i';
		if(s.at(j) == 'l')
			outfile << 'g';
		if(s.at(j) == 'm')
			outfile << 'l';
		if(s.at(j) == 'n')
			outfile << 'b';
		if(s.at(j) == 'o')
			outfile << 'k';
		if(s.at(j) == 'p')
			outfile << 'r';
		if(s.at(j) == 'q')
			outfile << 'z';	
		if(s.at(j) == 'r')
			outfile << 't';
		if(s.at(j) == 's')
			outfile << 'n';
		if(s.at(j) == 't')
			outfile << 'w';
		if(s.at(j) == 'u')
			outfile << 'j';
		if(s.at(j) == 'v')
			outfile << 'p';
		if(s.at(j) == 'w')
			outfile << 'f';
		if(s.at(j) == 'x')
			outfile << 'm';
		if(s.at(j) == 'y')
			outfile << 'a';
		if(s.at(j) == 'z')
			outfile << 'q';
		if(s.at(j) == ' ')
			outfile << ' ';
		}
		

		outfile <<	endl;
		

	}
			
return 0;	

}
