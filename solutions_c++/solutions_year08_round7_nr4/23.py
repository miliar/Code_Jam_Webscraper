#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cmath>
#include <string>

using namespace std;
int P[17][1<<16];
string b;
int dx[]={-1,0,1,-1,1,-1,0,1};
int dy[]={-1,-1,-1,0,0,1,1,1};
int R;
int C;
int rec(int id,int mask)
{
	if(P[id][mask]!=-1)
	return P[id][mask];
	int c,r;
	r = id / C;
	c = id % C;
	P[id][mask]=0;
	for(int i=0;i<8;i++)
	{
		int r1 = r + dx[i];
		int c1 = c + dy[i];
		if(r1>=0 && c1>=0 && r1<R && c1<C)
		{
			int id1 = r1*C+c1;
			if(b[id1]=='#' || ((mask>>id1)&1))
				continue;
			if(rec(id1,mask|(1<<id1))==0)
				P[id][mask]=1;
		}
	}
	return P[id][mask];
}

int main()
{

	int ctr = 0 ;
	int N;
	cin>>N;
	while(N--)
	{
		ctr++;
		cin>>R>>C;	
		for(int i=0;i<17;i++) for(int j=0;j<(1<<16);j++)
		P[i][j]=-1;
		int s;
		b="";
		for(int i=0;i<R;i++)
		{
			string T;
			cin>>T;
			for(int j=0;j<C;j++)
			if(T[j]=='K')
			{
				b=b+"#";
				s=i*C+j;		
			}
			else
				b=b+T[j];
		}
		if(rec(s,1<<s)==1)
		cout<<"Case #"<<ctr<<": A\n";
		else
		cout<<"Case #"<<ctr<<": B\n";
	}
	return 0;
}

