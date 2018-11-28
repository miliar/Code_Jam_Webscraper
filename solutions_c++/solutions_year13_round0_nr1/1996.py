#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

int n=4;
char a[10][10];

int O(int i, int j, char c)
{
	return a[i][j]==c || a[i][j]=='T';
}

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		for (int i=1;i<=n;++i)
			scanf("%s", a[i]+1);
		int ok=0,over=1;
		for (int i=1;i<=n;++i)
		{
			for (int j=1;j<=n;++j)
				over&=(a[i][j]!='.');
			if (O(i,1,'X')&&O(i,2,'X')&&O(i,3,'X')&&O(i,4,'X'))
			{
				ok=1;
				printf("Case #%d: X won\n", _i);
				break;
			}
			if (O(1,i,'X')&&O(2,i,'X')&&O(3,i,'X')&&O(4,i,'X'))
			{
				ok=1;
				printf("Case #%d: X won\n", _i);
				break;
			}
			if (O(i,1,'O')&&O(i,2,'O')&&O(i,3,'O')&&O(i,4,'O'))
			{
				ok=1;
				printf("Case #%d: O won\n", _i);
				break;
			}
			if (O(1,i,'O')&&O(2,i,'O')&&O(3,i,'O')&&O(4,i,'O'))
			{
				ok=1;
				printf("Case #%d: O won\n", _i);
				break;
			}
		}
		if (ok) continue;
		if (O(1,1,'X')&&O(2,2,'X')&&O(3,3,'X')&&O(4,4,'X'))
		{
			ok=1;
			printf("Case #%d: X won\n", _i);
			continue;
		}
		if (O(1,4,'X')&&O(2,3,'X')&&O(3,2,'X')&&O(4,1,'X'))
		{
			ok=1;
			printf("Case #%d: X won\n", _i);
			continue;
		}
		if (O(1,1,'O')&&O(2,2,'O')&&O(3,3,'O')&&O(4,4,'O'))
		{
			ok=1;
			printf("Case #%d: O won\n", _i);
			continue;
		}
		if (O(1,4,'O')&&O(2,3,'O')&&O(3,2,'O')&&O(4,1,'O'))
		{
			ok=1;
			printf("Case #%d: O won\n", _i);
			continue;
		}
		if (over)
			printf("Case #%d: Draw\n", _i);
		else
			printf("Case #%d: Game has not completed\n", _i);
	}	

	return 0;
}
