#include<stdio.h>

int isOk(char *s1, char *str)
{
	int fl, j, i;
	char ss[111], ch;
	for(i=0, j=0; s1[i]; i++, j++)
	{
		ch=s1[i];
		if(str[j]=='(')
		{
			j++;
			fl=0;
			while(str[j]!=')')
			{
				if(str[j]==ch)
					fl=1;
				j++;
			}
			if(fl==0)
				return 0;		
		}
		else if(str[j]!=s1[i])
			return 0;
	}
	return 1;
}




char s[33][33], str[33];


int main()
{
	freopen("a.txt", "r", stdin);
	freopen("a.ans", "w", stdout);
	int L, D, tst, t, i, cnt;
	while(scanf("%d %d %d", &L, &D, &tst)==3)
	{
		for(i=0; i<D; i++)
			scanf("%s", s[i]);
		for(t=1; t<=tst; t++)
		{
			scanf("%s", str);
			cnt=0;
			for(i=0; i<D; i++)
				if(isOk(s[i], str))
					cnt++;
			printf("Case #%d: %d\n", t, cnt);
		}
	}
	return 0;
}
