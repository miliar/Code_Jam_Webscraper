/*
Author:MarsChenly
Date:2012.04.14
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>

using namespace std;

const int maxn(1005);

const char s[maxn] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv\0"};
const char t[maxn] = {"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up\0"};

char trans[26];
char S[maxn],T[maxn];

void prepare()
{
	int len = strlen(s);
	cout << len << endl;
	for (int i = 0; i < len ;i++)
	if (s[i] != ' ')
	{
		trans[s[i] - 'a'] = t[i];
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	prepare();
	int task;
	scanf("%d\n",&task);
//	trans['o'-'a'] = 'e';
	trans['z' - 'a'] = 'q';
	trans['q' - 'a'] = 'z';
//	for (int i = 0; i < 26; i++)
//	     cout  << (char)(i + 'a') << trans[i] << endl;

	for (int cnt = 1; cnt <= task; cnt++)
	{
		cin.getline(S,maxn,'\n');
//		cout << "S = " << S << endl;
		
		int len = strlen(S);
		for (int i = 0; i < len ;i++)
		if (S[i] == ' ')
		{
			T[i] = ' ';
		} else
		{
			T[i] = trans[S[i] - 'a'];
		}
		T[len] = '\0';
		printf("Case #%d: %s\n",cnt,T);
	}
	return 0;
}
