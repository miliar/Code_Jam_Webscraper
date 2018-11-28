#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	string lut = "yhesocvxduiglbkrztnwjpfmaq";
	int N, z;
	//ifstream infile("A-small-attempt0.in");
	cin>>N;
	char temp[101];
	cin.getline(temp, 101);
	for(int i=0; i<N; i++)
	{
		cin.getline(temp, 101);
		string input(temp);
		string output;
		output.resize(input.length());
		for(int i=0; i<input.length(); i++)
		{
			if(input[i] == ' ')
				output[i] = ' ';
			else
				output[i] = lut[input[i]-'a'];
		}
		cout<<"Case #"<<i+1<<": "<<output<<endl;
	}
}

