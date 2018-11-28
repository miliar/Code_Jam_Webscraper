#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>

const char r[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 
					'k', 'r',  'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'}; 

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int testnum;
	in >> testnum;

	string p;
	getline(in, p);


	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		string s;
		getline(in, s);

		int l = s.length();
		
		for (int i = 0; i < l; i++)
		{
			if (s[i] >= 'a' && s[i] <= 'z')
				s[i] = r[s[i] - 'a'];
		}


		out << "Case #" << testcase << ": " << s << endl;
	}
	return 0;
}

