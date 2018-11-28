#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

char a[100][100];

int main()
{
	freopen("problem_1.in", "r", stdin);
	freopen("problem_1.out", "w", stdout);
	int n, m, t;
	scanf("%d", &t);
	for(int it=1; it<=t; ++it)
	{
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; ++i)
			scanf("%s", a[i]);
		for(int i=0; i<n-1; ++i)
			for(int j=0; j<m-1; ++j)
				if((a[i][j]=='#')&&(a[i+1][j]=='#')&&(a[i][j+1]=='#')&&(a[i+1][j+1]=='#'))
				{
					a[i][j]='/'; a[i][j+1]='\\';
					a[i+1][j]='\\'; a[i+1][j+1]='/';
				}
		bool ok=true;
		for(int i=0; i<n; ++i)
			for(int j=0; j<m; ++j)
				if(a[i][j]=='#')
					ok=false;
		printf("Case #%d:\n", it);
		if(!ok)
			printf("Impossible\n");
		else
		{
			for(int i=0; i<n; ++i)
				printf("%s\n", a[i]);
		}
	}
	return 0;
}