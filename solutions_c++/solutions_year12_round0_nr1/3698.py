#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <functional>

#define maxn 200

using namespace std;

int n;
char to_go[] = "yhesocvxduiglbkrztnwjpfmaq";
char tmp[maxn];

int main(){
	freopen("rand.in", "r", stdin);
	freopen("rand.out", "w", stdout);

	scanf("%d", &n);
	gets(tmp);
	for(int test = 1; test <= n; ++test){
		gets(tmp);
		printf("Case #%d: ", test);
		int len = strlen(tmp);
		for(int i = 0; i < len; ++i)
			if(tmp[i] != ' ')printf("%c", to_go[int(tmp[i] - 'a')]);
			else printf(" ");
		printf("\n");
	}

	return 0;
}