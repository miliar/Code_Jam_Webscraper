// CodeJam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int charNum, wordNum, caseNum;
vector<string> words;
vector<int> result(500);
vector<string> cases;
ofstream out("out.txt");

void parse(string, int);

int main()
{
	string temp;
	freopen("A-large.in","r",stdin);
	cin >> charNum >> wordNum >> caseNum;
	getline(cin,temp);
	for( int i=0; i<wordNum; i++)
	{
		getline(cin,temp);
		words.push_back(temp);
	}
	for( int i=0; i<caseNum; i++)
	{
		getline(cin, temp);
		cases.push_back(temp);
		result[i]=0;
	}
	for( int i=0; i<caseNum; i++)
	parse(cases[i],i);
	
}

void parse(string s, int ca)
{
	vector<vector<char>> a(15);
	int tempSize=0;
	for( int i=0; i<s.size(); i++)
	{

		if( s[i]!='(')
			a[tempSize].push_back(s[i]);
		else
		{
			i++;
			while( s[i]!=')')
			{
				a[tempSize].push_back(s[i]);
				i++;
			}
		}
		tempSize++;
	}
	bool breakout;
	for( int i=0; i<words.size();i++)
	{
		breakout = false;
		for(int j=0; j<charNum; j++)
			if( find(a[j].begin(),a[j].end(),words[i][j]) == a[j].end())
			{
				breakout=true;
				break;				
			}
		if( breakout == false)
			result[ca]++;
	}
	out << "Case #" << ca+1 << ": " << result[ca] <<endl;


}