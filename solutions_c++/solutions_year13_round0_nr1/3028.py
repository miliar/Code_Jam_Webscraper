#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <queue>
#include <vector>
#include <set>
#define maxn
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

char s[10][10];

bool check(char x)
{
	for (int i=1;i<=4;i++)
	{
		bool flag = true;
		for (int j=1;j<=4;j++)
			if (s[i][j]!=x&&s[i][j]!='T')
			{
				flag = false;
				break;
			}

		if (flag) return true;
	}

	for (int i=1;i<=4;i++)
	{
		bool flag = true;
		for (int j=1;j<=4;j++)
			if (s[j][i]!=x&&s[j][i]!='T')
			{
				flag = false;
				break;
			}

		if (flag) return true;
	}

	bool flag = true;
	for (int i=1;i<=4;i++)
		if (s[i][i]!=x&&s[i][i]!='T')
		{
			flag = false;
			break;
		}

	if (flag) return true;

	flag = true;

	for (int i=1;i<=4;i++)
		if (s[i][4-i+1]!=x&&s[i][4-i+1]!='T')
		{
			flag = false;
			break;
		}

	if (flag) return true;

	return false;
}

bool isOver()
{
	for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
			if (s[i][j]=='.')
				return false;
	return true;
}

int main()
{
    freopen("C:\\Users\\py\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\py\\Desktop\\output.txt","w",stdout);

   	int tt;
   	cin >> tt;
   	for (int id=1;id<=tt;id++)
   	{
   		for (int i=1;i<=4;i++)
   			scanf("%s",s[i]+1);

   		printf("Case #%d: ",id);
   		if (check('X'))
   		{
   			printf("X won\n");
   		} else
   		if (check('O'))
   		{
   			printf("O won\n");
   		} else
   		if (isOver())
   		{
   			printf("Draw\n");
   		} else
   		printf("Game has not completed\n");

   	}

    return 0;
}
