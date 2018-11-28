//============================================================================
// Name        : gcj2012a.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#define inf 1<<25;
#define max(a,b) ((a)>(b)?(a):(b));
#define min(a,b) ((a)>(b)?(a):(b));
#define sqr(x) ((x)*(x));
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(x) (printf("Case #%d: ",(x)++));
using namespace std;

char a[]="yhesocvxduiglbkrztnwjpfmaq\0";
int vis[26];
char s[1000];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int txt,i,len,cas=1;
	scanf("%d",&txt);getchar();
	while(txt--)
	{
		gets(s);
		print(cas);
		len=strlen(s);
		for(i=0;i<len;i++)
		{
			if(s[i]!=' ')
			{
				printf("%c",a[s[i]-'a']);
			}
			else
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}
