#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define ford(i, n) for(int i = (int)n -1; i>=0 ; i--)
#define pb push_back 
#define mp make_pair
#define se second
#define fi first
#define ll long long

#include <vector>
#include <list>
#include <map>
#include <set>
//#include <multiset>
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
#define sss 2000000
using namespace std;
 
 int t, n, a[20000], b[20000], m;
 char s[1000];
 int table[600][600];
 int d[600][600];
 int r[600][600];
 int maxsquare[600][600];
 int sizes[600];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	forn(tn, t)

	{
		scanf("%d%d", &m, &n);
		
		forn(i, m+5)
			forn(j, n+5)
				table[i][j] = -100;
		forn(i, m)
		{ 
			scanf("%s", s);
			forn(j, n/4){
				int tm;
				if (s[j]>='A'&&s[j]<='F')
					tm = 10+s[j]-'A';
				else
					tm = s[j] - '0';
				table[i][4*j] = (tm&8)/8;
				table[i][4*j+1] = (tm&4)/4;
				table[i][4*j+2] = (tm&2)/2;
				table[i][4*j+3] = tm&1;
			}
		}
		/*forn(i, m)
		{
			forn(j, n)
				printf("%d", table[i][j]);
			printf("\n");
		}*/
		forn(i, m+5)
			forn(j, n+5)
				r[i][j] = 0, d[i][j] = 0,maxsquare[i][j] = 0;
		ford(i, m)
			ford(j, n)
			{
				r[i][j] = 1+ (table[i][j]!=table[i][j+1]? r[i][j+1]:0);
				d[i][j] = 1+ (table[i+1][j]!=table[i][j]? d[i+1][j]:0);
				maxsquare[i][j] = min(min(r[i][j], d[i][j]), (table[i+1][j+1]==table[i][j]?maxsquare[i+1][j+1]:0)+1);
			}
		/*forn(i, m)
		{
			forn(j, n)
				printf("%d", maxsquare[i][j]);
			printf("\n");
		}*/
		int maxsize = min(n, m)+5;
		forn(i, maxsize+10)
			sizes[i+1] = 0;
		ford(s, maxsize)
		{
			forn(i, m)
				forn(j, n)
					if (table[i][j]>=0&&maxsquare[i][j]>s)
						if ((table[i][j+s]>=0)&&(table[i+s][j+s]>=0)&&(table[i+s][j]>=0))
						{
							sizes[s+1]++;
							forn(ii, s+1)
								forn(jj,s+1)
									table[i+ii][j+jj] = -100;
						}
			

		
		}
		printf("Case #%d: ", tn+1);
		int ans = 0;
		ford(s, maxsize)
			if (sizes[s+1]!=0)
				ans++;

		printf("%d", ans);
		printf("\n");
		ford(s, maxsize)
			if (sizes[s+1]!=0)
				printf("%d %d\n", s+1, sizes[s+1]);

	}
	return 0;
}
