#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>

using namespace std;

int arr[26] = {	24, 6, 2, 15, 
				10, -3, 15, 16, 
				-5, 11, -2, -5, 
				-1, -12, -4, 2,
				9, 2, -5, 3,
				-11, -6, -17, -11,
				-24, -9};


int get_number() 
{
	char s[100];
	cin.getline(s, 100);
	if (strlen(s) == 0)
	return 0;
	return atoi(s);
}

int main()
{
	int testcase = get_number();

	//cin >> testcase;

	ofstream file_out("Output.txt");

	for (int i = 0; i < testcase; i++)
	{
		char teststr[200];
		cin.getline(teststr, 200);

		int len = strlen(teststr);

		for (int j = 0; j < len; j++)
		{
			teststr[j] += arr[teststr[j] - 'a'];
		}
	
		file_out << "Case #" << i+1 << ": " << teststr << endl;
	}

	file_out.close();

	return 0;
}