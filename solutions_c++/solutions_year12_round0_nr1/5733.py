#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main( )
{
	int t, tt;
	char g[105], s[105];
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	//char chars[27] = "abcdefghijklmnopqrstuvwxyz";
	scanf("%d\n", &tt);
	for(t = 1; t <= tt; t++)
	{
		memset(s, 0, sizeof(s));
		memset(g, 0, sizeof(g));
		cin.getline (s, 105);
		for (int i = 0; i < sizeof(s); i++)
		{
			if (s[i] == ' ') g[i] = s[i];
			else 
			{
				switch (s[i])
				{
					case 'a': g[i] = 'y'; break;
					case 'b': g[i] = 'h'; break;
					case 'c': g[i] = 'e'; break;
					case 'd': g[i] = 's'; break;
					case 'e': g[i] = 'o'; break;
					case 'f': g[i] = 'c'; break;
					case 'g': g[i] = 'v'; break;
					case 'h': g[i] = 'x'; break;
					case 'i': g[i] = 'd'; break;
					case 'j': g[i] = 'u'; break;
					case 'k': g[i] = 'i'; break;
					case 'l': g[i] = 'g'; break;
					case 'm': g[i] = 'l'; break;
					case 'n': g[i] = 'b'; break;
					case 'o': g[i] = 'k'; break;
					case 'p': g[i] = 'r'; break;
					case 'q': g[i] = 'z'; break;
					case 'r': g[i] = 't'; break;
					case 's': g[i] = 'n'; break;
					case 't': g[i] = 'w'; break;
					case 'u': g[i] = 'j'; break;
					case 'v': g[i] = 'p'; break;
					case 'w': g[i] = 'f'; break;
					case 'x': g[i] = 'm'; break;
					case 'y': g[i] = 'a'; break;
					case 'z': g[i] = 'q'; break;
				}
			}
		}
		printf("Case #%d:", t);
        printf(" %s\n", g);
	}

	return 0;
}