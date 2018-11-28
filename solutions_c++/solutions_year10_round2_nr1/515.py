#include <iostream>
#include <string>
#include <set>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;

set<string>U;

void ready(string t)
{
	string a = "";
	for(int i = 0; i < t.length(); i++)
	{
		if(a.length() && t[i] == '/')  U.insert(a);
		a.push_back(t[i]);
	}
	U.insert(a);
}

int check(string t)
{
	int res = 0;
	string a = "";
	for(int i = 0; i < t.length(); i++)
	{
		if(a.length() && t[i] == '/') 
		{
			if(U.find(a) == U.end())
			{
				U.insert(a);
				res++;
			}
		}
		a.push_back(t[i]);
	}
	if(U.find(a) == U.end())
	{
		U.insert(a);	
		res++;
	}
	return res;
}

int main()
{

	freopen("d:\\A-large.in", "r", stdin);
	freopen("d:\\A-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		U.clear();	
		int ans = 0;
		scanf("%d%d", &n, &m);
		while(n--)
		{
			string t;
			cin >> t;
			ready(t);
		}
		while(m--)
		{
			string t;
			cin >> t;
			ans += check(t);
		}
		printf("Case #%d: %d\n", ++c, ans);
	}
}