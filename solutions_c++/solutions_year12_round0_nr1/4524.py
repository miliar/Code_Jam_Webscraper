#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	char arr1[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	ifstream in("A-small-attempt0.in");
	ofstream out("outfile.txt");
	int num;
	string num2;
	getline(in,num2);
	int  t = atoi(num2.c_str());
	string input;

	for(int i=0; i<t; i++)
	{
		getline(in,input);
		out<<"Case #"<<i+1<<": ";
		for(int j=0; j<input.size(); j++)
		{
			if(input[j]==' ')
				out<<' ';
			else
			{
			int index =int (input[j]-'a');
			out<<arr1[index];
			}
		}
		out<<endl;
	}

	return 0;
}