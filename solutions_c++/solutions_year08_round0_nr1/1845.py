// CodeJameQ 1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <assert.h>
#include "Functions.h"
int RecureMinTime(const SearchEngineVec & searchEngines,
				  int currentIndex,
				  IncomingQueryIt  It,
				  const IncomingQueryIt & end);

int IsNotNeedRecursive(const SearchEngineVec & searchEngines,
					   IncomingQueryIt  It,
					   const IncomingQueryIt & end);

int	MinTime(const SearchEngineVec & searchEngines,
			IncomingQueryIt  It,
			const IncomingQueryIt & end)
{
	int IsNeed=IsNotNeedRecursive(searchEngines,It,end);
	if(IsNeed!=-1)
		return IsNeed;
	size_t cLoopTime=searchEngines.size();
	int MinNum=0x7fffffff;
	for(int i=0;i!=cLoopTime;++i)
	{
		MinNum=std::min(RecureMinTime(searchEngines,
			i,
			It,end),MinNum);
	}
	return MinNum;
}


int RecureMinTime(const SearchEngineVec & searchEngines,
				  int currentIndex,
				  IncomingQueryIt  It,
				  const IncomingQueryIt & end)
{
	size_t cSearchEngines=searchEngines.size();
	while(It!=end)
	{
		if(*It!=searchEngines[currentIndex])
		{
			++It;
			continue;
		}
		int MinNum=0x7fffffff;
		for(int i=1;i!=cSearchEngines;++i)
			MinNum=std::min(RecureMinTime(searchEngines,
			(currentIndex+i)%cSearchEngines,
			It,end),MinNum);
		return MinNum+1;
	}
	return 0;
}
int IsNotNeedRecursive(const SearchEngineVec & searchEngines,
					   IncomingQueryIt  It,
					   const IncomingQueryIt & end)
{
	size_t s=searchEngines.size();
	int i;
	SearchEngineVec::const_iterator sbeg=searchEngines.begin();
	SearchEngineVec::const_iterator send=searchEngines.end();
	IncomingQueryIt  ItSave=It;
	for(;It!=end;++It)
	{
		if(std::find(sbeg,send,*It)==send)
			return -1;
	}
	typedef std::set<std::string> MySet;
	typedef MySet::_Pairib value_type;
	MySet NewEngines;
	It=ItSave;
	i=0;
	int setSize=0;
	//bool useSpecify=false;
	while(It!=end)
	{

		value_type v=NewEngines.insert(*It);
		if(v.second==true)
		{
			if(++setSize==s)
			{
				NewEngines.clear();
				NewEngines.insert(*It);
				++i;
				setSize=1;
				//useSpecify=true;
			}
		}


		++It;
	}
	return i;
}
int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream infile("A-small-attempt4.in");
	if(!infile)
		return 1;
	std::ofstream outfile("output.txt");
	if(!outfile)
		return 1;
	int cLoopTime;
	infile>>cLoopTime;
	assert(!infile==false);
	for(int i=0;i!=cLoopTime;++i)
	{
		int InnerLoopTime;
		infile>>InnerLoopTime;
		if(InnerLoopTime==0)
		{
			outfile<<"Case #"<<i+1<<": "<<0<<"\n";
			continue;
		}
		assert(!infile==false);
		SearchEngineVec searchEngine;
		IncomingQuery incomingQuery;
		infile.ignore();
		for(int j=0;j!=InnerLoopTime;++j)
		{
			std::string input;
			std::getline(infile,input);
			assert(!infile==false);
			searchEngine.push_back(input);
		}
		
		infile>>InnerLoopTime;
		if(InnerLoopTime==0)
		{
			outfile<<"Case #"<<i+1<<": "<<0<<"\n";
			continue;
		}
		assert(!infile==false);
		infile.ignore();
		for(int j=0;j!=InnerLoopTime;++j)
		{
			std::string input;
			std::getline(infile,input);
			assert(!infile==false);
			incomingQuery.push_back(input);
		}

		int Min=MinTime(searchEngine,incomingQuery.begin(),
			incomingQuery.end());
		outfile<<"Case #"<<i+1<<": "<<Min<<"\n";
	}

	return 0;
}

