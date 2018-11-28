#include<iostream>
#include <string.h>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int ma[200];

void init()
{
	memset(ma,0,sizeof(ma));
	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string b = "our language is impossible to understand";
	for(int i = 0 ; i < a.size(); i ++)
		ma[a[i]] = b[i];
	a = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	b = "there are twenty six factorial possibilities";
	for(int i = 0 ; i < a.size(); i ++)
		ma[a[i]] = b[i];
	a = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	b = "so it is okay if you want to just give up";
	for(int i = 0 ; i < a.size(); i ++)
		ma[a[i]] = b[i];
	ma['q'] = 'z';
	ma['z'] = 'q';
//	for(int i = 0 ; i < 200; i ++)
//		printf ("%c : %c\n",i,ma[i]);
}

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("a.out","w",stdout);
	int cas = 1;
	init();
	char s[110];
	int t;
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		gets(s);
		for(int i = 0 ; s[i]; i ++)
			s[i] = ma[s[i]];
		printf ("Case #%d: ",cas++);
		puts(s);
	}
	return 0;
}