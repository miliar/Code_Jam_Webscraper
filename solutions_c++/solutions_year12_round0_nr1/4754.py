#include <string>
#include <fstream>
#include <iostream>
using namespace std;

bool checklength(string Googlerese)
{

	if(Googlerese.length()>100)
	{
		return false;
	}
	else
		return true;
}



int main()
{
	ifstream in_data;
	ofstream out_data;
	int num_of_case;
	string Googlerese;


	in_data.open("input.txt");
	out_data.open("output.txt");

	in_data >> num_of_case;
	getline(in_data,Googlerese);

	if(num_of_case<1 || num_of_case>30)
	{
		out_data << "Invalid Number of Cases" << endl;
		return -1;
	}

	for(int k=0; k < num_of_case; k++)
	{
		out_data << "Case #" << k+1 << ": ";
		getline(in_data,Googlerese);
		if(!checklength(Googlerese))
		{
			out_data << "String is too long" << endl;
			return -2;
		}
		//Translate(Googlerese,out_data);
		int length = Googlerese.length();


	for(int i=0;i<length;i++)
	{
		switch(Googlerese.at(i))
		{
		case 'a':
			out_data << "y";
			break;
		case 'b':
			out_data << "h";
			break;
		case 'c':
			out_data << "e";
			break;
		case 'd':
			out_data << "s";
			break;
		case 'e':
			out_data << "o";
			break;
		case 'f':
			out_data << "c";
			break;
		case 'g':
			out_data << "v";
			break;
		case 'h':
			out_data << "x";
			break;
		case 'i':
			out_data << "d";
			break;
		case 'j':
			out_data << "u";
			break;
		case 'k':
			out_data << "i";
			break;
		case 'l':
			out_data << "g";
			break;
		case 'm':
			out_data << "l";
			break;
		case 'n':
			out_data << "b";
			break;
		case 'o':
			out_data << "k";
			break;
		case 'p':
			out_data << "r";
			break;
		case 'q':
			out_data << "z";
			break;
		case 'r':
			out_data << "t";
			break;
		case 's':
			out_data << "n";
			break;
		case 't':
			out_data << "w";
			break;
		case 'u':
			out_data << "j";
			break;
		case 'v':
			out_data << "p";
			break;
		case 'w':
			out_data << "f";
			break;
		case 'x':
			out_data << "m";
			break;
		case 'y':
			out_data << "a";
			break;
		case 'z':
			out_data << "q";
			break;
		case ' ':
			out_data << " ";
			break;
		default:
			out_data << "Input should contain characters in a-z!" << endl;
			return -3;


			
		}
	}
	out_data << endl;
	}


	return 0;

}