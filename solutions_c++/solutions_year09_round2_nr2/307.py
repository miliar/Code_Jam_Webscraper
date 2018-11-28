#include <stdio.h>
#include <string.h>

int t, l;
char s[30];

int minx(int pos)
{
	for(int i=pos+1; i<l; i++)
		if (s[i]<s[pos]) pos=i;
	return pos;
}

int maxx(int pos)
{
	for(int i=pos+1; i<l; i++)
		if (s[i]>s[pos]) pos=i;
	return pos;
}

int nxt(int pos)
{
	int val=s[pos];
	for(int i=pos; i<l; i++)
		if ((s[i]>val) && ((s[pos]==val) || (s[i]<s[pos]))) pos=i;
	return pos;
}

void swap(int a, int b)
{
	// printf("%d %d\n", a, b);
	char dummy=s[a];
	s[a]=s[b];
	s[b]=dummy;
}

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		s[0]='0';
		scanf(" %s", s+1);
		l=strlen(s);
		int pos=l-2;
		while(maxx(pos)==pos) pos--;
		swap(pos, nxt(pos));
		for(int i=pos+1; i<l; i++)
			swap(i, minx(i));
		if (s[0]=='0')
			printf("Case #%d: %s\n", cs, s+1);
		else
			printf("Case #%d: %s\n", cs, s);
	}
	return 0;
}
