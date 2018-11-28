#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int main()
{
	int cas;
	freopen("B-small-attempt1.in" , "r" , stdin);
	freopen("B-small-attempt1.out" , "w" , stdout);
	//freopen("input.txt" , "r" , stdin);
	//freopen("output.txt" , "w" , stdout);
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		int a[15] , n;
		printf("Case #%d: " , ca);
		scanf("%d" , &n);
		if (n == 0) {printf("0\n"); continue;}
		for (int i = 0; i < n; i ++) scanf("%d" , &a[i]);
		sort(a , a + n);
		int ok = 1;
		for (int i = 1; i < n; i ++)
			if (a[i] == a[i-1]) {ok = 0; break;}
		if (ok)
		{
			int k = 1;
			int min = 2000;
			for (int i = 1; i < n; i ++)
				if (a[i] == a[i-1] + 1) k ++;
				else
				{
					if (k < min) min = k;
					k = 1;
				}
			if (k < min) min = k;
			printf("%d\n" , min);
		}
		else
		{
		
			int b[15];
			for (int i = 0; i < n; i ++) b[i] = i;
			int res = 0;
			do
			{
				int c[15];
				for (int i = 0; i < n; i ++) c[i] = a[b[i]];
				int min = 100;
				int k = 1;
				for (int i = 1; i < n; i ++)
					if (c[i] == c[i-1] + 1) k ++;
					else
					{
						if (k < min) min = k;
						k = 1;
					}
				if (k < min) min = k;
				if (min > res) res = min;
				if (res == n) break;
			}
			while ( next_permutation( b, b + n ) );
			printf("%d\n" , res);
		}
	}
	return 0;
}
