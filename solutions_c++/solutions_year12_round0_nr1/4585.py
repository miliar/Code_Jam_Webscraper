#include <iostream>
#include <string>
using namespace std;

int main()
{
	//								abcdefghijklmnopqrstuvwxyz
	char table[27] = "yhesocvxduiglbkrztnwjpfmaq";
	int nCases;
	string input;

	cin >> nCases;
	cin.ignore();
	for (int i=0;i<nCases;i++)
	{
		getline(cin, input);
		for (unsigned int j=0;j<input.length();j++)
			if (input[j] >= 'a' && input[j] <= 'z')
				input[j] = table[input[j]-97];

		cout << "Case #" << i+1 << ": " << input << endl;
	}
	return 0;
}