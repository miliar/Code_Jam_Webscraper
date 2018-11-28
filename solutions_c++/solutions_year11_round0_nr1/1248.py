// turn_left.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <set>
#include <map>
#include <vector>


using namespace std;

int t;
vector< vector< pair<char, int> > >  input;

ofstream fout("output.txt");
ifstream fin("A-large.in");

void get_input()
{

	fin >> t;

	int n;
	char c;
	int num;
	int i, j;

	for(i = 0 ; i < t; i++)
	{
		fin >> n;
		vector< pair<char, int>  > item;
		for(j = 0 ; j < n; j++)
		{
			fin >> c;
			fin >> num;
			pair<char ,int> p(c, num);
			item.push_back(p);
		}

		input.push_back(item);
	}


}


int doit(vector<pair<char, int> >  item)
{
	int i;
	int pos1, pos2;
	int t, t1, t2;

	pos1 = pos2 = 1;

	t1 = 0; 
	t2 = 0;
	t = 0;

	vector< pair<char, int> >::iterator it;

	char past = (*(item.begin())).first;

	for(it = item.begin(); it != item.end(); it++)
	{
		char c;
		int num;
		c = (*it).first;
		num = (*it).second;
		int delt;

		if(c == 'O')
		{
			delt = num - pos1;
			if(delt < 0)
				delt = delt * (-1);

			t1 += delt + 1;

			if(past != c && t1 <= t2)
				t1 = t2 + 1;

			pos1 = num;	
		}
		else
		{
			delt = num - pos2;
			if(delt < 0)
				delt = delt * (-1);

			t2 += delt + 1;

			if(past != c && t2 <= t1)
				t2 = t1 + 1;

			pos2 = num;
		}

		past = c;
	}

	if(t1 > t2)
		return t1;
	else
		return t2;

}

int main(int argc, _TCHAR* argv[])
{
	vector< vector< pair<char, int> > > ::iterator it;
	int result;
	int i = 1;

    get_input();

	for(it = input.begin(); it != input.end(); it++)
	{
		result = doit(*it);
		fout<<"Case #"<<i<<": "<<result<<endl;
		i++;
	}
	
	return 0;
}

