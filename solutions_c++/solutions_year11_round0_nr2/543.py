#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <vector>
#include <map>
#include <set>

#include <algorithm>
#include <cmath>

using namespace std;


char tmp[110];
char g[300][300];
bool bad[300][300];
vector<char> res;


void add(int a, int b, int c)
{
	g[a][b] = g[b][a] = c;
}


bool refresh()
{
	if(res.size() < 2)
	{
		return false;
	}
	char A = res.back();
	res.pop_back();
	char B = res.back();
	res.pop_back();
	char v = g[A][B];
	if(v != -1)
	{
		res.push_back(v);
		return true;
	}
	res.push_back(B);
	res.push_back(A);
	for(int i = 0; i < res.size(); i++)
	{
		for(int j = i + 1; j < res.size(); j++)
		{
			if( bad[ res[i] ][ res[j] ])
			{
				res.clear();
				return true;
			}
		}
	}
	return false;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		for(int i = 'A'; i <= 'Z'; i++)
		{
			for(int j = 'A'; j <= 'Z'; j++)
			{
				g[i][j] = -1;
				bad[i][j] = false;
			}
		}
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			scanf("%s", tmp);
			add(tmp[0], tmp[1], tmp[2]);
		}
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			scanf("%s", tmp);
			bad[ tmp[0] ][ tmp[1] ] = bad[ tmp[1] ][ tmp[0] ] = true;
		}
		scanf("%d", &n);
		scanf("%s", tmp);
		res.clear();
		for(int i = 0; i < n; i++)
		{
			res.push_back(tmp[i]);
			refresh();
		}
		printf("Case #%d: ", testNumber);
		printf("\[");
		for(int i = 0; i < res.size(); i++)
		{
			printf("%c", res[i]);
			if(i + 1 != res.size())
			{
				printf(", ");
			}
		}
		printf("\]\n");
	}
	return 0;
}