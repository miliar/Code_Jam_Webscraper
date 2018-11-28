#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#define mp(a, b) make_pair(a, b)
#define pair_mst pair <int, pair <int, int> >

using namespace std;

int main()
{
	int t, n, c, d, p = 0;
	char form[40], op[30], input[105], temp[3];
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		p++;
		map <pair <char, char>, int> ops;
		map <pair <char, char>, char> red;
		char arr[105];
		
		scanf("%d", &c);
		for (int i = 0; i < c; i++)
		{
			scanf("%s", form);
			sort(form, form + 2);
			red[mp(form[0], form[1])] = form[2];
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
		{
			scanf("%s", op);
			sort(op, op + 2);
			ops[mp(op[0], op[1])] = 1;
		}
		scanf("%d", &n);
		scanf("%s", input);
		int counter = 0;
		for (int i = 0; i < n; i++)
		{
			arr[counter] = input[i];
			if (counter > 0)
			{
				temp[0] = arr[counter-1];
				temp[1] = arr[counter];
				sort(temp, temp + 2);
				if (red[mp(temp[0], temp[1])])
				{
					arr[counter-1] = red[mp(temp[0], temp[1])];
					continue;
				}
				int flag = 0;
				for (int j = 0; j < counter; j++)
				{
					temp[0] = arr[j];
					temp[1] = arr[counter];
					sort(temp, temp + 2);
					if (ops[mp(temp[0], temp[1])])
					{
						flag = 1;
						counter = 0;
					}
				}
				if (!flag)
					counter++;
			}
			else
				counter++;
		}
		printf("Case #%d: [", p);
		for (int i = 0; i < counter; i++)
		{
			if (i)
				printf(", ");
			printf("%c", arr[i]);
		}
		printf("]\n");
	}

   return 0;
}
