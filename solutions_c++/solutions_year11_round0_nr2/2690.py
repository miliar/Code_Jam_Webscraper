#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>
#include <queue>
#include <stack>
#include <list>
#include <deque>
#include <set>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <utility>
#include <cassert>
#include <time.h>
using namespace std;

#define  max(a,b)  ((a)>(b)?(a):(b))
#define  min(a,b)  ((a)<(b)?(a):(b))
#define out(x) (cout << #x << " = " << x <<endl)
const int inf = 0x3f3f3f3f;
const double eps = 1e-10;
#define N 100005

int a[1002];

int main()
{
	int T;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	cin >> T;
	int cases = 1;

	while(T--)
	{
	    int c,d,n,i,j;
		map<pair<char,char>,char>com;
		map<char,char>opp;
		cin >> c;
        while(c--)
		{
			char x,y,z;
			cin >> x >> y >> z;
            com[make_pair(x,y)] = z;
			com[make_pair(y,x)] = z;
		}
		cin >> d;
		while (d--)
		{
			char x,y;
			cin >> x >> y;
			opp[x] = y;
			opp[y] = x;
		}
		cin >> n;
	    char ans[205],tmp;
		int len  = -1;
		for(i = 0; i < n; i++)
		{
			cin >> tmp;
            if(len == -1)
			{
				ans[++len] = tmp;
			}
			else
			{
				bool flag = false;

				if( (com[make_pair(tmp,ans[len])] >= 'A' && com[make_pair(tmp,ans[len])] <= 'Z') )
				{ 
					ans[len] = com[make_pair(tmp,ans[len])];
					flag = true; 
				}
			  	if( (com[make_pair(ans[len],tmp)] >= 'A' && com[make_pair(ans[len],tmp)] <= 'Z') )
				{
					ans[len] = com[make_pair(ans[len],tmp)]; flag = true; 
				}
                if(!flag)
				{
					bool flag2 = true;
					for(j = len; j >= 0; j--)
					{
						if(opp[tmp] == ans[j])
						{
							len = -1;
							flag2 = false;
							break;
						}
					}
					if(flag2) ans[++len] = tmp;
				}
			}
		}
		printf("Case #%d: [",cases++);
	    if(len == -1)
			puts("]");
		else if(len == 0)
		{
			printf("%c]\n",ans[0]);
		}
		else
		{
           printf("%c",ans[0]);
		   for(i = 1; i <= len; i++)
		   {
			   printf(", %c",ans[i]);
		   }
		   puts("]");
		}
	}
	return 0;
}
