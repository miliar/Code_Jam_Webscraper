#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<climits>
#include<algorithm>
#include<map>
using namespace std;

char trans[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 
				   'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

char str[101010];

void conduct() {
	int i;
	gets(str);
	for (i = 0; i < strlen(str); ++i) 
		if (str[i] >= 'a') str[i] = trans[str[i]-'a'];
	printf("%s\n", str);
}

int main() {
	int time;
	scanf("%d", &time); gets(str);
	for (int i = 1; i <= time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	} return 0;
}
