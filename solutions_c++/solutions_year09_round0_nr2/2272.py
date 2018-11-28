// code_jam_b.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <fstream>
#include <vector>
#include <stack>
using namespace std;


	long t,h,w,mas[105][105];
	char p[105][105];
	char fl[105][105]; //1 - suhaya
	stack<pair<int,  int>> was;
	long dx[]={-1, 0, 0, 1};
	long dy[]={0, -1, 1, 0};
	char th='a';

void fillp(char c)
{
	int x, y;
	while(!was.empty())
	{
		
		x = was.top().first;
		y = was.top().second;
		was.pop();

		p[x][y]=c;
		fl[x][y]=0;
	}
}
pair<int, int> togo(pair<int, int> t)
{
	long tmin = mas[t.first-1][t.second];
	pair<int, int> res = make_pair(t.first-1, t.second);
	if(mas[t.first][t.second-1] < tmin)
	{
		tmin = mas[t.first][t.second-1];
		res = make_pair(t.first, t.second-1);
	}
	if(mas[t.first][t.second+1] < tmin)
	{
		tmin = mas[t.first][t.second+1];
		res = make_pair(t.first, t.second+1);
	}
	if(mas[t.first+1][t.second] < tmin)
	{
		tmin = mas[t.first+1][t.second];
		res = make_pair(t.first+1, t.second);
	}
	if(	tmin>=mas[t.first][t.second])
	{
		return make_pair(0, 0);
	}
	if(fl[res.first][res.second]==0)
	{
		return make_pair(-1*res.first, -1*res.second);
	}
	return res;

}
void go(int x, int y)
{
	fl[x][y]=0;
	was.push(make_pair(x,y));
	long ii=0;

	pair<int, int> to = togo(make_pair(x, y));

	if((to.first!=0)&&(to.first>0))
	{
		go(to.first, to.second);
		return;
	}
	if(to.first==0)
	{
		fillp(th);
		th++;
	}
	if(to.first<0)
	{
		fillp(p[-1*to.first][-1*to.second]);
		return;
	}
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");


	in>>t;
	
	long i,j,k,l,m,n;
	for(l=1;l<=t;l++)
	{
		th='a';
		in>>h>>w;
		for(i=0;i<105;i++)
		{
			for(j=0;j<105;j++)
			{
				mas[i][j]=10005;
				p[i][j]='0';
				fl[i][j]=1;
			}
		}

		for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
			{
				in>>mas[i][j];
			}
		}

		for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
			{
				if(fl[i][j]!=0)
				{
					go(i,j);
				}
			}
		}

		out<<"Case #"<<l<<":\n";
		for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
			{
				out<<p[i][j];
				if(j!=w)
				{
					out<<" ";
				}
				else
				{
					out<<"\n";
				}
			}
		}
	}
		
	

	return 0;
}

