// string constructor
#include "stdafx.h"
#include <iostream>
#include <string>
#include <conio.h>
#include <fstream>

using namespace std;

int main ()
{
	fstream input;
	fstream output;
	input.open ("A-small.in", fstream::in | fstream::out | fstream::app);
	output.open ("A-small.out", fstream::in | fstream::out | fstream::app);
	int L,D,N;
	int caseN[5000];
	string word[5000];
	string testCase[500];
	input >> L;
	input >> D;
	input >> N;
	for(int i=0;i<D;i++)
	{
		input >> word[i];
	}
	for(int j=0;j<N;j++)
	{
		caseN[j]=0;
		input >> testCase[j];
	}
	for(int k=0;k<D;k++)
	{
		for(int l=0;l<N;l++)
		{
			int res=0;
			char * pch;
			char * cstr;
			cstr = new char [testCase[l].size()+1];
			strcpy (cstr, testCase[l].c_str());
			pch = strtok (cstr,")");
			int count=0;
			int countToken=0;
			while (pch != NULL)
			{
				string token = pch;
				size_t found;
				found=token.find(word[k].at(count));
				if (found!=string::npos)
				{
					res++;
				}
				pch = strtok (NULL, ")");
				count++;
				countToken++;
			}
			if(countToken==1)
			{
				for(int w=0;w<L;w++)
				{
					if (testCase[l].at(w)==word[k].at(w))
					{
						res++;
					}
				}
			}
			if(res>=L)
			{
				caseN[l]++;
			}
		}
	}
	for(int result=0;result<N;result++)
	{
		output << "Case #"<<(result+1)<<": "<<caseN[result] << endl;
	}
	input.close();
	output.close();
	return 0;
}