#include <stdio.h>
#include <string.h>

char inp[30];

void _sort(char a[], int n)
{
	int i, j, t;

	for(i = 0; i < n; i++)
		for(j = i+1; j < n; j++)
		{
			if(a[i] > a[j])
			{
				t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
		}
}

void process()
{
	int i, j, len, max, mem;
	char temp[30];

	max = -1;
	len = strlen(inp);
	strcpy(temp, inp);
	for(i = len-1; i >= 0; i--)
	{
		if(inp[i]-'0' < max) break;
		if(inp[i]-'0' > max) max = inp[i]-'0';
	}
	if(i < 0)
	{
		inp[len] = '0';
		len++;
		inp[len] = '\0';
		for(i = len-1; i >= 0; i--)
			if(inp[i] != '0') break;
		mem = inp[0];
		inp[0] = inp[i];
		inp[i] = mem;
		_sort(&inp[1], len-1);
	}
	else
	{
		for(j = len-1; j >= 0; j--)
			if(inp[i] < inp[j]) break;

		mem = inp[i];
		inp[i] = inp[j];
		inp[j] = mem;
		_sort(&inp[i+1], len-i-1);
	}
}

int main()
{
	int z, t;

	t = 1;
	scanf("%d", &z);
	while(z > 0)
	{
		scanf("%s", inp);
		process();
		printf("Case #%d: %s\n", t++, inp);
		z--;
	}

	return 0;
}