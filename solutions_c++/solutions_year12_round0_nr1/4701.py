#include<iostream>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;

int toInt(string);
int main()
{
	string input;
	int cases;	
	
	ifstream infile("A-small-attempt0.in",ios::in);
	ofstream outfile("output.txt",ios::out);
	if (infile.fail() || outfile.fail())
	{
		cout <<"Error opening files" <<endl;
		return 1;
	}
	
	getline(infile, input);
	cases = toInt(input);
		
	for(int j=0; j<cases; j++)
	{	
		string output="";
		char c = 'a';
		getline(infile, input);
		for(int i=0; i<input.length(); i++) {
			c = input.at(i);
			switch(c){
				case ' ': output.append(" "); break;
				case 'a': output.append("y"); break; case 'n': output.append("b"); break; 
				case 'b': output.append("h"); break; case 'o': output.append("k"); break;
				case 'c': output.append("e"); break; case 'p': output.append("r"); break;
				case 'd': output.append("s"); break; case 'q': output.append("z"); break;
				case 'e': output.append("o"); break; case 'r': output.append("t"); break;
				case 'f': output.append("c"); break; case 's': output.append("n"); break;
				case 'g': output.append("v"); break; case 't': output.append("w"); break;
				case 'h': output.append("x"); break; case 'u': output.append("j"); break;
				case 'i': output.append("d"); break; case 'v': output.append("p"); break;
				case 'j': output.append("u"); break; case 'w': output.append("f"); break;
				case 'k': output.append("i"); break; case 'x': output.append("m"); break;
				case 'l': output.append("g"); break; case 'y': output.append("a"); break;
				case 'm': output.append("l"); break; case 'z': output.append("q"); break;
			}
		}			
		outfile << "Case #" <<j+1<<": "<< output  <<endl;
	}	
	infile.close();
	outfile.close();
	return 0;
}

int toInt(string s)
{
	stringstream ss;
	ss << s;
	int i;
	ss >> i;
	return i;
}