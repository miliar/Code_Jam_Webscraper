#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int stringToInt(string testCase);
int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("a.out");
	string original = "abcdefghijklmnopqrstuvwxyz";
	string encrypted = "ynficwlbkuomxsevzpdrjgthaq";
	string C;
	getline (cin,C);
	int c = stringToInt(C);
	for (int i = 1; i <= c; i++)
	{
		string temp;
		getline(cin,temp);
		string output = "";
		for (int j = 0; j < temp.size(); j++)
		{
			if (temp[j] == ' ')
				output += ' ';
			else
			{
				output += original[encrypted.find(temp[j])]; 
			}
		}
		cout << "Case #" << i << ": " << output << endl;
	}
	return 0;
}

int stringToInt(string testCase)
{
	int result = 0;
	for (int i = 0; i < testCase.size(); i++)
	{
		result *= 10;
		result += (testCase[i]-'0');  
	}
	return result;
}