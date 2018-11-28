// codejam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

char  combine [36*3];
char  opposed [28*3];
char squence [100];
char resultSqu [100];
int curResultLength = 0;
int C, D, N;

bool IsCombine(char pre, char cur, char & res);
bool IsOpposedWithAny(char cur, char & opposedChar);

int main(int argc, char* argv[])
{
	ifstream infile;
	infile.open("in.txt", ios::in);
	ofstream outfile;
	outfile.open("out.txt", ios::out | ios::trunc);
	int T = 0;
	infile>>T;
	int test = 0;
	while(++test <= T)
	{
		C = 0, D = 0, N = 0, curResultLength = 0;
		infile>>C;
		int i = 0, j = 0;
		if(C != 0)
		{
			while(i < C)
			{
				infile.ignore();
				infile>>combine[i]>>combine[i+1]>>combine[i+2];
				i += 3;
			}
		}
		infile>>D;
		if(D != 0)
		{
			i = 0;
			while(i < D)
			{
				infile.ignore();
				infile>>opposed[i]>>opposed[i+1];
				i += 2;
			}
		}
		infile>>N;
		infile.ignore();
		for(i = 0; i < N; ++i)
			infile>>squence[i];		
		
		for(i = 0; i < N; ++i)
		{
			char ch = squence[i];
			if(curResultLength == 0)			
			{
				resultSqu[0] = ch;
				++curResultLength;
			}else{
				char ch1;
				if(IsCombine(resultSqu[curResultLength - 1], ch, ch1))
				{
					resultSqu[curResultLength - 1] = ch1;
				}else if(IsOpposedWithAny(ch, ch1))
				{
					int loc = 0;
					bool f = false;
 					for(loc = curResultLength - 1; loc >= 0; --loc)
					{
						if(resultSqu[loc] == ch1)
						{
							curResultLength = 0;
							f = true;
							break;
						}
					}
					if(!f)
					{
						resultSqu[curResultLength] = ch;
						++curResultLength;
					}
				}else{
					resultSqu[curResultLength] = ch;
					++curResultLength;
				}
			}
		}
		outfile<<"Case #"<<test<<": [";
		for(j = 0; j < curResultLength; ++j)
		{
			if(j != curResultLength - 1)
				outfile<<resultSqu[j]<<", ";
			else
				outfile<<resultSqu[j];
		}
		
		outfile<<"]"<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

bool IsCombine(char pre, char cur, char & res)
{
	int length = C * 3;
	for(int i = 0; i < length; i += 3)
	{
		if((combine[i]==pre && combine[i+1]==cur) || (combine[i]==cur && combine[i+1]==pre))
		{
			res = combine[i+2];
			return true;
		}
	}
	return false;
}

bool IsOpposedWithAny(char cur, char & opposedChar)
{
	int length = D * 2;
	for(int i = 0; i < length; i += 2)
	{
		bool f = false;
		if(opposed[i] == cur)
		{
			opposedChar = opposed[i+1];
			f = true;
		}else if(opposed[i+1] == cur)
		{
			opposedChar = opposed[i];
			f = true;
		}
		if(f)
			return true;
	}
	return false;
}