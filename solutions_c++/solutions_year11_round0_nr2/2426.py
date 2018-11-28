#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

char str[101];
int go[26][26];
bool opposed[26][26];

int main()
{
	freopen("problem_2.in", "r", stdin);
	freopen("problem_2.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int test=1; test<=tests; ++test)
	{
		memset(go, -1, sizeof(go));
		memset(opposed, 0, sizeof(opposed));
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; ++i)
		{
			scanf("%s", str);
			go[str[0]-'A'][str[1]-'A']=str[2]-'A';
			go[str[1]-'A'][str[0]-'A']=str[2]-'A';
		}
		scanf("%d", &n);
		for(int i=0; i<n; ++i)
		{
			scanf("%s", str);
			assert(str[0]!=str[1]);
			opposed[str[0]-'A'][str[1]-'A']=true;
			opposed[str[1]-'A'][str[0]-'A']=true;
		}
		scanf("%d%s", &n, str);
		vector<char> cur_str;
		for(int i=0; i<n; ++i)
		{
			cur_str.pb(str[i]);
			bool processed=false;
			while((cur_str.size()>=2)&&(go[cur_str[cur_str.size()-2]-'A'][cur_str[cur_str.size()-1]-'A']!=-1))
			{
				char ch='A'+go[cur_str[cur_str.size()-2]-'A'][cur_str[cur_str.size()-1]-'A'];
				cur_str.pop_back(), cur_str.pop_back(), cur_str.pb(ch);
				processed=true;
			}
			if(!processed)
			{
				for(int j=0; j<cur_str.size()-1; ++j)
					if(opposed[cur_str[j]-'A'][cur_str[cur_str.size()-1]-'A'])
					{
						cur_str.clear();
						break;
					}
			}
		}
		printf("Case #%d: [", test);
		if(!cur_str.empty())
		{
			for(int i=0; i<cur_str.size()-1; ++i)
				printf("%c, ", cur_str[i]);
			printf("%c", cur_str[cur_str.size()-1]);
		}
		printf("]\n");

	}
	return 0;
}