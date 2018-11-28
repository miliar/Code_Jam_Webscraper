#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

int first(vector<string>& V, int start, string what)
{
	while(start<V.size())
		if(V[start]==what)
			break;
		else
			start++;
	return start;
}

int main()
{
	int N,S,Q,i,j;
	char buf[200];
	scanf("%d",&N);
	for(i = 1; i <= N; i++)
	{
		int res = 0;
		scanf("%d\n", &S);
		vector<string> engines;
		vector<string> queries;
		for(j=0;j<S;j++)
			gets(buf), engines.push_back(buf);
		scanf("%d\n", &Q);
		for(j=0;j<Q;j++)
			gets(buf), queries.push_back(buf);
		//copy(engines.begin(),engines.end(),ostream_iterator<string>(cout," "));cout<<endl;
		//copy(queries.begin(),queries.end(),ostream_iterator<string>(cout," "));

		int pos = 0;
		while(pos!=queries.size())
		{
			int bestv=-1;
			for(j=0;j<engines.size();j++)
				if(first(queries, pos, engines[j])>bestv)
					bestv = first(queries, pos, engines[j]);
			pos = bestv;
			res++;
		}

		printf("Case #%d: %d\n", i, res-1);
	}

	return 0;
}