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
struct node
{
	int id, b;
}f[210];
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
	   freopen("D:/A-large.in", "r", stdin);
		freopen("D:/test.out", "w", stdout);
	#endif
	int O[200], t, B[200], n, i, j, cas, lenb, leno;
	char str[4];
	cin >> cas;
	for(int ca = 1; ca <= cas; ca++)
	{
		printf("Case #%d: ", ca);
		cin >> n;
		lenb = leno = 0;
		for(i = 0; i < n; i++)
		{
			scanf("%s%d", str, &f[i].b);
			if(str[0]=='B')
			{
				f[i].id = 1;
				B[lenb++] = i;
			}
			else
			{
				f[i].id = 2;
				O[leno++] = i;
			}
		}
		int time = 0;
// 		int preb = 1, preo = 1;
// 		while(i < lenb && j < leno)
// 		{
// 			
// 		}

		i = j = 0;
		int pob = 1, poo=1, freeb=0, freeo=0;
		for(i = 0; i < n; i++)
		{
			if(f[i].id==1)                   //b
			{
				int temptime = time;
				int t = abs(f[i].b - pob);
				if(freeb < t)
					time += t - freeb;
				freeb = 0;
				time++;
				freeo += time - temptime;
				pob = f[i].b;
			}
			else                   //o
			{
				int temptime = time;
				int t = abs(f[i].b - poo);
				if(freeo < t)
					time += t - freeo;
				time++;
				freeb += time - temptime;
				freeo = 0;
				poo = f[i].b;
			}
		}
		printf("%d\n", time);
	}
	return 0;
}