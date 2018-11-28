// CodeJam.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>

using namespace std;

void clean(vector<bool>& v )
{
	for ( int i = 0; i < v.size(); i++ )
		v[i] = false;
}

int nswitches(map<string, int>& engines, vector<string>& data)
{
	int nvisit = 0;
	int ndata = data.size();
	int nengines = engines.size();
	int switches = 0;

	vector<bool> visited(nengines, false);

	for ( int i = 0; i < ndata; i++ )
	{
		if ( ! visited[engines[data[i]]] )
		{
			visited[engines[data[i]]] = true;
			nvisit++;
		}

		if ( nvisit >= nengines )
		{
			clean(visited);
			nvisit = 1;
			visited[engines[data[i]]] = true;
			switches++;
		}
	}
	return switches;
}

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int cases;
	in >> cases;

	for ( int i = 0; i < cases; i++ )
	{
		int e, d;
		in >> e;
		cout << e;
		map<string, int> engines;
		string tmp;

		getline(in, tmp);
		for ( int j = 0; j < e; j++ )
		{

			getline(in, tmp);
			engines[tmp] = j;
			cout << tmp << "\n";
		}
		
		in >> d;
		cout << d;
		getline(in, tmp);
		vector<string> data(d);
		for ( int j = 0; j < d; j++ )
		{
			getline(in, tmp);
			data[j] = tmp;
			cout << tmp << tmp.size() << "\n";
		}
		out << "Case #" << (i+1) << ": " << nswitches(engines, data) << "\n";
			
		engines.clear();
	}
	return 0;
}

