#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int t;
char st[30];
int i,j;
void swap(int p1, int p2)
{
	char temp = st[p1];
	st[p1] = st[p2];
	st[p2] = temp;
}
int compare(const void *p1, const void *p2)
{
	return (*(char *)p1) - (*(char *)p2);
}
void special()
{
	int mm,p;
	mm = 9999999;
	int ll = strlen(st);
	for (int i = 0; i <= ll - 1; ++i)
		if (st[i] != '0' && st[i] < mm)
		{
			mm = st[i];
			p = i;
		}
	swap(0, p);
	st[ll] = st[1];
	st[1] = '0';
	st[ll + 1] = 0;
	qsort(st + 2, ll - 1, sizeof(char), compare);

	
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&t);
	for (int ll = 1; ll <=t; ++ll)
	{
	gets(st);
	bool flag;
	flag=false;
	int length = strlen(st);
	for (i = length - 1; i >= 0; --i)
		if (st[i] < st[i+1]) 
		{
			flag = true;
			break;
		}
	if (flag == false)
	{
		special();
		printf("Case #%d: %s\n",ll, st);
		continue;
	}
	int minnum = 99999;
	for (int k = length - 1; k > i; --k)
		if (st[k] < minnum && st[k] > st[i])
		{
			minnum = st[k];
			j = k;
		}
	swap(i, j);
	for (int k = i + 1; k <= (i + length - 1) / 2; ++k) swap(k, (length -k + i));
	printf("Case #%d: %s\n",ll, st);
	}
	return 0;
}