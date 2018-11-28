#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;


#define _CRT_SECURE_NO_WARNINGS
#define Fill(a,c) memset(&a, c, sizeof(a))
#define All(v) (v).begin(), (v).end()
#define foreach(it,X) for(it = (X).begin(); it != (X).end(); ++it) 
#define rforeach(it,X) for(it = (X).rbegin(); it != (X).rend(); ++it)
//value = *it

struct Point
{
	long x;
	long y;
};

char buf[1024] = "/0";
void main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int iNum = atoi(gets(buf));
	for(int n=1; n<=iNum; n++) 
	{
		int i, P, K, L;

		scanf("%d %d %d", &P, &K, &L);

		list<long> mylist;
		list<long>::reverse_iterator it;

		for(i = 0; i < L; i++)
		{
			scanf("%s ", buf);
			 mylist.push_back(atol(buf));
		}

		

		int iResult = 0;
		int iKey = 0;
		int iMax = P - 1;

		mylist.sort();
		rforeach(it,mylist)
		{
			iResult += (*it) * (P - iMax);
			++iKey;
			if(iKey >= K)
			{
				iKey = 0;
				--iMax;
			}
		}
		printf("Case #%d: %d", n, iResult);

		printf("\n");
	}

}
