// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
#include <map>
#include <set>
using namespace std;
ifstream in("B-large.in");
ofstream out("out.txt");

map<pair<char,char>,char> reglas;
set<pair<char,char>> opuestos;
string texto;

void Solve()
{
/**leo letra por letra, si cumple regla remplazo y sinio chequeo toto 
*/
	map<char,int> allChars;
	string res;
	for(int i = 0;i<texto.size();++i)
	{
		if(res.empty())
		{
			res.push_back(texto[i]);
			allChars[texto[i]]++;
		}
		else
		{
			///Chequeamos reduccion
			map<pair<char,char>,char>::iterator it = reglas.find(pair<char,char>(res[res.size()-1],texto[i]));
			if(it != reglas.end())
			{///Reduce
				allChars[res[res.size()-1]]--;
				assert(allChars[res[res.size()-1]] >= 0);
				res[res.size()-1] = it->second;
			}
			else
			{///queda
				res.push_back(texto[i]);
				allChars[texto[i]]++;
				map<char,int>::iterator itAll;
				for(itAll = allChars.begin();!allChars.empty() && itAll != allChars.end();)
				{
					if(itAll->second > 0 && opuestos.find(pair<char,char>(texto[i],itAll->first)) != opuestos.end())
					{
						allChars.clear();
						res.clear();
					}
					else
						++itAll;
				}
			}
		}
	}

	out << "[";
	for(int i = 0;i < res.size();++i)
	{
		if(i != 0)
			out << ", ";
		out << res[i];
	}
	out << "]";
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	in >> T;
	for(int i = 0;i<T;++i)
	{
		int rules;
		in >> rules;
		reglas.clear();
		opuestos.clear();
		texto.clear();
		for(int m = 0;m < rules;++m)
		{
			string rr;
			in >> rr;
			reglas[pair<char,char>(rr[0],rr[1])] = rr[2];
			reglas[pair<char,char>(rr[1],rr[0])] = rr[2];
		}

		int op;
		in >> op;
		for(int m = 0;m < op;++m)
		{
			string rr;
			in >> rr;
			opuestos.insert(pair<char,char>(rr[0],rr[1]));
			opuestos.insert(pair<char,char>(rr[1],rr[0]));
		}
		in >> op;
		in >> texto;

		out << "Case #" << (i+1) << ": ";
		Solve();
		out << endl;
	}
	return 0;
}

