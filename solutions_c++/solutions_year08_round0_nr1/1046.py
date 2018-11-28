#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <queue>
#include <map>
#include <utility>
using namespace std;
#define rep(x,from,to,step) for(int x=(from);x<(to);x+=(step))
#define all(x) (x).begin(),(x).end()


map < string, int > names;
int numNames, numQueries;
vector < int >queries;

void clear()
{
	names.clear();
	queries.clear();
}

void read()
{
	int  tmp;
	char buf[1024];
	scanf("%d", &numNames);
	fgets(buf, 1024, stdin);

	tmp = 0;
	while(tmp++ < numNames) {
		fgets(buf, 1024, stdin);
		buf[strlen(buf)-1]=0;
		names[string(buf)] = tmp;
	}
	scanf("%d", &numQueries);
	fgets(buf, 1024, stdin);
	queries.resize(numQueries + 10);
	tmp = 0;
	while(tmp < numQueries) {
		fgets(buf, 1024, stdin);
		buf[strlen(buf)-1]=0;
		if(names.count(string(buf)))
			queries[tmp++] = names[string(buf)];
		else
			queries[tmp++] = -1;
	}
}

int findLastSeen(int pos)
{
	int seen[110];
	int num = 0, loop;
	for(int a = 0; a < 110; a++)
		seen[a] = 0;

	for(loop = pos; loop < numQueries && num < numNames; loop++) {
		if(queries[loop] >= 0)
			if(!seen[queries[loop]]) {
				seen[queries[loop]] = 1;
				num++;
			}
	}
	if(num==numNames)
		return loop-1;
	else return loop;
}

int doStuff()
{
	int swaps = 0;
	int tmp = 0;
	while(tmp < numQueries) {
		tmp = findLastSeen(tmp);
		swaps++;
	}

	return max(swaps - 1,0);

}

int main()
{
	int cases, a = 0;
	scanf("%d", &cases);
	while(a++ < cases) {
		clear();
		read();
		printf("Case #%d: %d\n", a, doStuff());

	}

}
