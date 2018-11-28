#include <iostream>
#include <fstream>
#include <string>
#include <iostream>
#include <set>
#include <deque>
#include <algorithm>
#include <bitset>
#include <functional>
#include <stack>
#include <numeric>
#include <sstream>
#include <utility>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cassert>
#include<vector>
#include <fstream>
using namespace std;

int main () 
{
pair<char,char>* pairs = new pair<char,char>[26];
	pairs[0].first = 'a';pairs[0].second = 'y';
	pairs[1].first = 'b';pairs[1].second = 'h';
	pairs[2].first = 'c';pairs[2].second = 'e';
	pairs[3].first = 'd';pairs[3].second = 's';
	pairs[4].first = 'e';pairs[4].second = 'o';
	pairs[5].first = 'f';pairs[5].second = 'c';
	pairs[6].first = 'g';pairs[6].second = 'v';
	pairs[7].first = 'h';pairs[7].second = 'x';
	pairs[8].first = 'i';pairs[8].second = 'd';
	pairs[9].first = 'j';pairs[9].second = 'u';
	pairs[10].first = 'k';pairs[10].second = 'i';
	pairs[11].first = 'l';pairs[11].second = 'g';
	pairs[12].first = 'm';pairs[12].second = 'l';
	pairs[13].first = 'n';pairs[13].second = 'b';
	pairs[14].first = 'o';pairs[14].second = 'k';
	pairs[15].first = 'p';pairs[15].second = 'r';
	pairs[16].first = 'q';pairs[16].second = 'z';
	pairs[17].first = 'r';pairs[17].second = 't';
	pairs[18].first = 's';pairs[18].second = 'n';
	pairs[19].first = 't';pairs[19].second = 'w';
	pairs[20].first = 'u';pairs[20].second = 'j';
	pairs[21].first = 'v';pairs[21].second = 'p';
	pairs[22].first = 'w';pairs[22].second = 'f';
	pairs[23].first = 'x';pairs[23].second = 'm';
	pairs[24].first = 'y';pairs[24].second = 'a';
	pairs[25].first = 'z';pairs[25].second = 'q';

	int testCases;
	ifstream fin("A-small-attempt4.in");
	ofstream fout("A.out");
	vector<string> output;
	string input,outputTemp;
		fin>>testCases;
		getline(fin,outputTemp);
		outputTemp = "";
	if (fin.is_open())
	{
	while (fin.good())
	{
	  getline (fin,input);
	  for(int i=0;i<input.size();i++)
	  {
			outputTemp+=' ';
			if (input[i] == ' ') 
			  outputTemp[i] = ' ';
			else
			{
				for(int k=0;k<26;k++)
				{
					if(pairs[k].first == input[i])
					{
						outputTemp[i] = pairs[k].second;
						break;
					}
				}
			}
	  }
			output.push_back(outputTemp);
			outputTemp.clear();
	}
	}
	for(int i=0;i<output.size()-1;i++)
	{
		fout << "Case #" << (i+1) << ": " << output[i];
		if(i<output.size()-2) fout<<endl;
	}
	return 0;
}