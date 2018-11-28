// D.cpp : Defines the entry point for the console application.
//

#pragma warning(disable:4786)
#include <stdafx.h>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

map<vector<vector<char> >,bool> mem;
int dir[8][2]={1,0,-1,0,0,1,0,-1,1,1,1,-1,-1,1,-1,-1};

bool f(vector<vector<char> > &c,int nr,int nc)
{
	if(mem.find(c)!=mem.end()) return mem[c];

	int kr,kc;
	for(int i=0;i<nr;i++) for(int j=0;j<nc;j++) if(c[i][j]=='K') {kr=i;kc=j;break;}
	for(int i=0;i<8;i++)
	{
		int tr=kr+dir[i][0],tc=kc+dir[i][1];
		if(tr>=0&&tr<nr&&tc>=0&&tc<nc)
		{
			if(c[tr][tc]=='.')
			{
				vector<vector<char> > nst=c;
				nst[kr][kc]='#';
				nst[tr][tc]='K';
				if(f(nst,nr,nc)==false) return true;
			}
		}
	}
	return false;
}

void process(int num)
{
	vector<vector<char> > c(4,vector<char>(4,' '));
	int nr,nc;

	cin>>nr>>nc;
	for(int i=0;i<nr;i++)
		for(int j=0;j<nc;j++)
			cin>>c[i][j];
	if(f(c,nr,nc)==true)
		cout<<"Case #"<<num<<": A"<<endl;
	else
		cout<<"Case #"<<num<<": B"<<endl;
}

int main(void)
{
	int num;
	cin>>num;
	for(int i=1;i<=num;i++) process(i);
	return 0;
}
