#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <queue>

using namespace std;

char maps[26] = {'y','h', 'e', 's', 'o', 'c', 'v',
				 'x', 'd', 'u', 'i', 'g', 'l', 'b',
				 'k', 'r', 'z', 't', 'n', 'w',
				 'j', 'p', 'f', 'm', 'a', 'q'};
int main(void){
	freopen("A-small-attempt1.in", "rb", stdin);
	freopen("result.txt", "w", stdout);
	char line[1024];
	int T, k = 0;
	scanf("%d", &T);
	getchar();
	while(k++ < T){
		gets(line);
		for(int i = 0; line[i] != '\0'; ++i)
			if(line[i] != ' ')
				line[i] = maps[line[i] - 'a'];
		printf("Case #%d: %s\n", k, line);
	}
	return 0;
}
