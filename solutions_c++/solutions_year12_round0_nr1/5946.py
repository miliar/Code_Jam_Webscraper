#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int main()
{
	int cases;
	int j = 0;

	fstream fin;

	fin.open("input.txt");

	fin >> cases;

	string *input; 
	input = new string [cases + 1];

	for(int i = 0; i < cases + 1; i++)
	{
		getline(fin, input[i]);
	}

	

	for(int i = 0; i < cases + 1; i++)
	{
		j = input[i].length();
		for(int a = 0; a < j; a++)
		{
			if(input[i].at(a) == 'a'){input[i].at(a) = 'y';}
			else if(input[i].at(a) == 'b'){input[i].at(a) = 'h';}
			else if(input[i].at(a) == 'c'){input[i].at(a) = 'e';}
			else if(input[i].at(a) == 'd'){input[i].at(a) = 's';}
			else if(input[i].at(a) == 'e'){input[i].at(a) = 'o';}
			else if(input[i].at(a) == 'f'){input[i].at(a) = 'c';}
			else if(input[i].at(a) == 'g'){input[i].at(a) = 'v';}
			else if(input[i].at(a) == 'h'){input[i].at(a) = 'x';}
			else if(input[i].at(a) == 'i'){input[i].at(a) = 'd';}
			else if(input[i].at(a) == 'j'){input[i].at(a) = 'u';}
			else if(input[i].at(a) == 'k'){input[i].at(a) = 'i';}
			else if(input[i].at(a) == 'l'){input[i].at(a) = 'g';}
			else if(input[i].at(a) == 'm'){input[i].at(a) = 'l';}
			else if(input[i].at(a) == 'n'){input[i].at(a) = 'b';}
			else if(input[i].at(a) == 'o'){input[i].at(a) = 'k';}
			else if(input[i].at(a) == 'p'){input[i].at(a) = 'r';}
			else if(input[i].at(a) == 'q'){input[i].at(a) = 'z';}
			else if(input[i].at(a) == 'r'){input[i].at(a) = 't';}
			else if(input[i].at(a) == 's'){input[i].at(a) = 'n';}
			else if(input[i].at(a) == 't'){input[i].at(a) = 'w';}
			else if(input[i].at(a) == 'u'){input[i].at(a) = 'j';}
			else if(input[i].at(a) == 'v'){input[i].at(a) = 'p';}
			else if(input[i].at(a) == 'w'){input[i].at(a) = 'f';}
			else if(input[i].at(a) == 'x'){input[i].at(a) = 'm';}
			else if(input[i].at(a) == 'y'){input[i].at(a) = 'a';}
			else if(input[i].at(a) == 'z'){input[i].at(a) = 'q';}
			else if(input[i].at(a) == ' '){input[i].at(a) = ' ';}
		}
	}


	
	ofstream fout;
	fout.open("output.txt");
	

	for(int i = 0; i < cases + 1; i++)
	{
		fout << "Case #" << i << ": " << input[i] << endl;
	}

	fin.close();
	fout.close();
	

	return 0;
}