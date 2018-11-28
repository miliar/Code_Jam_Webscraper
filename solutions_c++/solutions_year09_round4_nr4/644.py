/*
ID: linjd821
LANG: C++
TASK: 
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <ctype.h>
#include <map>
#include <string>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <fstream>
#include <list>

using  namespace  std;
int n;
typedef struct
{
	double  x, y;
	double  r;
}Point;
Point pt[10];



double dis(int a, int b)
{
	return sqrt((pt[a].x-pt[b].x)*(pt[a].x-pt[b].x)+(pt[a].y-pt[b].y)*(pt[a].y-pt[b].y));
}

int main()
{
	int T, i, CAS = 1;
	double ans;
	//freopen("D1.in", "r", stdin);
	//freopen("D1.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%lf %lf %lf", &pt[i].x, &pt[i].y, &pt[i].r);
		pt[n] = pt[0];
		if(n == 1)
			ans = pt[0].r;
		else if(n == 2)
			ans = max(pt[0].r, pt[1].r);
		else
		{
			ans = 1e20;
			for(i = 0; i < 3; i++)
			{
				double t = (dis(i, i+1)+pt[i].r+pt[i+1].r)/2;
				double tt = pt[(i+2)%3].r;
				double tmp = max(t, tt);
				if(tmp < ans)
					ans = tmp;
			}
		}
		printf("Case #%d: %.6lf\n", CAS++, ans);
	}
	return 0;
} 
