/*
 * famin.cpp
 *
 *  Created on: 2009-9-3
 *      Author: sunguoyang07
 *      email: matrixworker@gmail.com
 *  This is the solution for alien language,code jam 2009
 */

#include <string>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

bool doit(string pattern, string text)
{
	unsigned int i=0, j=0;
	while(i<pattern.size() && j<text.size())
	{
		if(pattern[i]=='(')
		{
			bool parenthesis_match = false;
			i++;
			while(pattern[i] != ')')
			{
				if(pattern[i]==text[j])
					parenthesis_match = true;
				i++;
			}
			if(!parenthesis_match)
				return false;
		}
		else
		{
			if(pattern[i] != text[j])
				return false;
		}
		i++;j++;
	}
	if(i == pattern.size() && j == text.size())
		return true;
	return false;
}

int main()
{
	string pattern, text;
	vector<string> patterns;
	vector<string> texts;

	int L,D,N;
	int i;
	ifstream fin("input.txt");
	assert(fin);
	fin>>L>>D>>N;
	for(i=0; i<D; i++)
	{
		fin>>text;
		texts.push_back(text);
	}
	for(i=0; i<N; i++)
	{
		fin>>pattern;
		patterns.push_back(pattern);
	}
	fin.close();

	ofstream fout("output.txt");
	assert(fout);
	vector<string>::iterator pattern_iter;
	vector<string>::iterator text_iter;
	int sum;
	int pattern_no = 1;
	for(pattern_iter = patterns.begin();pattern_iter != patterns.end();pattern_iter++)
	{
		sum=0;
		for(text_iter = texts.begin(); text_iter != texts.end(); text_iter++)
		{
			if(doit(*pattern_iter,*text_iter))
				sum++;
		}
		fout<<"Case #"<<pattern_no++<<": "<<sum<<endl;
	}
	return 0;
}
