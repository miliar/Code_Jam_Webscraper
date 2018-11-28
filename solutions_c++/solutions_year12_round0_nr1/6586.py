#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>

using namespace std;

char getChar(char c) {
	switch (c)
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
		return 'z';
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
		}
	
}

int main() {
    ofstream out;
    ifstream in;
    
    out.open ("file.out");
    in.open ("file.in");
    
	
    string line;
	int i = 0;
    while(getline(in,line)) 
    {
		i++;
		if (i == 1) continue;
        if(line[0] == '/n') continue;
		
		string str;
		int length = line.length();

		for (int x = 0; x < length; x++)
		{
			str += getChar(line[x]);
		}

		
		cout << "Case #" << i-1 << ": " << str << endl;
		out << "Case #" << i-1 << ": " << str << endl;
    }

	

    system("PAUSE");
    return 0;
}