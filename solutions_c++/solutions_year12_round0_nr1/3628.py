#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
	return (*(char*)a) - (*(char*)b);
}

char Googlerese1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysiqz";
char Googlerese2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char Googlerese3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char English1[] = "our language is impossible to understandzq";
char English2[] = "there are twenty six factorial possibilities";
char English3[] = "so it is okay if you want to just give up";

char Translation[30];

void Map(char Googlerese[], char English[])
{
	int i;
	int Len = strlen(Googlerese);

	for (i=0; i<Len; i++)
	{
		Translation[Googlerese[i] - 'a'] = English[i];
	}
}

void MakeMap()
{
	Map(Googlerese1,English1);
	Map(Googlerese2,English2);
	Map(Googlerese3,English3);
}

void DisMap()
{
	
	int i;
	
	for (i=0; i<26; i++)
	{
		printf("%c->%c\n", 'a' + i, Translation[i]);
	}
}

void Translate(char Googlerese[], char English[])
{
	int i;
	int Len = strlen(Googlerese);
	
	for (i=0; i<Len; i++)
	{
		if (Googlerese[i] == ' ')
		{
			English[i] = ' ';
			continue;
		}
		English[i] = Translation[Googlerese[i] - 'a'];
	}
	English[Len] = '\0';
}

int main()
{
	freopen("D://download//A-small-attempt0.in", "r", stdin);
	freopen("D://download//A-small-attempt0.out", "w", stdout);
	int T;
	int i;
	char Googlerest[110];
	char English[110];
	MakeMap();
	//DisMap();
	scanf("%d", &T);
	getchar();
	
	for (i=0; i<T; i++)
	{
		gets(Googlerest);
		Translate(Googlerest, English);
		printf("Case #%d: %s\n", i + 1, English);
	}
	return 0;
}