#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cassert>
#include <string>
#include <hash_map>
#include <ctime>

using namespace std;
using namespace stdext;

#define FOR(x,a,b) for(int x=a;x<b;x++)

vector<string>::iterator fun(vector<string>::iterator iter1,vector<string>::iterator iter2,int size,set<string,less<string>>& search)
{
	set<string> a;
	vector<string>::iterator iter=iter1;
	while (iter!=iter2)
	{
		if(search.find(*iter)!=search.end())
			a.insert(*iter);
		if (a.size()==size)
			return iter;
		else
			iter++;
	}
	return iter2;
}

int main()
{
	ifstream file("a.txt");
	int N;
	file>>N;
	ofstream file1("out.txt");
	FOR(i,1,N+1)
	{
		int S,Q;
		set<string,less<string> > query;
		set<string,less<string> > search_engine;
		vector<string> qq,ss;

		file>>S;
		ss.reserve(S);
		string temp;
		char c;
	
		getline(file,temp,'\n');
		FOR(j,0,S)
		{
			getline(file,temp,'\n');
			search_engine.insert(temp);
			ss.push_back(temp);
		}
		file>>Q;
		qq.reserve(Q);
		getline(file,temp,'\n');
		FOR(j,0,Q)
		{
			getline(file,temp);
			query.insert(temp);
			qq.push_back(temp);
		}

		int  result=0;
		
		int q_class=query.size();
		int s_class=search_engine.size();
		set<string> u;
		set_intersection(query.begin(),query.end(),search_engine.begin(),search_engine.end(),inserter(u,u.begin()));
		if (u.size()<search_engine.size())
		{
			file1<<"Case #"<<i<<": 0"<<endl;
			continue;
		}
		vector<string>::iterator iter=qq.begin();
		while (true)
		{
			
			iter=fun(iter,qq.end(),s_class,search_engine);
			
			if (iter==qq.end())
				break;
			result++;
		}
		
		
		file1<<"Case #"<<i<<": "<<result<<endl;

	}
	file1.close();
	file.close();
	return 0;
}