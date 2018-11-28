// prjQ1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>

#pragma warning (disable: 4996)


using namespace std;
vector<string> Token_List;
vector<string> Pattern_List;
vector<string> Pattern_segs;

int nTokenLength;
int nToken;
int nPattern;
int score[512] = {0};

bool IsValid(string token)
{
	for(int i=0; i<nTokenLength; i++)
	{
		if(Pattern_segs[i].length() == 1)
		{
			char t= token.c_str()[i];
			char p = Pattern_segs[i].c_str()[0];
			if(t != p)
				return false;
			continue;
		}
		else
		{
			size_t pos = Pattern_segs[i].find_first_of(token.c_str()[i]);

			if(pos == string::npos)
				return false;
			continue;
		}
	}
	return true;

}	

void compare()
{
	for(int i=0; i<nPattern; i++)
	{
		int segStart = false;
		char segBuf[512];
		int bufUsage = 0;

		string pattern = Pattern_List[i];
		Pattern_segs.clear();

		for(size_t j=0; j<pattern.length(); j++)
		{
			if(pattern.c_str()[j] == '(')
			{
				segStart = true;
				memset(segBuf, 0, 512);
				bufUsage = 0;
				continue;
			}
			if(pattern.c_str()[j] == ')')
			{
				segStart = false;
				string tmp = segBuf;
				Pattern_segs.push_back(tmp);
				continue;
			}

			if(segStart == false)
			{
				char p[2] = {0};
				p[0] = pattern.c_str()[j];
				string tmp = p;
				Pattern_segs.push_back(tmp);
			}
			else
			{
				segBuf[bufUsage] = Pattern_List[i].c_str()[j];
				bufUsage++;
			}
		}

		for(int index=0; index < nToken; index++)
		{
			string token = Token_List[index];
			if(IsValid(token)) 
			{
				score[i]++;
			}
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fptr = NULL;
	fopen_s(&fptr, "D:\\A-large.in", "r");

	fscanf_s(fptr, "%d %d %d\n", &nTokenLength, &nToken, &nPattern);

	for(int i=0; i<nToken; i++)
	{
		char buf[512] = {0};
		fscanf(fptr, "%[^\n]\n", buf);		
		string tmp = buf;
		Token_List.push_back(tmp);
	}

	for(int j=0; j<nPattern; j++)
	{
		char buf[512] = {0};
		fscanf(fptr, "%[^\n]\n", buf);		
		string tmp = buf;
		Pattern_List.push_back(tmp);		
	}
	fclose(fptr);

	compare();

	FILE *ofptr = fopen("D:\\output", "w");
	for(int outindex=0; outindex<nPattern; ++outindex)
	{
		fprintf(ofptr, "Case #%d: %d\n", outindex+1, score[outindex]);
	}
	fclose(ofptr);

	return 0;
}

