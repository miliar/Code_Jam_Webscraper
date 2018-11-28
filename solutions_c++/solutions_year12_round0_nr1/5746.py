#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{

	string input = "abcdefghijklmnopqrstuvwxyz";
	string output = "yhesocvxduiglbkrztnwjpfmaq";
	string out = "" , in = "" , in1 = "" , out1 = "";
	int t;
	cin >> t;
	int c = 1;
	while(c <= t)
	{
		in1  = "";
		out1 = "";	
		cin >> in1;
		getline(cin , in);
		
		for(int i = 0;i < in1.length();i++)
		{
			if(in1[i] == ' ')
				out1 += ' ';
			else
			{ 
				for(int j = 0;j < input.length();j++)
				{
					if(in1[i] == input[j])
						out1 += output[j];
				}
			}
		}
		for(int i = 0;i < in.length();i++)
		{
			if(in[i] == ' ')
				out += ' ';
			else
			{ 
				for(int j = 0;j < input.length();j++)
				{
					if(in[i] == input[j])
						out += output[j];
				}
			}
		}
		cout << "Case #" << c << ": " << out1 << out << endl;
		out = "";
		in = "";		
		c++;
	}
}
