#include <stdio.h>
#include <string.h>

const int MaxL=16;
const int MaxD=50001;
const int MaxN=501;

char code[MaxD][MaxL];
bool testarr[MaxL][26];

inline void readin(int);
inline int fcounter(int , int);
inline bool find(char *str);
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);
	readin(d);
	for(int i=0; i<n; i++)
	{
		printf("Case #%d: %d\n", i+1, fcounter(l, d));
	}
	return 0;
}
inline void readin(int d)
{
	for(int i=0; i<d; i++)
	{
		scanf("%s", code[i]);
	}
}
inline int fcounter(int l, int d)
{
	memset(testarr, false, sizeof(testarr));

	int counter=0;
	char strin[MaxL*40];

	scanf("%s", strin);
	int j=0, v=0;
	while(strin[j]!='\0')
	{
		if(strin[j]=='(')
		{
			j++;	
			while(strin[j]!=')')	
				testarr[v][strin[j++]-'a']= true;
			j++;
		}
		else
		{
			testarr[v][strin[j++]-'a']= true;
		}
		v++;
	}
	for(int i=0; i<d; i++)
		if(find(code[i]))	counter++;
	return counter;
}

inline bool find(char *str)
{
	int i=0;
	while(str[i]!='\0')
	{
		if(!testarr[i][str[i]-'a']) return false;
		i++;
	}
	return true;
}