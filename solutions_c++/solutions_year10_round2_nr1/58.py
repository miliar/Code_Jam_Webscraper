#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

vector<vector<pair<string,int> > > lis;

vector<string> parse(string s)
{
	vector<string> ans;
	for(int i=0; i<s.size(); i++)
	{
		if(s[i]=='/')
			s[i]=' ';
	}
	stringstream sin(s);
	string t;
	while(sin >> t)
		ans.push_back(t);
	return ans;
}

int add(string s)
{
	int ans = 0;
	int curr = 0;
	int i,j;
	vector<string> vals = parse(s);
	vector<pair<string,int> > empt;
	
	for(int k=0; k<vals.size(); k++)
	{
		for(i=0; i<lis[curr].size(); i++)
		{
			if(lis[curr][i].first==vals[k])
				break;
		}
		if(i<lis[curr].size())
		{
			curr=lis[curr][i].second;
		}
		else {
			lis[curr].push_back(make_pair(vals[k],lis.size()));
			curr = lis.size();
			lis.push_back(empt);
			ans++;
		}
	}
	return ans;

}

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		lis.clear();
		vector<pair<string,int> > empt;
		lis.push_back(empt);
		int ans = 0;
		fin >> i >> j;
		for(k=0; k<i; k++)
		{
			string s;
			fin >> s;
			add(s);
		}
		for(k=0; k<j; k++)
		{
			string s;
			fin >> s;
			ans+=add(s);
		}
		
		
	
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

