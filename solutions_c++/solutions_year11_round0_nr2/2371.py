// TaskB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Base
{
	char c1;
	char c2;
	char res;
};

struct Opposed
{
	char c1;
	char c2;
};

bool hasOpposite(vector<Opposed>& opposites, vector<char>& invocations)
{
	char newCh = invocations.at(invocations.size() - 1);
	vector<char> contrary;
	for(vector<Opposed>::iterator it1 = opposites.begin(); it1 != opposites.end(); it1++)
	{
		if(it1->c1 == newCh)
			contrary.push_back(it1->c2);
		else if(it1->c2 == newCh)
			contrary.push_back(it1->c1);
	}
	vector<char>::iterator it = contrary.begin();
	for(; it != contrary.end(); it++)
	{
		vector<char>::iterator found = find(invocations.begin(), invocations.end(), *it);
		if(found != invocations.end())
			return true;
	}
	return false;
}

void Combine(vector<Base>& combinations, vector<char>& invocations)
{
	bool wasCombined = true;
	while(wasCombined)
	{
		wasCombined = false;
		/// Check that we have at least two symbols
		if(invocations.size() < 2)
			return;
		int lastIdx = invocations.size() - 1;
		char ch1 = invocations.at(lastIdx);
		char ch2 = invocations.at(lastIdx - 1);
		for(vector<Base>::iterator it = combinations.begin(); it != combinations.end(); it++)
		{
			Base b = *it;
			if(((b.c1 == ch1) && (b.c2 == ch2)) ||
			   ((b.c1 == ch2) && (b.c2 == ch1)))
			{
				invocations.pop_back();
				invocations.pop_back();
				invocations.push_back(b.res);
				wasCombined = true;
				break;
			}
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("B-large.in");
	ofstream output;
	output.open("B.out");
	if(input.is_open())
	{
		int T;
		input >> T;
		for(int testi = 0;testi < T; testi++)
		{
			int C;
			vector<Base> bases;
			input >> C;
			for(int i = 0; i<C; i++)
			{
				char c = ' ';
				while (c == ' ') 
					input >> c;
				Base b;
				b.c1 = c;
				input >> b.c2;
				input >> b.res;
				bases.push_back(b);
			}
			vector<Opposed> opposed;
			int D;
			input >> D;
			for(int i = 0; i<D; i++)
			{
				char c = ' ';
				while (c == ' ')
					input >> c;
				Opposed o;
				o.c1 = c;
				input >> o.c2;
				opposed.push_back(o);
			}
			int N;
			input>>N;
			output<<"Case #" << testi + 1<<": [";
			vector<char> invocations;
			for(int i = 0; i<N; i++)
			{
				char newSymbol;
				input >> newSymbol;
				invocations.push_back(newSymbol);
				/// Check combinations
				Combine(bases, invocations);
				/// Check opposite
				if(hasOpposite(opposed, invocations))
				{
					invocations.clear();
				}
			}
			vector<char>::iterator it;
			if(!invocations.empty())
			{
				it = invocations.begin();
				output << *it;
				it++;
				for(; it != invocations.end(); it++)
				{
					output<<", ";
					output<<*it;
				}
			}
			output<<"]"<<endl;
		}
		input.close();
		output.close();
	}
	else
	{
		cout<<"Input file not found";
		return 1;
	}
	return 0;
}

