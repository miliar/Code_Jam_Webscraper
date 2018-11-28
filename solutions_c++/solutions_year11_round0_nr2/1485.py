#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	int tt = t;
	while(t--)
	{
		int c, d;
		scanf("%d", &c);
		char combine[26][26];
		memset(combine, -1, sizeof(combine));
		while(c--)
		{
			char str[4];
			scanf("%s", str);
			combine[str[0] - 'A'][str[1] - 'A'] = str[2];
			combine[str[1] - 'A'][str[0] - 'A'] = str[2];
		}
		
		scanf("%d", &d);
		bool oppose[26][26];
		memset(oppose, 0, sizeof(oppose));
		while(d--)
		{
			char str[3];
			scanf("%s", str);
			oppose[str[0] - 'A'][str[1] - 'A'] = true;
			oppose[str[1] - 'A'][str[0] - 'A'] = true;
		}
		
		int n;
		scanf("%d", &n);
		int present[26];
		memset(present, 0, sizeof(present));
		char elem[101];
		int id = 0;
		char ch;
		scanf("%c", &ch);
		while(n--)
		{
			scanf("%c", &ch);
			elem[id] = ch;
			id++;
			present[ch - 'A']++;
			if(id == 1)
				continue;
						
			if(combine[elem[id - 1] - 'A'][elem[id - 2] - 'A'] != -1)
			{
				present[elem[id - 1] - 'A']--;
				present[elem[id - 2] - 'A']--;
				elem[id - 2] = combine[elem[id - 1] - 'A'][elem[id - 2] - 'A'];
				id--;
				continue;
			}
			
			for(int i=0; i<26; i++)
			{
				if(oppose[ch - 'A'][i])
				{
					if(present[ch - 'A']>0 && present[i]>0)
					{
						id = 0;
						memset(present, 0, sizeof(present));
					}
				}
			}
		}
		
		if(id == 0)
		{
			printf("Case #%d: []\n", tt-t);
			continue;
		}
		printf("Case #%d: [%c", tt-t, elem[0]);
		
		for(int i=1; i<id; i++)
			printf(", %c", elem[i]);
		
		printf("]\n");	
			
	}
	return 0;
}
