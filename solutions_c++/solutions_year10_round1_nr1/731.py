#include <algorithm>
#include <functional>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <iostream>

using namespace std;

int tc, n, k;
char b[51][51], tr[51][51];

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &tc);
	for(int T = 1; T <= tc; ++T)
	{
		memset(tr, ' ', sizeof(tr));
		scanf("%d %d", &n, &k);
		for(int i = 0; i < n; ++i)
			scanf("%s", &b[i]);
		for(int i = n - 1; i >= 0; --i)
			for(int j = n - 1, cur = n - 1; j >= 0; --j)
				if(b[i][j] != '.')
					tr[cur--][n - i - 1] = b[i][j];
		bool red = false, blue = false;
		for(int i = n - 1; i >= 0; --i)
			for(int j = n - 1; j >= 0; --j)
				if(tr[i][j] == 'R' || tr[i][j] == 'B')
				{
					//kanan
					int ii = i, jj = j, cur = 1;
					while(jj + 1 < n && tr[ii][jj + 1] == tr[i][j])
					{
						++cur;
						++jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//kanan bawah
					ii = i; jj = j; cur = 1;
					while(ii + 1 < n && jj + 1 < n && tr[ii + 1][jj + 1] == tr[i][j])
					{
						++cur;
						++ii;
						++jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//bawah
					ii = i; jj = j; cur = 1;
					while(ii + 1 < n && tr[ii + 1][jj] == tr[i][j])
					{
						++cur;
						++ii;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//kiri bawah
					ii = i; jj = j; cur = 1;
					while(ii + 1 < n && jj - 1 >= 0 && tr[ii + 1][jj - 1] == tr[i][j])
					{
						++cur;
						++ii;
						--jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//kiri
					ii = i; jj = j; cur = 1;
					while(jj - 1 >= 0 && tr[ii][jj - 1] == tr[i][j])
					{
						++cur;
						--jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//kiri atas
					ii = i; jj = j; cur = 1;
					while(ii - 1 >= 0 && jj - 1 >= 0 &&  tr[ii - 1][jj - 1] == tr[i][j])
					{
						++cur;
						--ii;
						--jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//atas
					ii = i; jj = j; cur = 1;
					while(ii - 1 >= 0 && tr[ii - 1][jj] == tr[i][j])
					{
						++cur;
						--ii;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
					//kanan atas
					ii = i; jj = j; cur = 1;
					while(ii - 1 >= 0 && jj + 1 < n && tr[ii - 1][jj + 1] == tr[i][j])
					{
						++cur;
						--ii;
						++jj;
					}
					if(cur == k)
					{
						if(tr[i][j] == 'R')
							red = true;
						else
							blue = true;
					}
				}
		printf("Case #%d: ", T);
		if(!red && !blue)
			printf("Neither\n");
		else if(red && blue)
			printf("Both\n");
		else if(red)
			printf("Red\n");
		else
			printf("Blue\n");
	}
	return 0;
}
