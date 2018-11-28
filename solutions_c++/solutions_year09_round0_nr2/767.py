#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>
using namespace std;


typedef long long int64;
typedef unsigned long long uint64;
#define pause system("pause");
#define set0(x) memset(x, 0, sizeof(x))

clock_t __time;
#define retime __time = clock();
#define outtime cout<<clock()-__time<<endl;
const double pi = acos(-1.0);
const double eps = 1e-11;

template<class T> T gcd(const T &a, const T &b) {return (b == 0) ? a : gcd ( b, a%b);}
template<class T> T lcm(const T &a, const T &b) {return a*(b/gcd(a,b));}

int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

int m1[101][101];
char m2[101][101];
int h,w;
char f;

int pd(int x, int y)
{
	int ou = 0;
	int m = m1[x][y];
	if(x > 0)
	{
		if(m1[x-1][y] < m)
		{
			ou = 1;
			m = m1[x-1][y];
		}
	}
	if(y > 0)
	{
		if(m1[x][y-1] < m)
		{
			ou = 2;
			m = m1[x][y-1];
		}
	}
	if(y < w-1)
	{
		if(m1[x][y+1] < m)
		{
			ou = 3;
			m = m1[x][y+1];
		}
	}
	if(x < h-1)
	{
		if(m1[x+1][y] < m)
		{
			ou = 4;
			m = m1[x+1][y];
		}
	}
	return ou;
}

typedef struct
{
	int x,y;
} node;


void fill(int x, int y)
{
	queue<node> que;
	node m,t;
	m.x = x;
	m.y = y;
	m2[x][y] = f;
	que.push(m);
	while(!que.empty())
	{
		m = que.front();
		que.pop();
		if(m.x > 0)
		{
			if(m2[m.x-1][m.y] == 0)
			{
				if(pd(m.x-1, m.y) == 4)
				{
					m2[m.x-1][m.y] = f;
					t.x = m.x - 1;
					t.y = m.y;
					que.push(t);
				}
			}
		}
		if(m.y > 0)
		{
			if(m2[m.x][m.y-1] == 0)
			{
				if(pd(m.x, m.y-1) == 3)
				{
					m2[m.x][m.y-1] = f;
					t.x = m.x;
					t.y = m.y - 1;
					que.push(t);
				}
			}
		}
		if(m.y < w-1)
		{
			if(m2[m.x][m.y+1] == 0)
			{
				if(pd(m.x, m.y+1) == 2)
				{
					m2[m.x][m.y+1] = f;
					t.x = m.x;
					t.y = m.y + 1;
					que.push(t);
				}
			}
		}
		if(m.x < h-1)
		{
			if(m2[m.x+1][m.y] == 0)
			{
				if(pd(m.x+1, m.y) == 1)
				{
					m2[m.x+1][m.y] = f;
					t.x = m.x + 1;
					t.y = m.y;
					que.push(t);
				}
			}
		}
	}
	f++;
}

void run()
{
	for(int i = 0; i < h; i++)
	{
		for(int j = 0; j < w; j++)
		{
			if(pd(i,j) == 0)
			{
				fill(i,j);
			}
		}
	}
}

int main()
{
	int n;
	cin>>n;
	for(int i = 1; i <= n; i++)
	{
		set0(m1);
		set0(m2);
		f = 'A';
		cin>>h>>w;
		for(int j = 0; j < h; j++)
			for(int k = 0; k < w; k++)
				cin>>m1[j][k];
		run();
		f = 'a';
		for(int j = 0; j < h; j++)
		{
			for(int k = 0; k < w; k++)
			{
				if('A' <= m2[j][k] && m2[j][k] <= 'Z')
				{
					char ff;
					ff = m2[j][k];
					for(int jj = 0; jj < h; jj++)
						for(int kk = 0; kk < w; kk++)
							if(m2[jj][kk] == ff)
								m2[jj][kk] = f;
					f++;
				}
			}
		}
		cout<<"Case #"<<i<<":"<<endl;
		for(int j = 0; j < h; j++)
		{
			cout<<m2[j][0];
			for(int k = 1; k < w; k++)
				cout<<" "<<m2[j][k];
			cout<<endl;
		}
	}
	return 0;
}