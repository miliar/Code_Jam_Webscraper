#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

bool alreadyMap[256];
char mapChar[256];
char baris[105];

bool doMap(char sourceStr[], char targetStr[])
{
	int lenS = strlen(sourceStr);
	int lenT = strlen(targetStr);
	if (lenS != lenT) return false;
	int i;
	for (i = 0; i < lenS; i++) {
		if (alreadyMap[sourceStr[i]]) {
			if (mapChar[sourceStr[i]] != targetStr[i]) return false;
		}
		else {
			mapChar[sourceStr[i]] = targetStr[i];
			alreadyMap[sourceStr[i]] = true;
		}
	}
	return true;
}

int main()
{
	freopen("Ainput.txt", "r", stdin);
	freopen("Aoutput.txt", "w", stdout);
	bool validStatement = true;
	int nc, tc;
	int i, len;
	for (i = 0; i < 256; i++)
		mapChar[i] = i;
	validStatement = validStatement && doMap("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	validStatement = validStatement && doMap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	validStatement = validStatement && doMap("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	validStatement = validStatement && doMap("qz", "zq");
	if (!validStatement) {
		puts("somethings go wrong...");
		system("pause");
		return 0;
	}
	scanf("%d", &tc);
	gets(baris);
	for (nc = 1; nc <= tc; nc++) {
		gets(baris);
		len = strlen(baris);
		for (i = 0; i < len; i++)
			baris[i] = mapChar[baris[i]];
		printf("Case #%d: %s\n", nc, baris);
	}
}
