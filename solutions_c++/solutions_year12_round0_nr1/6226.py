#include<iostream>
#include <string>
#include <algorithm>
using namespace std;

char trans[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	
	
	int n;
	cin >> n;
	
	string line,translated;
	getline(cin,line,'\n');

	for (int test=1;test<=n;test++)
	{

		line=""; 
		getline(cin,line,'\n');

		for (int i=0;i<line.size();i++)
			if (line[i]!=' ')
				line[i]=trans[line[i]-'a'];

		cout << "Case #" << test << ": " << line << endl;

	}

	//system("pause");
	return 0;
}

