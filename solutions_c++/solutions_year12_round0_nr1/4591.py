/*
 * a.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: appemax
 */
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int MAXN = 300;

char S[MAXN];

char ss1[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi"};
char ss2[]={"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"};
char ss3[]={"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char s1[]={"our language is impossible to understand"};
char s2[]={"there are twenty six factorial possibilities"};
char s3[]={"so it is okay if you want to just give up"};

char F[30];

inline char getChange(char x)
{
	if(x<='z' && x>='a')
		x = F[x-'a'];
	return x;
}

void initial()
{
	int i, l;

	for(i=0; i<26; i++)
		F[i] = 'z';

	l = strlen(ss1);
	for(i=0; i<l; i++)
		if(ss1[i]<='z' && ss1[i]>='a')
			F[ss1[i]-'a'] = s1[i];
	l = strlen(ss2);
	for(i=0; i<l; i++)
		if(ss2[i]<='z' && ss2[i]>='a')
			F[ss2[i]-'a'] = s2[i];
	l = strlen(ss3);
	for(i=0; i<l; i++)
		if(ss3[i]<='z' && ss3[i]>='a')
			F[ss3[i]-'a'] = s3[i];
	F[25] = 'q';
	return;
}

int main()
{
	int t , i, j;

	initial();

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("a.out", "w+", stdout);
	scanf("%d", &t);
	getchar();
	for(i=0; i<t; i++)
	{
		gets(S);
		for(j=0; S[j]!='\0'; j++)
			S[j] = getChange(S[j]);
		printf("Case #%d: ", i+1);
		puts(S);
	}
	return 0;
}

