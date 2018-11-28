#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <cstring>

using namespace std;

#define all(x) (x).begin(),(x).end()

map<int,int> M,M2;

string solve(string g)
{
	for(int i = 0; i < (int)g.length(); i++)
		g[i] = M[g[i]];
	return g;
}

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi|rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd|de kr kd eoya kw aej tysr re ujdr lkgc jv|yeqz";
string b = "our language is impossible to understand|there are twenty six factorial possibilities|so it is okay if you want to just give up|aozq";

void init()
{
	for(int i = 0; i < (int)a.length(); i++)
	{
		M[a[i]] = b[i];
		M2[b[i]] = a[i];
	}
	for(int c = 'a'; c <= 'z'; c++)
	{
		if( M[c] == 0) printf("alarm! %c\n",c);
		if( M2[c] == 0) printf("alarm2! %c\n",c);
	}
}

int main()
{	
	init();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	string g;
	cin >> t; 
	getline(cin,g);
	for(int i = 0; i < t; i++)
	{
		getline(cin,g);
		g = solve(g);
		printf("Case #%d: %s\n",i+1,g.c_str());
	}
	return 0;
}
