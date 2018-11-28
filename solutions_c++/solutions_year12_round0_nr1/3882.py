#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;

int map[128];
char str[120];

void Init()
{
	int i;
	string ie1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string ie2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string ie3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string ans1 = "our language is impossible to understand";
	string ans2 = "there are twenty six factorial possibilities";
	string ans3 = "so it is okay if you want to just give up";
	for(i = 0; i < ie1.size(); i++)
		map[ ie1[i] ] = ans1[i];
	for(i = 0; i < ie2.size(); i++)
		map[ ie2[i] ] = ans2[i];
	for(i = 0; i < ie3.size(); i++)
		map[ ie3[i] ] = ans3[i];

	map['y'] = 'a'; 
	map['q'] = 'z'; 
	map['e'] = 'o';
	map['z'] = 'q';
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	Init();
	int t,i,j;
	scanf("%d",&t);
	getchar();
	for(i = 1; i <= t; i++)
	{
		gets(str);
		printf("Case #%d: ",i);
		for(j = 0; j < strlen(str); j++)
			printf("%c",map[str[j]]);
		printf("\n");
	}
	return 0;
}