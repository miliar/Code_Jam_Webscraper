#include "stdlib.h"
#include <iostream>
#include <string>
using namespace std;

#define MAXB 26
#define INERT -1

int T;
int c[MAXB][MAXB], d[MAXB][MAXB];
int C, D, N;
string sin, sout;

void read_case()
{
	string s;
	for (int i=0; i<MAXB; i++)
		for (int j=0; j<MAXB; j++)
		{
			c[i][j] = INERT;
			d[i][j] = INERT;
		}
	sout = "";
	cin>>C;
	for (int i=0; i<C; i++)
	{
		cin>>s;
		c[s[0]-'A'][s[1]-'A'] = s[2]-'A';
		c[s[1]-'A'][s[0]-'A'] = s[2]-'A';
	}
	cin>>D;
	for (int i=0; i<D; i++)
	{
		cin>>s;
		d[s[0]-'A'][s[1]-'A'] = s[2]-'A';
		d[s[1]-'A'][s[0]-'A'] = s[2]-'A';
	}
	cin>>N>>sin;
}

void solve()
{
	sout += sin[0];
	
	for (int i=1; i<N; i++)
	{
		if (sout.length()==0)
		{
			sout += sin[i];
			continue;
		}
		if (c[sout[sout.length()-1]-'A'][sin[i]-'A'] != INERT)
			sout[sout.length()-1] = c[sout[sout.length()-1]-'A'][sin[i]-'A'] + 'A';
		else
		{
			sout += sin[i];
			for (unsigned int j=0; j<sout.length(); j++)
				if (d[sout[j]-'A'][sin[i]-'A'] != INERT)
					sout.clear();
		}
	}
}

void output(int i)
{
	cout<<"Case #"<<i<<": [";
	if (sout.length()==0)
	{
		cout<<"]"<<endl;
		return;
	}
	for (unsigned int i=0; i<sout.length()-1; i++)
		cout<<sout[i]<<", ";
	if (sout.length()>=1)
		cout<<sout[sout.length()-1];
	cout<<"]"<<endl;
}

int main()
{
	cin>>T;
	for (int i=0; i<T; i++)
	{
		read_case();
		solve();
		output(i+1);
	}
	return 0;
}
