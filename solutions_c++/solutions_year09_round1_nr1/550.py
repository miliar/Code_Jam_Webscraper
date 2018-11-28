#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

char flag[3000001][11];
bool visit[701];

int happy(int num, int base)
{	
	if(num <= 3000000 && flag[num][base] != -1)
		return flag[num][base];

	if(num <= 700 && visit[num])
	{
		flag[num][base] = 0;
		return 0;
	}
	else if(num <= 700)
		visit[num] = true;
	
	int sum = 0;
	int j;
	do
	{
		j = num % base;
		sum += (j * j);
		num /= base;
	} while(num);
	if(sum == 1)
	{
		flag[num][base] = 1;
		return 1;
	}
	else
	{
		flag[num][base] = happy(sum, base);
		return flag[num][base];
	}
}


int main()
{
	int i,j,c;
	char line[100];
	int bases[10];
	char * sep = " \t";
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	memset(flag, -1, sizeof(flag));
	int cases;
	scanf("%d", &cases);
	gets(line);
	memset(visit, 0, sizeof(visit));
	for (int t = 1; t <= cases; t++)
	{
		gets(line);
		c=0;
		char * token = strtok(line, sep);
		while(token)
		{
			bases[c++] = atoi(token);
			token = strtok(NULL, sep);
		}
		for(i = 2; ;i++)
		{
			for(j = 0; j < c; j++)
			{
				memset(visit, 0, sizeof(visit));
				if(happy(i, bases[j]))
					continue;
				else
					break;
			}
			if(j == c)
				break;
		}
		printf("Case #%d: %d\n", t, i);
	}
	return 0;
}