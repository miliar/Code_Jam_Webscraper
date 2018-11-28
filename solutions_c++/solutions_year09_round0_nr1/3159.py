#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()

using namespace std;
int L, D, N;
vector<string> d;

vector<string> LL( string x )
{
	vector<string> R;
	for( int i = 0; i< x.length(); i++ )
	{	string tmp = "A";
		tmp[0] = x[i];
		if( x[i] == '(' )
		{
			int u = x.find(")", i + 1);
			R.push_back( x.substr(i + 1, u - i - 1) );
			i = u ;
		}	
		else R.push_back(tmp);
	}	
	return R;
}

bool cud( char c, string x)
{
	for(int i=0; i<x.length(); i++)
		if( c== x[i]) return true;
		
	return false;	
}

int F( string x )
{
	vector<string> V = LL( x );	
	int res = 0;
	for(int i = 0; i<d.size(); i++)
	{
		bool ok = 1;
		for( int j= 0; j< V.size(); j++)	
		{
			if( !cud( d[i][j], V[j]) ) 
			{
				ok = 0;
			}
		}
		if( ok ) res++;
	}
	return res;
}
int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

	//cin >> L >> D >> N;
	scanf("%d %d %d", &L, &D, &N);
	d.resize(D);
	for( int i = 0; i< D; i++ )
		cin >> d[i];
		
	for( int i = 1; i<= N; i++ )
	{
		string tmp;
		cin >> tmp;
		printf("Case #%d: %d\n", i, F(tmp));	
	}
	
//system("pause");
return 0;
}
