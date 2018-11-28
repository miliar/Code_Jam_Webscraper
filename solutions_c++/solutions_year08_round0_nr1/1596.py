// qual1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>



using namespace std;



#define INF 100000

int fff(vector<string>& const qu, vector<string>const & ser)
{
	map<string, int> prev;
	map<string, int> cur;

	for (int i =0; i< ser.size(); ++i)
		prev[ser[i]] = 0;

	for (int i = 0; i < qu.size(); ++i)
	{
		string q = qu[i];
		int mn = INF;
		for (int j = 0; j < ser.size(); ++j)
		{
			string s = ser[j];
			if (prev[s] != -1)
				mn = min(mn, prev[s]);
		}

		for (int j = 0; j < ser.size(); ++j)
		{
			string s = ser[j];
			if (q == s)
			{
				cur[s] = -1;
				continue;
			}
			if (prev[s] == -1)
			{
				cur[s] = mn +1;
			}
			else
			{
				cur[s] = min(prev[s], mn + 1);
			}
		}

		swap(prev, cur);
	}

	int mn = INF;
	for (int j = 0; j < ser.size(); ++j)
	{
		string s = ser[j];
		if (prev[s] != -1)
			mn = min(mn, prev[s]);
	}
	return mn;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream f("D:/2.txt");

	string s;
	getline(f, s);
	istringstream is(s);
	int TextsCount;
	is >> TextsCount;

	ofstream fout("D:/3.txt");

	for (int test = 0; test < TextsCount; ++test)
	{
		vector<string> servers;
		{
			getline(f,s);
			istringstream is(s);
			int serversCount;
			is >> serversCount;
			for (int serv =0 ; serv < serversCount; ++serv)
			{
				getline(f, s);
				servers.push_back(s);
			}
		}
		vector<string> comands;
		{
			getline(f,s);
			istringstream is(s);
			int comCount;
			is >> comCount;
			for (int com =0 ; com < comCount; ++com)
			{
				getline(f, s);
				comands.push_back(s);
			}
		}
		int res = fff(comands, servers);
		fout << "Case #" << test +1  << ": " << res << endl;
	}

	return 0;
}

