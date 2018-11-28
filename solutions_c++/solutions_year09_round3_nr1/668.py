#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>

using namespace std; 

int main()
{
	fstream infile("A-small-attempt1.in");
	ofstream outfile("Result.txt");


	int t,testCase(1);
	infile >> t;

	for(;testCase <= t ; testCase ++)
	{
		string message;
		infile >> message;

		int base = 2;
		map<char,int> keyMap;

		string::iterator iter = message.begin();

		char firstChar = *iter;		
		keyMap[firstChar] = 1;

		iter ++;

		while(iter != message.end() && *iter == firstChar)
		{
			iter ++;
		}

		if( iter != message.end() )
		{
			keyMap.insert(make_pair(*iter,0));
			iter++;
			while( iter != message.end())
			{
				if(keyMap.count(*iter) == 0)
				{
					keyMap.insert(make_pair(*iter,base++));
				}

				iter ++;
			}
		}

		int length(message.length());
		long long result(0);

		for(long long len = 0 ; len < length ; len ++)
		{

			result += keyMap[message[len]] * pow((double)base,int(length - len  - 1));

		}

		outfile << "Case #" << testCase << ": " << result << endl;

	}

	return 0;
}