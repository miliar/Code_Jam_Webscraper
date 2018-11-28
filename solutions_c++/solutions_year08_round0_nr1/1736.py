#ifndef CODEJAM_H
#define CODEJAM_H

#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <math.h>
#include <map>
#include <algorithm>
#include <vector>
//#include <crtdbg.h>
using namespace std;

#define FOR0(i,b)	for(int i=0,_b=(b);i<_b;i++)
#define FOR1(i,b)	for(int i=1,_b=(b);i<=_b;i++)
#define LOG(s,ss)	cout<<s<<""<<ss<<endl;
// functions declaraion
void su(ifstream &input);

#endif

#include "game.h"

std::map<string, int> sn;
int q[1024];
int f(int* query, int& p);

class BitNumber
{
public:
	BitNumber(int n)
	{
		nn = n;
		bn[0] = bn[1] = 0;
		if (n>64) FOR0(i,n-64) bn[0]|=1LL<<i;
		n=(n>64)?64:n;
		FOR0(j,n)bn[1]|=1LL<<j;
	}
	void clear(int p)
	{
		if (p<0 || p>nn)
		{
			LOG("Unexpected big shifting:", p)
		}
		if(p>64) bn[0]&=(1LL<<(p-65))^(~0LL);
		else bn[1]&=(1LL<<p)^(~0LL);
	}
	bool isEmpty()
	{
		return (bn[0]==0 && bn[1]==0);
	}

private:
	__int64 bn[2];
	int nn;
};

bool bisEmpty = false;
void su(ifstream &input)
{
	char buf[128] = {0};
	int cases;
	input >> cases;

	FOR1(z,cases)
	{
		sn.clear();
		memset(q,-1,1024);
		int se;
		input >> se;
		input.getline(buf, 127);
		FOR0(i,se)
		{
			input.getline(buf, 127);
			string s(buf);
			sn.insert(pair<string,int>(s, i));
		}
		int qn; input >> qn;
		if (qn==0) 
		{
			cout << "Case #" << z << ": 0" << "\n";
			continue;
		}

		input.getline(buf, 127);
		FOR0(j,qn)
		{
			input.getline(buf, 127);
			string s(buf);
			map<string, int>::iterator it;
			it = sn.find(s);
			if (it == sn.end()) 
				LOG("Unexcepted:", s)
			else 
				q[j]=it->second;
		}
		int st=0, p=0;
		while (q[f(q,p)] != -1) 
		{
			st++;
		}
		if (bisEmpty) st++;
		cout << "Case #" << z << ": " << st << "\n";
	}

	cout.flush();
}

int f(int* query, int& p)
{
	BitNumber b((int)sn.size());
	while(!b.isEmpty() && query[p]>=0)
		b.clear(query[p++]);
	p--;
	bisEmpty = b.isEmpty();
	return p+1;
}


int main(int argc, char *argv[])
{

	char filename[64] = {0};
	if (argc > 1)
		strcpy(filename, argv[1]);
	else
		strcpy(filename, "input.jam");

	std::ifstream input(filename);

	if (!input.is_open())
	{
		cout << "Warning: unable to open input file -- " << filename << endl;
		return 1;
	}

	
	su(input);
	return 0;
}