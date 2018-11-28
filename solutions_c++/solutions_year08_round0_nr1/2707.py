#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char s[1008][108];
char q[1008][108];
bool m[1008];

void my_gets(char* s)
{
	gets(s);
	int t = strlen(s);
	while(t > 0 && (s[t - 1] == '\r' || s[t - 1] == '\n'))
	{
		s[t - 1] = 0;
		t--;
	}
}

int cmp(const void* a, const void* b)
{
	return strcmp((char*)a, (char*)b);
}

int find_str(int total_num, char* str)
{
	int low = 0;
	int high = total_num - 1;
	while (low <= high)
	{
		int mid = (low + high) >> 1;
		if (strcmp(s[mid], str) < 0)
		{
			low = mid + 1;
		}
		else if (strcmp(s[mid], str) > 0)
		{
			high = mid - 1;
		}
		else
		{
			return mid;
		}
	}
	return -1;
}
int main()
{
	int test_case;
	int s_num, q_num;
	scanf("%d", &test_case);
	int test_num = 1;
	while (test_case--)
	{
		scanf("%d", &s_num);
		for (int i = 0; i < s_num; i++)
		{
			my_gets(s[i]);
			if (s[i][0] == 0 || s[i][0] == '\r' || s[i][0] == '\n') 
			{
				i--;
				continue;
			}
		}
		scanf("%d", &q_num);
		for (int i = 0; i < q_num; i++)
		{
			my_gets(q[i]);
			if (q[i][0] == 0 || q[i][0] == '\r' || q[i][0] == '\n')
			{
				i--;
				continue;
			}

		}

		qsort((void *)s, s_num, sizeof(s[0]), cmp);
		int c = 0;
		memset(m, 0, sizeof(m));
		for (int i = 0; i < q_num; i++)
		{

			int j = 0;
			/*
			   for (j = 0; j < s_num; j++) {
			   if (strcmp(q[i], s[j]) == 0) {
			   m[j] = 1;
			   break;
			   }
			   }*/
			int t = find_str(s_num, q[i]);
			m[t] = 1;

			for (j = 0; j < s_num; j++)
			{
				if (m[j] == 0) {
					break;
				}
			}

			if (j == s_num)
			{
				c++;
				memset(m, 0, sizeof(bool) * s_num);
			}
		}
		// Case #1: 1
		printf("Case #%d: %d\n", test_num++, c);
	}
	return 0;
}

