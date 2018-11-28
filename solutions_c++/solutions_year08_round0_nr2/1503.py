#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <istream>
#include <sstream>
#include <set>
using namespace std;
 
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl; 

vs strsp(string c, string delim=" ")
{
	vs ret;
	string a = "";
	int p = 0;
	while(p < c.size())
	{
		while(p < c.size() && delim.find(c[p]) == string::npos ) { a += c[p++]; }
		if(a.size()) { ret.push_back(a); a = ""; }
	}
	return ret;
}	

pair<pair<int,int>,int> mtri(int a, int b, int c)
{
	return make_pair(make_pair(a,b),c);
}

int NT,turntime;
vector<pair<pair<int,int>,int> > trains;
int ran[505];

void ChooChoo(int time, int station)
{
	for(int i = 0; i < NT; i++)
	{
		if(trains[i].first.first < time) continue;
		if(ran[i]) continue;
		if(trains[i].second != station) continue;

		ran[i] = 1;
		ChooChoo(trains[i].first.second + turntime, 1-station);
		return;
	}
	return;
}

int main()
{
	int T, ctest = 0;
	
	ofstream fout("bout.txt");
	ifstream fin("bin.txt");
	fin >> T;
	while(ctest++ < T)
	{
		trains.clear();
		int na, nb;
		fin >> turntime >> na >> nb;
		
		for(int i = 0; i < na; i++)
		{
			string start = "", end = "";
			fin >> start >> end;

			int sh, sm, eh, em;
			sscanf(start.c_str(), "%d:%d",&sh,&sm);
			sscanf(end.c_str(), "%d:%d",&eh,&em);

			trains.push_back(mtri(sh*60+sm,eh*60+em,0));
		}

		for(int i = 0; i < nb; i++)
		{
			string start = "", end = "";
			fin >> start >> end;

			int sh, sm, eh, em;
			sscanf(start.c_str(), "%d:%d",&sh,&sm);
			sscanf(end.c_str(), "%d:%d",&eh,&em);

			trains.push_back(mtri(sh*60+sm,eh*60+em,1));
		}

		NT = na + nb;
		sort(trains.begin(),trains.end());
		memset(ran,0,sizeof(ran));
		
		int Atrain = 0, Btrain = 0;
		for(int i = 0; i < NT; i++)
		{
			if(ran[i]) continue;
			
			ran[i] = 1;
			if(trains[i].second == 0) Atrain++;
			else Btrain++;
			ChooChoo(trains[i].first.second + turntime, 1-trains[i].second);
		}

		fout << "Case #" << ctest << ": " << Atrain << " " << Btrain << "\n";
	}
	fout.close();
	return 0;
}
		