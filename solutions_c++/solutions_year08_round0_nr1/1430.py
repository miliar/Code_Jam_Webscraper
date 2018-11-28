// a-saving.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include <string>
#include <list>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;



class Engine
{
public:
	Engine(string _name) : name(_name) {}
	void check(unsigned int p, const string &s)
	{
		if(s==name)
			pos.push_back(p);
	}
	int delta_next(unsigned int p)
	{
		if(pos.empty())
			return -1;
		unsigned int i = 0;
		while(i<pos.size()&&p>pos[i]) 
			i++;
		if(i==pos.size())
			return -1;
		return (pos[i]-p);
	}
private:
	string name;
	vector<unsigned int> pos;
};

class Case
{
public:
	Case(ifstream &f) : nS(0)
	{
		int nE;
		f >> nE;
		char name[255];
		f.getline(name,255);
		for(int i = 0; i<nE; i++)
		{
			f.getline(name,255);
			Engine* tmp2 = new Engine(name);
			engs.push_back(tmp2);
		}
		int nQ;
		f >> nQ;
		f.getline(name,255);
		for(int i=0; i<nQ; i++)
		{
			f.getline(name,255);
			string tmp(name);
			for(list<Engine*>::iterator it= engs.begin(); it!=engs.end(); it++)
			{
				(*it)->check(i,tmp);
			}
		}
	}
	void Simulate()
	{
		//Select 1st
		unsigned int a=0;
		unsigned int n=0;
		while(true)
		{
			for(list<Engine*>::iterator it= engs.begin(); it!=engs.end(); it++)
			{
				int t = (*it)->delta_next(a);
				if(t==-1)
					return;
				if(t>n)
				n=t;
			}
			nS++;
			a+=n;
			n=0;
		}
	}
	void Print()
	{
		cout << nS << endl;
	}
private:
	unsigned int nS;
	list<Engine*> engs;
};

int _tmain(int argc, _TCHAR* argv[])
{
	if(argc!=2)
		return 1;
	ifstream f(argv[1]);
	int total;
	f >> total;
	for(int i = 0;i<total;i++)
	{
		Case c(f);
		c.Simulate();
		cout << "Case #" << (i+1) << ": ";
		c.Print();
	}
	return 0;
}

