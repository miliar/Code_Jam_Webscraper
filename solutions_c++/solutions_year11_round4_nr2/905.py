#include <vector>
#include <algorithm>
#include <stdio.h>
#include <iostream>

using namespace std;

#define RC 500

int t, r, c;
double w[RC][RC];
double d;
double x, y, dx, dy, cx, cy;
char cc;


int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		cin >> r >> c >> d;
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
			{
				cin >> cc;
				w[i][j] = cc - '0';
				w[i][j] += d;
			}
		bool isOk = false;
	   	for(int k = min(r, c); k >= 3; k--)
	   	{
			x = y = 0;
	   		for(int l = 0; l <= c - k; l++)
	   		{
	   			for(int t = 0; t <= r - k; t++)
	   			{
					cx = (k % 2 == 0) ? l + k / 2 : l + k / 2 + 0.5;
					cy = (k % 2 == 0) ? t + k / 2 : t + k / 2 + 0.5;

	   				x = y = 0.0;

	   				for(int i = 0; i < k; i++)
	   					for(int j = 0; j < k; j++)
	   					{
	   						if((i == 0 || i == k - 1) && (j == 0 || j == k 
- 1))
	continue;
	   						dx = (double) (i + l) + 0.5 - cx;
 							dy = (double) (j + t) + 0.5 - cy;
 							x += dx * w[t + j][l + i];
 							y += dy * w[t + j][l + i];
	   					}
	    	   	   if(x == 0 && y == 0)
			  	   {
	   	    			 isOk = true;
				   	      printf("Case #%d: %d\n", test, k);
				   	      break;
			   	   }	   				

	   			}
	   			if(isOk)
	   				break;
	   		}
	   		if(isOk)
	   			break;
	   	}
	   	if(!isOk)
	   		printf("Case #%d: IMPOSSIBLE\n", test);
	}
	return 0;
}