//      language.cpp
//      
//      Copyright 2012 Antonio <antonio@antonio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>

char translate(char letter);


using namespace std;


int main(int argc, char** argv)
{
	//Solution : Ugly 1:1 mapping
	char cycles_char[4] = {0};
	int cycles = 0;
	//Start to execute the sequence
	string filename = argv[1];
    //Open the filename
    ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("language.out",ios::out);
	file_inst >> cycles_char;
	cycles = atoi(cycles_char);
    
    string line;
    //cout << "The value of cycles is "<<cycles << endl;
    getline(file_inst, line);//Move to next line
    for(int i = 0; i < cycles ; i++)
	{
		string new_line;
		//Parse a line
		getline(file_inst, line);
		//cout << "My line is " << line;
		//Parse every element of the line
		for(int j = 0; j < line.length() ; j++)
		{
			//cout << "The length is "<<line.length() <<  endl;
			char letter;
			char translated;
			letter = line[j];
			//if( i == 0 && (j == 0 || j == 1))
			//{
			//	cout << "The letter is " << letter << endl;
			//}
			translated = translate(letter);
			new_line.push_back(translated);
		} 
		cout << "Case #" << i << ": " << new_line << endl;
		file_output<<"Case #"<<i+1<<": "<<new_line << endl;
	}
	file_inst.close();
	file_output.close();
	return 0;
}

//Implementation of translate
char translate(char letter)
{
	switch (letter)
	{
		case 'a': 
			return 'y';
			break;
		case 'b': 
			return 'h';
			break;
		case 'c': 
			return 'e';
			break;
			case 'd': 
				return 's';
			break;
		case 'e': 
			return 'o';
		break;
		case 'f': 
			return 'c';
			break;
		case 'g': 
			return 'v';
			break;
		case 'h': 
			return 'x';
			break;
		case 'i': 
			return 'd';
			break;
		case 'j': 
			return 'u';
			break;
		case 'k': 
			return 'i';
			break;
		case 'l': 
			return 'g';
			break;
		case 'm': 
			return 'l';
			break;
		case 'n': 
			return 'b';
			break;
		case 'o': 
			return 'k';
			break;
		case 'p': 
			return 'r';
			break;
		case 'q': 
			return 'z';//Doubt
			break;
		case 'r': 
			return 't';
			break;
		case 's': 
			return 'n';
			break;
		case 't': 
			return 'w';
			break;
		case 'u': 
			return 'j';
			break;
		case 'v': 
			return 'p';
			break;
		case 'w': 
			return 'f';
			break;
		case 'x': 
			return 'm';
			break;
		case 'y': 
			return 'a';
			break;
		case 'z': 
			return 'q';
			break;
		case ' ':
			return ' ';
			break;
		default : 
			cout << "Not recognized input " << endl;
			return 0;
	}
}
