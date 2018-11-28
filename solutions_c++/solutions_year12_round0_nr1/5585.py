#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

int mm[256];

void ready()
{
	string a[3], b[3];

	a[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	a[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	a[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	b[0] = "our language is impossible to understand";
	b[1] = "there are twenty six factorial possibilities";
	b[2] = "so it is okay if you want to just give up";

	memset(mm, -1, sizeof(mm));

	for(int i = 0; i < 3; i++)
	{
		for(int j = 0; j < a[i].length(); j++)
		{
			mm[a[i][j]] = b[i][j];
		}
	}

	mm['z'] = 'q';
	mm['q'] = 'z';
}

int main()
{
	freopen("C:\\Users\\litstrong\\Desktop\\GCJ\\A-small-attempt1.in", "r", stdin);
	freopen("C:\\Users\\litstrong\\Desktop\\GCJ\\A-small-attempt1.out", "w", stdout);

	ready();

	/*
	for(int i = 'a'; i <= 'z'; i++)
		printf("%c %c\n", i, mm[i]);
		*/

	int T;
	//cin >> T;
	scanf("%d\n", &T);
//	cin >> T;

	int c = 0;
	while(T--)
	{
		char ch[105];
		gets(ch);

		printf("Case #%d: ", ++c);
		for(int i = 0; i < strlen(ch); i++)
		{
			if(ch[i] == ' ')  printf(" ");
			else  printf("%c", mm[ch[i]]);
		}

		printf("\n");
	}
}