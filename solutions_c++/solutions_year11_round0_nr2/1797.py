//      b.cxx
//      
//      Copyright 2011 crbtmac <crbtmac@ubuntu>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
const int N = 205;

char com[N][N];
bool op[N][N];
char st[N];

void init()
{
	
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			com[i][j] = '#';
	
	memset(op, 0, sizeof(op));
}


bool ok(int loc)
{
	if(com[st[loc]][st[loc-1]] != '#') return true;
	return false;
}

bool ok2(int loc)
{
	for(int i = loc - 1; i >= 0; i--)
		if(op[st[loc]][st[i]]) return true;
	return false;
}

int main(int argc, char **argv)
{
	
	freopen("B-large.in", "r", stdin);
//	freopen("ans", "w", stdout);
	
	int t, i, j, k;
	
	scanf("%d", &t);
	for(int cas = 1; cas <= t; cas++)
	{
		init();
		int c, d;
		scanf("%d", &c);
		while(c--)
		{
			char s[10];
			scanf("%s", s);
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}
		scanf("%d", &d);
		while(d--)
		{
			char s[10];
			scanf("%s", s);
			op[s[0]][s[1]] = op[s[1]][s[0]] = true;
		}
		
		scanf("%d", &d);
		scanf("%s", st);
		//cout << st << endl;
		int loc = 1;
		int len = strlen(st);
		char cnt[N];
		while(loc < len)
		{
			
			if(ok(loc))
			{
				//cout << "ok\n";
				st[loc-1] = com[st[loc]][st[loc-1]];
				for(i = loc + 1; i < len; i++)
					st[i-1] = st[i];
				st[i-1] = 0;
				len = i-1;
				loc = 1;
				//cout << st << endl;
			}
			else if(ok2(loc))
			{
				//cout << "ok2\n";
				j = 0;
				for(i = loc + 1; i < len; i++)
					st[j++] = st[i];
				st[j] = 0;
				len = strlen(st);
				loc = 1;
				//cout << st << endl;
			}
			else loc++;
		}
		
		printf("Case #%d: ", cas);
		len = strlen(st);
		printf("[");
		for(i = 0; i < len; i++)
		{
			printf("%c", st[i]);
			if(i != len - 1) printf(", ");
			//else printf("\n");
		}
		printf("]\n");
		
		
	}
	
	return 0;
}

