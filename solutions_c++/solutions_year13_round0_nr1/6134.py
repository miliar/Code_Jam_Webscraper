#pragma comment(linker, "/STACK:500000000")
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-9
#define ll long long
#define N 1048581


int  n, i, j, k, open,t, x, y, xx, yy, ok;
char s[10][10];
int gcd(int a, int b){while(b) b^=a^=b^=a%=b;return a;}
int main()
{
	freopen("A-small-attempt4.in.txt", "rt", stdin);
    freopen("A-small-attempt4.out.txt", "wt", stdout);
	scanf("%d", &t);
	n = 4;
	for(int g = 1;g<=t;g++)
	{
		scanf("%s\n%s\n%s\n%s", &s[0], &s[1], &s[2], &s[3]);
		//printf("%s\n%s\n%s\n%s\n", s[0], s[1], s[2], s[3]);
		k = 0;
		ok = 1;
		for(i = 0;i<n;i++)
		{
			x = y = 0;
			for(j = 0;j<n;j++)
			{
				if(s[i][j]=='X')
					x++;
				if(s[i][j] == 'O')
					y++;
				if(s[i][j] == 'T')
					x++, y++;

			}
			k+=x+y;
			if(x==4)
			{
				printf("Case #%d: X won\n", g);
				i = 4;
				ok = 0;
				break;
			}
			if(y==4)
			{
				printf("Case #%d: O won\n", g);
				i = 4;
				ok = 0;
				break;
			}
		}
		if(ok)
		for(i = 0;i<n;i++)
		{
			x = y = 0;
			for(j = 0;j<n;j++)
			{
				if(s[j][i]=='X')
					x++;
				if(s[j][i] == 'O')
					y++;
				if(s[j][i] == 'T')
					x++, y++;

			}
			if(x==4)
			{
				printf("Case #%d: X won\n", g);
				i = 4;
				ok = 0;
				break;
			}
			if(y==4)
			{
				printf("Case #%d: O won\n", g);
				i = 4;
				ok = 0;
				break;
			}
		}
		if(ok)
		{
			x=  y =0;
			for(i = 0;i<n;i++)
			{
	
					if(s[i][i]=='X')
						x++;
					if(s[i][i] == 'O')
						y++;
					if(s[i][i] == 'T')
						x++, y++;
			}
				if(x==4)
				{
					printf("Case #%d: X won\n", g);
					i = 4;
					ok = 0;
				//	break;
				}
				if(y==4)
				{
					printf("Case #%d: O won\n", g);
					i = 4;
					ok = 0;
		//			break;
				}
			
	}
		if(ok)
		{
			x = y = 0;
			for(i = 0;i<n;i++)
			{
	            
					if(s[i][n-1-i]=='X')
						x++;
					if(s[i][n-1-i] == 'O')
						y++;
					if(s[i][n-1-i] == 'T')
						x++, y++;
			}
				if(x==4)
				{
					printf("Case #%d: X won\n", g);
					i = 4;
					ok = 0;
					//break;
				}
				if(y==4)
				{
					printf("Case #%d: O won\n", g);
					i = 4;
					ok = 0;
	//				break;
				}
		}
		if(ok)
		{
			if(k>=16)
				printf("Case #%d: Draw\n", g);
			else
				printf("Case #%d: Game has not completed\n", g);
		}
		//scanf("\n");
	}

	return 0;
}
