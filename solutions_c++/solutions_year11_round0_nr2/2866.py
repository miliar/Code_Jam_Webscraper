/*
*	Author:
*   FileName:
*   Create:
*/
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;
int c[27][27], d[27][27], alp[27];
int main()
{
	#ifndef ONLINE_JUDGE
	    freopen("D:/B-large.in", "r", stdin);
// 	   freopen("D:/test.in", "r", stdin);
	   freopen("D:/test.out", "w", stdout);
	#endif
	int cas, len, i, j, pos, D, C;
	string str, d1[30];
	char c1[4], c2[3];
	cin >> cas;
	for(int ca=1l; ca <= cas; ca++)
	{
		printf ("Case #%d: [", ca);
		cin >> C;
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		memset(alp, 0, sizeof(alp));
		while(C--)
		{
			cin >> c1;
			c[c1[0]-'A'][c1[1]-'A'] = c[c1[1]-'A'][c1[0]-'A'] = c1[2];
		}
		cin >> D;
		for(int p = 0; p < D; p++)
		{
			cin >> d1[p];
			d[d1[p][0]-'A'][d1[p][1]-'A'] = d[d1[p][1]-'A'][d1[p][0]-'A'] = 1;
		}
		cin >> len >> str;
		int t=0;
		while(t < str.length())
		{
			alp[str[t]-'A']++;
			if(t<1)
			{	t++;continue;}
			if(c)
			{
				int a = str[t] - 'A';
				int b = str[t-1] - 'A';
			
				if(c[a][b])
				{	
					alp[a]--;
					alp[b]--;
					t -= 1;
					char ch[2];
					ch[0] = c[a][b];
					ch[1] = '\0';
					str.erase(t, 2);
					str.insert(t, ch);
					alp[c[a][b]-'A']++;
					//	t--;
					continue;
				}
			}
			if(d)
			{
				for(int p = 0; p < D; p++)
				{
					if(str[t] == d1[p][0] || str[t] == d1[p][1])
						if(alp[d1[p][0]-'A'] && alp[d1[p][1]-'A'])
						{
							i=0;
							str.erase(i, t-i+1);
							t = -1;
							memset(alp, 0, sizeof(alp));
							break;
						}
				}
			}
			t++;
		}
		t = 0;
		while(str[t])
		{
			if(t)
				putchar(','),putchar(' ');
			putchar(str[t]);
			t++;
		}
		puts("]");
	}
	return 0;
}
