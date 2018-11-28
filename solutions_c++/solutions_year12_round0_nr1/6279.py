#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

#define MAXN 100

int	mp[MAXN]={24,7,4,18,14,2,21,23,3,
20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main()
{
	int text;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d\n",&text);
	char s[MAXN];
	for(int t=1;t<=text;t++)
	{
		gets(s);
		int i,j;
		int len=strlen(s);
		for(i=0;i<len;i++)
		{
			if(s[i]==' ')	continue;
			s[i]=mp[s[i]-'a']+'a';
		}
		printf("Case #%d: %s\n",t,s);
	}
	return 0;
}
