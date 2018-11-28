// codejamtemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // I/O 
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation
#include <ios>
#include <string>
#include <sstream>
#include <map>
#include <list>
#include <set>

using namespace std;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

void SetOpposed(map<char, set<char>> &opposed, char f, char s)
{
	opposed[f].insert(s);
}

void ProcessCase(int caseIndex, ifstream &inFile, ofstream &outFile)
{
	int C;
	inFile >> C;
	map<pair<char, char>, char> combine;
	for (int i = 0; i < C; i++)
	{
		char first, second, res;
		inFile >> first >> second >> res;
		if (first >= second)
		{// keep it ordered
			char t = first;
			first = second;
			second = t;
		}
		combine[pair<char, char>(first, second)] = res;
	}

	int D;
	inFile >> D;
	map<char, set<char>> opposed;
	for (int i = 0; i < D; i++)
	{
		char first, second;
		inFile >> first >> second;
		SetOpposed(opposed, first, second);
		SetOpposed(opposed, second, first);
	}

	int N;
	inFile >> N;
	list<char> invoke;
	for (int i = 0; i < N; i++)
	{
		char elem;
		inFile >> elem;
		invoke.push_back(elem);
	}

	list<char> elementList;
	map<char, char> elementMap;

	for (char current = invoke.front(); invoke.size() > 0; invoke.size() > 0 ? current = invoke.front() : 0)
	{
		if (elementList.size() == 0)
		{
			elementList.push_back(current);
			elementMap[current] = 1;
			invoke.pop_front();
			continue;
		}
		char last = elementList.back();
		pair<char, char> p;
		if (current >= last)
		{// keep it ordered
			p.first = last;
			p.second = current;
		}
		else
		{
			p.first = current;
			p.second = last;
		}
		char nonBase = combine[p];
		if (nonBase != NULL)
		{
			elementList.pop_back();
			elementList.push_back(nonBase);
			if (elementMap[last] > 0)
				elementMap[last] = elementMap[last] - 1;
		}
		else
		{
			bool cleared = false;
			for (set<char>::iterator it = opposed[current].begin(); it != opposed[current].end(); it++)
			{
				if (elementMap[*it] != NULL)
				{
					elementList.clear();
					elementMap.clear();
					cleared = true;
					break;
				}
			}
			if (!cleared)
			{
				elementList.push_back(current);
				elementMap[current] = elementMap[current] + 1;
			}
		}
		invoke.pop_front();
	}

	outFile << "Case #" << caseIndex << ": [";
	int end = 1;
	for (list<char>::iterator it = elementList.begin(); it != elementList.end(); it++, end++)
	{
		outFile << *it;
		if (end < elementList.size())
		{
			outFile << ", ";
		}
	}
	outFile << "]\n";
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	inFile.open("B-large.in", ios::in);    // open the streams
	outFile.open("B-large.out", ios::out);

	int N; // the number of cases
	inFile >> N;

	for (int i = 0; i < N; i++)
	{
		ProcessCase(i + 1, inFile, outFile);
	}

	inFile.close();   // close the streams
	outFile.close(); 

	return 0;
}
