/*
 * fmain.cpp
 *
 *  Created on: 2009-9-13
 *      Author: sunguoyang07
 */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	assert(fin);
	assert(fout);

	int T, cas=1;
	fin>>T;

	string str;
	while(T--)
	{
		long long sum=1;
		//main process
		fin>>str;
		if (str.size() > 1)
		{
			sum=0;
			set<char> charset;
			for(int i=0; i < str.length(); i++)
				charset.insert(str[i]);
			int base=charset.size();
			if(base==1)
				base++;
			map<char, int> charmap;

			charmap[str[0]]=1;
			int j;
			for(j=1; j < str.length() && (str[j] == str[0]); j++)
				;
			if (j < str.length())
				charmap[str[j]]=0;

			int count=2;

			for(int i=0; i < str.length(); i++)
			{
				if (charmap.find(str[i]) == charmap.end())
					charmap[str[i]]=count++;
				sum=sum * base + charmap[str[i]];
			}
		}
		fout<<"Case #"<<cas++<<": "<< sum <<endl;
	}

	fin.close();
	fout.close();

	return 0;
}
