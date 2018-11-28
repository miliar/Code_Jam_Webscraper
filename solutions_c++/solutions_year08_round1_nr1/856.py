#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <assert.h>
typedef std::vector<int > MyVec;
class Caculator
{
public:

	typedef MyVec ::iterator MyIterator;
	typedef MyVec::reverse_iterator MyRIterator;
public:

	static int  GetResult(	MyVec &v1,
	MyVec &v2)
	{
		assert(v1.size()==v2.size());
		std::sort(v1.begin(),v1.end());
		std::sort(v2.begin(),v2.end());
		int r1=0,r2=0;

		MyIterator v1End=v1.end();
		MyRIterator v2RBegin=v2.rbegin();
		for(MyIterator iV1=v1.begin();iV1!=v1End;++iV1,++v2RBegin)
		{
			r1+=(*iV1)* (*v2RBegin);
		}
		MyRIterator v1REnd=v1.rend();
		MyIterator v2Beg=v2.begin();
		for(MyRIterator iV1=v1.rbegin();iV1!=v1REnd;++iV1,++v2Beg)
		{
			r2+=(*iV1) *
				(*v2Beg);
		}
		return std::min(r1,r2);
	}
	
};


int
main(int agrc,char ** agrv)
{
	std::ifstream infile("input.in");
	std::ofstream outfile("output");
	if(!infile)
	{
		std::cout<<"file not exists"<<std::endl;
		exit(1);
	}
	if(!outfile)
	{
		std::cout<<"cannot open output file"<<std::endl;
		exit(1);
	}
	int LoopTime;
	infile>>LoopTime;
	if(!infile)
	{
		std::cout<<"fail to read loop count"<<std::endl;
		exit(1);
	}
	for(int i=0;i!=LoopTime;++i)
	{
		int VecSize;
		infile>>VecSize;
		if(!infile)
		{
			std::cout<<"fail to read vec size"<<std::endl;
			exit(1);
		}
		typedef std::vector<int > MyVec;
		MyVec v1,v2;
		for(int j=0;j!=VecSize;++j)
		{
			int Input;
			infile>>Input;
			if(!infile)
			{
				std::cout<<"fail to read vec content"<<std::endl;
				exit(1);
			}
			v1.push_back(Input);
		}
		for(int j=0;j!=VecSize;++j)
		{
			int Input;
			infile>>Input;
			if(!infile)
			{
				std::cout<<"fail to read vec content"<<std::endl;
				exit(1);
			}
			v2.push_back(Input);
		}

		int result=Caculator::GetResult(v1,v2);
		outfile<<"Case #"<<i+1<<": "<<result<<"\n";
	}
	return 0;
}