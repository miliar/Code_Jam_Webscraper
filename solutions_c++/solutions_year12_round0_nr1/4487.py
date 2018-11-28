
#include<stack>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<utility>
#include<map>
#include<cmath>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
	int mapr[200]={0};
	string a="ejp mysljylc kd kxveddknmc re jsicpdrysi",b="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",c="de kr kd eoya kw aej tysr re ujdr lkgc jv",a1="our language is impossible to understand",b1="there are twenty six factorial possibilities",c1="so it is okay if you want to just give up";
	for(int i=0;i<a.size();i++)
	{
		mapr[a[i]] = a1[i];
	}
	for(int i=0;i<b.size();i++)
	{
		mapr[b[i]] = b1[i];
	}
	for(int i=0;i<c.size();i++)
	{
		mapr[c[i]] = c1[i];
	}
	mapr['q'] = 'z';
	mapr['z'] = 'q';
	int t;
	cin >> t;
		char x[100];
	gets(x);
	int j;
	for(j=1;j<=t;j++)
	{
		char s1[1500];
		gets(s1);
		printf("Case #%d: ",j);
		for(int i=0;i<strlen(s1);i++)
		{
			printf("%c",mapr[s1[i]]);
		}
		printf("\n");
	}
	return 0;
}
