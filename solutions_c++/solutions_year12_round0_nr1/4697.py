#include<iostream>
#include<conio.h>
#include<string>
#include<xstring>
#include<fstream>
#include<sstream>
using namespace std;
void main()
{
	int i=0,j,length,k,x;
	string my_string[3], string1,string2[10000];
	char z;
	string line = "abcdefghijklmnopqrstuvwxyz";
	string code = "yhesocvxduiglbkrztnwjpfmaq";

	ifstream input("a.in");
	ofstream output("a.out");
	if(output == NULL)
	{
		cout<<"can not opent file"<<endl;
	}

	input >> i; 
	cout<<i;
	getline(input,string1);

	for (j = 0; j < i; j++)
	{
		cout<<endl;
		int temp;
		cout << "case #"<<j+1<<": ";
		output << "Case #"<<j+1<<": ";
		getline(input,string1);
		int length = string1.size();

		for (int g = 0; g <= length-1; g++)
		{
			for ( int z = 0; z <= 25; z++)
			{
				if (string1[g] == line[z])
				{
					output<<code[z];
				}
			}
			if ( string1[g] == ' ')
			{
				output<<" ";
			}
		
		}
	output << endl;
	}
	
	cout<<endl;
	
	input.close();
	output.close();

	getch();


}
