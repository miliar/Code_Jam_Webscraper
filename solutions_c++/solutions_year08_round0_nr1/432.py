//============================================================================
// Name        : SavingTheUniverse.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

void initEngine(list<int> *e, int n, int except)
{
	for (int i=0;i<n;i++)
		if (i != except) 
			e->push_back(i);
}

int main() {

	ifstream fin;
	ofstream fout;
	fout.open("output.txt");
	fin.open("sample.txt");
	int n, search, queryNum;
	string *sName;
	fin>>n;
	for(int i=0;i<n;i++)
	{
		int Switch = 0;
		fin>>search;
		fin.ignore(10,'\n');
		list<int> engineList;
		initEngine(&engineList, search, -1);
		sName = new string [search];
//debug
//		cout<<search<<endl;
	
		int maxSName =0;
		for (int s =0; s<search;s++)
		{
			getline(fin,sName[s]);
			if (sName[s].size()>maxSName)
				maxSName = sName[s].size();
//debug
//			cout<<sName[i]<<endl;
		}
//debug	
//		cout<<maxSName<<endl;
		
		fin >> queryNum;
		fin.ignore(10,'\n');
		string query;
		int engineTerminator;
		for(int j=0;j<queryNum;j++)
		{
//debug
			cout<<i<<"\t"<<j<<"\t"<<Switch<<"\t"<<engineList.size()<<endl;

			getline(fin,query);
			if(query.size()<=maxSName)
			{
				list<int>::iterator l = engineList.begin();
				while(l != engineList.end())
				{
					if (query.compare(sName[*l])==0)
					{
						engineTerminator = *l;
						list<int>::iterator remove = l;
						l++;
						engineList.erase(remove);
					}
					else
						l++;
				}
				if (engineList.empty())
				{
					Switch++;
					initEngine(&engineList, search, engineTerminator);
					
				}
			}
			else
			{
//debug				
//				cout<<i<<"\t"<<j<<"\t"<<"no mathcing query"<<endl;
			}
		}
		cout<<"Case #"<<i+1<<": "<<Switch<<endl;
		fout<<"Case #"<<i+1<<": "<<Switch<<endl;
		delete[] sName;
		engineList.clear();
	}
	fout.close();
	fin.close();
	return 0;
}
