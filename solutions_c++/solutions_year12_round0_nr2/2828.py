// DancingWiththeGooglers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

inline bool canReach(int score, int p)
{
	return (score + 2) / 3 >= p;
}

inline bool canReachSpecial(int score, int p)
{
	return (score + 4) / 3 >= p && score >= p;
}

int main(int argc, char* argv[])
{
	int t, n, s, p, g[101], r;//why did I use an array?
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		r = 0;
		cin>>n>>s>>p;
		for (int j = 0; j < n; j++)
		{
			cin>>g[j];
			if (canReach(g[j], p))
				r++;
			else if (s && canReachSpecial(g[j], p))
			{
				r++;
				s--;
			}
		}
		cout<<"Case #"<<i<<": "<<r<<endl;
	}
	return 0;
}

