/*
	Filename: GCJR1A.CPP
	Created:  2011/05/21 09:25
	Author:	  Freshines
*/
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int n, cas, pd, pg, i, j;
int flag[101];
int check(int win, int total)
{
	int i = total*pg%100;
// 	if(i == 0 && total*pg/100 >= win)
// 		return 1;
	i = 100 - i;
	if(!flag[i])
		return 0;
	else 
	{
		if((total+flag[i])*pg/100 >= win)
			return 1;
		else if(!flag[0])
			return 0;
	}
}
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("D:/A-small-attempt3.in", "r", stdin);
		freopen("D:/out.txt", "w", stdout);
	#endif
	cin >> cas;

	for(int ca = 1; ca <= cas; ca++)
	{
		printf("Case #%d: ", ca);
		cin >> n >> pd >> pg;
		memset(flag, 0, sizeof(flag));
		int t = pg;
		int cnt = 0;
		if(pg ==pd)
		{
			puts("Possible");
			continue;
		}
		while(!flag[t%100])
		{
			cnt++; 
			flag[t%100] = cnt;
			t += pg;
		}
		for(i = 1; i <= n; i++)
		{
			if(i*pd%100==0)
			{
				if(check(i*pd/100, i))
				{
	// 				cout << i << endl;
					puts("Possible");
					break;
				}
			}		
		}
		if(i>n)
			puts("Broken");
	}
	return 0;
}