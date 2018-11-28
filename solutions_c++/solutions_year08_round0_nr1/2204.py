// Prinks.cpp : Defines the entry point for the console application.
//

#include <conio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>
#include <istream>

using namespace std;
//Alogrithm.
#define REP(i,n) for(int i = 0;i<n;++i)
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<VS> VVS;
typedef vector<VI> VVI;


int main()
{
	int N;
	char s[128];
	string str;
	VS search_engines;
	VS search_queries;
	VVS search_engine;
	VVS search_querie;
	bool flag = false;
	std::map<string,int> Query;
	VI num_times;
	VI out;	
	int pos = 0;
	int size = sizeof("\n");
	ifstream inp;
	inp.open("A-small.in");
	inp>>N;
	REP(i,N)
	{
		int S,Q;			
		inp>>S;
		REP(j,S+1)
		{
			getline(inp,str);			
			search_engines.push_back(str);
		}
		search_engine.push_back(search_engines);
		inp>>Q;
		REP(j,Q+1)
		{
			getline(inp,str);
			search_queries.push_back(str);
		}
		search_querie.push_back(search_queries);
		search_engines.clear();
		search_queries.clear();
	}
	REP(i,N)
	{
		VS search = search_querie.at(i);	
		for(int j=1;j< search.size();++j)
		{
			str = search.at(j);
			if(Query.find(str)!=Query.end())
				Query[str]+=1;
			else
			{
				Query.insert(make_pair(str,1));
			}
		}
		VS SE = search_engine.at(i);
		for(int k =1;k<SE.size();++k)
		{
			if(Query.find(SE.at(k))==Query.end())
			{
				out.push_back(0);
				flag = true;
				break;
			}			
		}

		VS::iterator itr1;
		VS::iterator itr2;
		vector<VS::iterator> vec;
		int count = 0;
		bool found = false;
		if(!flag)
		{			
			for(itr1 = search.begin()+1;itr1 < search.end();)
			{
				for(int k = 1; k < SE.size();++k)
				{
					itr2 = std::find(itr1,search.end(),SE.at(k));
					if(itr2 == search.end())
					{
						found = true;
						break;
					}
					vec.push_back(itr2);
				}	
				if(!found)
				{
					itr1 = *(std::max_element(vec.begin(),vec.end()));
					++count;
				}
				else
					break;
			}
			out.push_back(count);
		}		
		//reset the data structures
		flag = false;
		SE.clear();
		Query.clear();
		search.clear();
		num_times.clear();
		count = 0;
		found = false;
	}	

	ofstream file("A-small.out");
	REP(i,out.size())
		file<<"Case  #"<<i+1<<":  "<<out.at(i)<<endl;

	getch();
}

