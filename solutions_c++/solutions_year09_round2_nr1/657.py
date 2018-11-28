// CJ09R1BA.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cstring>
#include <string>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

struct Node{
	double p;
	string name;
	bool enabled;

	Node():p(0.0),name(),enabled(false){}
};

void BuildNode(vector<Node> & tree,int current,string & input,int begin,int end)
{
	while(begin<end && isspace(input[begin]))++begin;
	if(input[begin]!='(')return;
	++begin;
	while(begin<end && isspace(input[begin]))++begin;

	int now=begin;
	while(begin<end && input[begin]!=')' && input[begin]!='(' && !isspace(input[begin])) ++begin;
	
	string sub=input.substr(now,begin-now);

	if(current>=tree.size())tree.resize(current+1);
	tree[current].p=atof(sub.c_str());
	tree[current].enabled=true;

	while(begin<end && isspace(input[begin]))++begin;
	if(input[begin]==')') return;

	if(input[begin]!='('){
		now=begin;
		while(begin<end && input[begin]!=')' && input[begin]!='(' && !isspace(input[begin])) ++begin;
		tree[current].name=input.substr(now,begin-now);
		while(begin<end && isspace(input[begin]))++begin;
	}

	if(input[begin]=='('){
		now=begin++;
		int level=0;

		for(;input[begin]!=')' || level!=0;++begin)
		{
			if(input[begin]=='(') level++;
			if(input[begin]==')') level--;
		}
		begin++;

		BuildNode(tree,current+current+1,input,now,begin);
	}

	while(begin<end && isspace(input[begin]))++begin;

	if(input[begin]=='('){
		now=begin++;
		int level=0;

		for(;input[begin]!=')' || level!=0;++begin)
		{
			if(input[begin]=='(') level++;
			if(input[begin]==')') level--;
		}
		begin++;

		BuildNode(tree,current+current+2,input,now,begin);
	}



}

void BuildTree(vector<Node> & tree,int lines)
{
	char buf [255];

	string input;

	for(int l=0;l<lines;++l)
	{
		memset(buf,0,255);
		cin.getline(buf,255);
		input.append(buf);
	}

	BuildNode(tree,0,input,0,input.size());

}

void Judge(vector<Node> & tree,vector<string> fea)
{
	double p=1.0;
	int c=0;

	while(true)
	{
		p*=tree[c].p;

		bool has=true;
		if(find(fea.begin(),fea.end(),tree[c].name)==fea.end()) has=false;

		if(has && c+c+1 < tree.size() && tree[c+c+1].enabled)
		{
			c=c+c+1;
			continue;
		}

		if(!has && c+c+2 < tree.size() && tree[c+c+2].enabled)
		{
			c=c+c+2;
			continue;
		}

		break;
		
	}

	printf("%1.7lf\n",p);
}


int _tmain(int argc, _TCHAR* argv[])
{
	char buf[255];
	int cases;
	cin>>cases;
	cin.getline(buf,255);

	for (int c=0;c<cases;++c)
	{
		printf("Case #%d:\n",c+1);
		int lines;
		cin>>lines;
		memset(buf,0,255);
		cin.getline(buf,255);

		vector<Node> tree;
		BuildTree(tree,lines);


		int animals;
		cin>>animals;
		memset(buf,0,255);
		cin.getline(buf,255);

		for(int i=0;i< animals; ++i)
		{
			memset(buf,0,255);
			cin.getline(buf,255);
			
			string animal(buf);
			stringstream ssa(animal);

			string name;
			ssa>>name;

			int features;
			ssa>>features;
			
			vector<string> f;
			for(int j=0;j<features;++j)
			{
				string fea;
				ssa>>fea;
				f.push_back(fea);
			}

			Judge(tree,f);


		}

	}
	return 0;
}

