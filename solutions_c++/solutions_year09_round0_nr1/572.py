#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>
#include <stdio.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for((a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))

string s;
bool a[5001][16][26];
bool ok[5001];
bool tmpok[5001];
int l, d, n;

int main()
{
	cin >> l >> d >> n;
	
	memset(a, false, sizeof(a));
	RP(i, d)
	{
		cin >> s;
		RP(j, s.sz) a[i][j][s[j]-'a'] = true;
	}
		
	RP(test, n)
	{
		memset(ok, true, sizeof(ok));
		cin >> s;
		int pos = 0;
		int pp = 0;

		while(pp < s.sz)
		{
			if (s[pp] != '(')
			{
				RP(j, d)
				{					
					ok[j] = ok[j] && a[j][pos][s[pp]-'a'];					
				}
			}
			else
			{
				pp++;
				memset(tmpok, false, sizeof(tmpok));
				while (s[pp] != ')')
				{					
					RP(j, d)
					{
						tmpok[j] = tmpok[j] || a[j][pos][s[pp]-'a'];
					}
					pp++;
				}
				RP(i, d) { ok[i] = ok[i] && tmpok[i]; }

			}
			
			pp++;
			pos++;
		}

		int res = 0;
		RP(j, d) res += ok[j];
		
		printf("Case #%d: %d\n", test+1, res);				
	}
}
