#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;


char transtable[] = {'y', 'n', 'f', 'i', 'c', 
						'w', 'l', 'b', 'k', 'u', 'o',
						'm', 'x', 's', 'e', 'v', 'z',
						'p', 'd', 'r', 'j', 'g',
						't', 'h', 'a', 'q'};

char trtable[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x',
					'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
					'z', 't', 'n', 'w', 'j', 'p', 'f', 'm',
					'a', 'q'};

string translate(string input);

int main()
{
	int cases;
	cin >> cases;
	cin >> ws;

	for(int i=0; i<cases; ++i)
	{
		string input;
		getline(cin,input);

		cout << "Case #" << i+1 << ": " << translate(input) << endl;
	}

	return 0;

}

string translate(string input)
{
	string result;

	for(int i=0; i<input.size(); ++i)
	{
		char c = input.at(i);
		if(c == ' ') result.push_back(c);
		else{
			result.push_back(trtable[c-97]);
		}

	}


	return result;
}