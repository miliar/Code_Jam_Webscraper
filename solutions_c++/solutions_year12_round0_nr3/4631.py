#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;
int tot;

char str[15], str2[15];

int val()
{
    int ret = 0;
    int i;
    int len = strlen(str);
    for(i = 0; i < len; i++)
    {
        ret = ret * 10 + (str[i] - '0');
    }
    return ret;
}

int getval(int x, int y)
{
    int i, j, yy;
    sprintf(str, "%d", x);
    int len = strlen(str);

    for(i = 1; i < len; i++)
    {
        char tmp = str[0];
        for(j = 0; j < len - 1; j++)
        {
            str[j] = str[j + 1];
        }
        str[j] = tmp;
        yy = val();
        if(y == yy)
        {
            //printf("%d %d\n", x, y);
            return 1;
        }
    }
    return 0;
}

int main()
{
	int i, j, k;
	freopen("c-small-attempt0.in", "rt", stdin);
	freopen("c-small.out", "wt", stdout);

	int inp, kase;
	int a, b;
	scanf("%d", &inp);
	gets(str);
	for(kase = 1; kase <= inp; kase++)
	{
	    tot = 0;
		scanf("%d %d", &a, &b);
		for(i = a; i <= b; i++)
		{
		    for(j = i + 1; j <= b; j++)
                tot += getval(i, j);
		}
		printf("Case #%d: %d\n", kase, tot);
	}
	return 0;
}
