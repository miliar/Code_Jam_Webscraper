#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

template<class It>
int maxstep(It first, It end, const vector<string>& engines)
{
	int maxstep = 0;
	for (size_t i=0;i<engines.size();i++)
	{
		It it = first;
		while (it != end && engines[i].compare(*it) != 0) it++;
		maxstep = max(maxstep, distance(first, it));
	}
	return maxstep;
}

int main()
{
	int N;
	scanf("%d\n", &N);
	for (int n=0;n<N;n++)
	{
		int S;
		scanf("%d\n", &S);
		vector<string> se;
		for (int i=0;i<S;i++)
		{
			char name[128];
			gets(name);
			se.push_back(name);
		}

		int Q;
		scanf("%d\n", &Q);
		vector<string> queries;
		for (int i=0;i<Q;i++)
		{
			char name[128];
			gets(name);
			queries.push_back(name);
		}

		int sw=0;
		for (vector<string>::iterator it = queries.begin(); it != queries.end();)
		{
			int s = maxstep(it, queries.end(), se);
			it = it+s;
			if (it != queries.end()) sw++;
		}

		printf("Case #%d: %d\n", n+1, sw);
	}

	return 0;
}
