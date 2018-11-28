#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

long test,tcounter;
long cLength, oLength, len;
vector<string> combineList;
vector<string> opposeList;



char canCombine(char a, char b)
{
	for(long i=0;i<cLength;i++)
	{
		string str = combineList[i];
		if( (str[0]==a && str[1]==b) ||
			(str[0]==b && str[1]==a) )
			return str[2];			
	}
	return 0;
}

bool isOpposed(string stra)
{
	char a = stra[stra.length()-1];
	for(long j=0;j<stra.length()-1;j++)
	{
		char b = stra[j];

		for(long i=0;i<oLength;i++)
		{
			string str = opposeList[i];
			if( (str[0]==a && str[1]==b) ||
				(str[0]==b && str[1]==a) )
				return true;
		}
	}

	return false;
}

int main()
{
    SetInputFile();	
	char c;
	string str;

	cin >> test;
	tcounter = 1;
	while(test--)
	{
		combineList.clear();
		opposeList.clear();

		cin >> cLength;
		while(cLength--)
		{
			cin >> str;
			combineList.push_back(str);
		}
		cLength = combineList.size();
		cin >> oLength;
		while(oLength--)
		{
			cin >> str;
			opposeList.push_back(str);
		}
		oLength = opposeList.size();



		int index = 0;
		string str, output;
		cin >> len >> str;

		output = str[index++];
		while(index < len)
		{
			char c = str[index++];
			output += c;
			while(true){
				c = canCombine(output[output.size()-1], output[output.size()-2]);
				if(c!=0)
				{
					output.erase(output.size()-2,2),
					output += c;
				}
				else break;
			}

			if(isOpposed(output))
				output = "";
			
		}


		cout << "Case #" << tcounter++ << ": [";

		for(int j=0;j<output.size();j++)
		{
			if(j==0) cout << output[j];
			else cout << ", " << output[j];
		}

		cout << "]" << endl;

	}


    return 0;
}
