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


ofstream fout("output.txt");
ifstream fin("B-small-attempt0.in");


string doit(map< pair<char, char>, char>  comb,  map< char, set<char> >   opp, int n, string source );

void get_input()
{
	fin >> t;	 
	int i, j;	

	for(i = 0 ; i < t; i++)
	{
		int c, d, n;
		fin >> c;

		map< pair<char, char>, char>  comb;
		map< char, set<char> >   opp;
		string source;
	 
		for(j = 0 ; j < c; j++)
		{
			char c1,c2,c3;
			fin >> c1 >> c2 >> c3;
			pair<char, char> p1(c1,c2);
			pair<char, char> p2(c2,c1);
			comb[p1] = c3;
			comb[p2] = c3;
		 
		}

		fin >> d;

		for(j = 0; j < d; j++)
		{
			char c4, c5;
			fin >> c4 >> c5;
			opp[c4].insert(c5);
			opp[c5].insert(c4);

		}

		fin >> n >> source;
		string result;		 

	
		result = doit(comb, opp, n, source);

		fout<<"Case #"<<i+1<<": [";
		
		if(result.size() >= 1)
		{
			fout<<result[0];
		}

		for(j = 1 ; j < result.size(); j++)
		{
			fout<<", "<<result[j];
		}
	 

		fout<<"]"<<endl;
	}


}


string doit(map< pair<char, char>, char>  comb,  map< char, set<char> >   opp, int n, string source )
{
	string result;
 

	int i;

	char curr;
	for(i = 0 ; i < n; i++)
	{
		curr = source[i];
		
		result.push_back(curr);
	 
		char last, prev;

		while(result.size() >= 2)
		{
			last = result[result.size() - 1];
			prev = result[result.size() - 2];

			pair<char, char> p(last, prev);
			if(!comb.empty()  && comb.find(p) != comb.end())
			{
			 
				int pos = result.size() - 2;
				result.erase(pos, 2);

				result.push_back(comb[p]);		

				 
				break;
			}
			else
			{
				break;
			}
		}
	

		char oppc;
		if(result.size() >= 2)
		{
			last = result[result.size() - 1];
			if(!opp.empty() && opp.find(last) != opp.end())
			{
				set<char>::iterator jt;
				for(jt = opp[last].begin(); jt != opp[last].end(); jt++)
				{
					 oppc = *jt;
				 
					 if(result.find(oppc) != string::npos)
					 {
					 
						result.clear();	
						
					 }
				}
			}			
		}
	}

	return result;
}
 

int main(int argc, char * argv[])
{
	 

    get_input();

	 
	
	return 0;
}

