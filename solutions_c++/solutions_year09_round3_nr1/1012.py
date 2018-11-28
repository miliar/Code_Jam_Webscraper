// PracticeA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include "stdlib.h"

struct st
{
	char ch;
	long value;
}
values[100];

int compareChar(const void *x,const void *y)
{
	char  *a = (char *)x;
	char  *b = (char *)y;
	return *a - *b;
}
long search(char c, long size)
{

	int i;
	for(i = 0;i<size;i++)
		if(values[i].ch == c)
			return values[i].value;

	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("c:\\in.txt","r",stdin);
	freopen("c:\\outAtel.txt","w",stdout);
	char input[100], temp[100], check;
	long test, testcase, len, base, i, j, inc;
	unsigned _int64 res;
	bool flag;
	scanf("%ld", &testcase);
	gets(input);

	for(test=1;test<=testcase;test++)
	{
		printf("Case #%ld: ", test);
		gets(input);
		strcpy(temp, input);
		

		len = strlen(temp);
		qsort(temp,len,sizeof(temp[0]),compareChar);
		
		check = 0;
		
		base = 0;
		for(i=0;i<len;i++)
		{
			if(check != temp[i])
				base++;
			check = temp[i];
		}

		len = strlen(input);
		j = 0;
		flag = false;

		inc = 0;
		for(i=0;i<len;i++)
		{
			if(search(input[i], j) == -1)
			{
				values[j].ch = input[i];
				if(!flag)
				{
					flag = true;
					values[j].value = 1;
				}
				else
				{
					if(inc == 1)
						inc++;
					values[j].value = inc++;
				}
				j++;
			}
		}

		res = 0;
		if(base == 1)
			base = 2;
		for(i=0;i<len;i++)
		{
			res = res*base + search(input[i], j);
		}
		printf("%I64u\n", res);
	}
	return 0;
}

