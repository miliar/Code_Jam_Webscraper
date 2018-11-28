
/***** Author : Kunal *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

//int d[][2]={{-1.0},{1,0},{0,-1},{0,1}};

struct Tree
{
	vector< Tree > T;
	string name;
};

int gctr;

void insert( istringstream &path, Tree &node, bool ct )
{
	string tmp;
	if(path >> tmp )
	{
		bool fl = false;
		REP(i, SZ(node.T) )
		{
			if( node.T[i].name == tmp )
			{
				fl = true;
				insert( path, node.T[i], ct );
				return;
			}
		}
		Tree mtmp;
		mtmp.name = tmp;
		if( !fl )
		{
			node.T.PB( mtmp );
			insert( path, node.T[ SZ(node.T) -1 ], ct );
			if( ct ) gctr++;
		}
	}
}

void modifyString( string &str)
{
	size_t found;

	found=str.find_first_of("/");
	while (found!=string::npos)
	{
		str[found]=' ';
		found=str.find_first_of("/",found+1);
	}
}

int main()
{
	int t; S("%d", &t);
	int n, m;
	string str;
	REP(tc ,t )
	{
		S("%d%d", &n, &m);
		Tree root;
		root.name = "/";
		REP(i,n )
		{
			cin >> str;
			modifyString( str );
			istringstream iss(str);
			insert( iss, root, false );
		}
		gctr = 0;
		REP(i,m )
		{
			cin >> str;
			modifyString( str );
			istringstream iss(str);
			insert( iss, root, true );
		}
		P("Case #%d: %d\n", tc+1,gctr );
	}
	return 0;
}
