#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;


//ifstream ss("input.txt");
//ofstream xx("output.txt");
int main()
{
	int testcases = 0;

	cin >> testcases;
	string str = "";
	bool flag = false;
	for(int nn = 0;nn <=testcases;nn++)
{
	string answer = "";
	getline( cin , str );

	if(flag == false)
	{
		flag =true; 
		continue;
	}
	
	
	for(int j = 0;j<str.length();j++)
	{
		if(str[j] == ' ')
			answer += " ";
		else if(str[j] == 'a')
			answer+="y";
		else if(str[j] == 'b')
			answer+="h";
		else if(str[j] == 'c')
			answer+="e";
		else if(str[j] == 'd')
			answer+="s";
		else if(str[j] == 'e')
			answer+="o";
		else if(str[j] == 'f')
			answer+="c";
		else if(str[j] == 'g')
			answer+="v";
		else if(str[j] == 'h')
			answer+="x";
		else if(str[j] == 'i')
			answer+="d";
		else if(str[j] == 'j')
			answer+="u";
		else if(str[j] == 'k')
			answer+="i";
		else if(str[j] == 'l')
			answer+="g";
		else if(str[j] == 'm')
			answer+="l";
		else if(str[j] == 'n')
			answer+="b";
		else if(str[j] == 'o')
			answer+="k";
		else if(str[j] == 'p')
			answer+="r";
		else if(str[j] == 'q')
			answer+="z";
		else if(str[j] == 'r')
			answer+="t";
		else if(str[j] == 's')
			answer+="n";
		else if(str[j] == 't')
			answer+="w";
		else if(str[j] == 'u')
			answer+="j";
		else if(str[j] == 'v')
			answer+="p";
		else if(str[j] == 'w')
			answer+="f";
		else if(str[j] == 'x')
			answer+="m";
		else if(str[j] == 'y')
			answer+="a";
		else if(str[j] == 'z')
			answer+="q";
	}
	cout << "Case #" << nn << ": " << answer << endl;

}
	return 0;
}