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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

int n, s, q;

char name[108][108], quest[108], temp[108];
int main()
{
	scanf("%d", &n);
	for(int r=1; r<=n; r++)
	{
		map<string, int> _map;
		scanf("%d", &s);
		getchar();
		for(int i=0; i<s; i++)
			gets(name[i]);
		scanf("%d", &q);
		getchar();
		int min=0;
		int t=0, tt=0;
		for(int i=0; i<q; i++)
		{
			gets(quest);
			string str=(string)quest;
			_map[str]++;
			if(_map[str]==1)
				t++;
			if(t==s)
			{
				min++;
				_map.clear();
				_map[str]++;
				t=1;
	
			}
		}
		printf("Case #%d: %d\n",r, min); 
	}
	return 0;
}