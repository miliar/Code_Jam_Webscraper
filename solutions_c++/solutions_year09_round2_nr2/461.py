#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int number[10];
int now[10];

int cmp(const char &n1, const char &n2)
{
	return n1 > n2;
}

int main()
{
	int tcase, i, j, tno, n, t, maxv;
	char buf[100], buf2[100];
	
	scanf("%d", &tcase);
	for (tno = 1; tno <= tcase; tno++)
	{
		scanf("%s", buf2);

		strcpy(buf, buf2);
		for (i = strlen(buf) - 2; i >= 0; i--)
		{
			sort(buf + i, buf + strlen(buf), cmp);
			if (strcmp(buf2, buf))
			{
				//printf("%s\n", buf);
				strcpy(buf, buf2);
				maxv = i + 1;
				for (j = i + 2; j < strlen(buf); j++)
					if (buf[j] > buf[i] && buf[j] < buf[maxv])
						maxv = j;
				swap(buf[i], buf[maxv]);
				sort(buf + i + 1, buf + strlen(buf));
				
				printf("Case #%d: %s\n", tno, buf);
				break;
			}
			
		}
		if (i < 0)
		{
				
				maxv = 0;
				for (j = 1; j < strlen(buf); j++)
					if (buf[j] != '0' && buf[j] < buf[maxv])
						maxv = j;
				swap(buf[0], buf[maxv]);
				sort(buf + 1, buf + strlen(buf));
				printf("Case #%d: %c0%s\n", tno, buf[0], buf + 1);
		}
		/*
		sort(buf + 1, buf + strlen(buf), cmp);
		if (strcmp(buf2, buf) == 0)
		{
			
		}*/
	}
	
	return 0;
}
