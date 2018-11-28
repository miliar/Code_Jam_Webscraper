#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>

using namespace std;

int main()
{
	ifstream is("B-small.in");
	ofstream os("B-small.out");

	int T;
	char ret[100];
	is >> T;
	is.getline(ret, 21);
	for(int t = 0; t < T; t++)
	{
		int len;
		int number[21];
		char line[21];
		is.getline(line, 21);
		len = (int)strlen(line);
		for(int i = 0; i < len; i++)
			number[i+1] = (int)(line[i]-48);
		number[0] = 0;
		next_permutation(number, number+len+1);
		

		os << "Case #" << t+1 << ": ";
		if(number[0] == 0)
			for(int i = 1; i < len + 1; i++) 
				os << number[i];
		else
			for(int i = 0; i < len+1; i++) 
				os << number[i];
		os << endl;
	}
	is.close();
	os.close();
	return 0;
}