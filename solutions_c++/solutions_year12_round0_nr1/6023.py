#include <stdio.h>
#include <string.h>

int main()
{//다 푼거애여?응 노가다햇어
	int testcase, i, j, len;

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	scanf_s("%d\n", &testcase);
	for(i = 1; i <= testcase; i++){
		char G[101] = {0,};
		gets(G); len = strlen(G);
		for(j = 0; j < len; j++){
			switch(G[j]){
			case 'a': G[j] = 'y';break;
			case 'b': G[j] = 'h';break;
			case 'c': G[j] = 'e';break;
			case 'd': G[j] = 's';break;
			case 'e': G[j] = 'o';break;
			case 'f': G[j] = 'c';break;
			case 'g': G[j] = 'v';break;
			case 'h': G[j] = 'x';break;
			case 'i': G[j] = 'd';break;
			case 'j': G[j] = 'u';break;
			case 'k': G[j] = 'i';break;
			case 'l': G[j] = 'g';break;
			case 'm': G[j] = 'l';break;
			case 'n': G[j] = 'b';break;
			case 'o': G[j] = 'k';break;
			case 'p': G[j] = 'r';break;
			case 'q': G[j] = 'z';break;
			case 'r': G[j] = 't';break;
			case 's': G[j] = 'n';break;
			case 't': G[j] = 'w';break;
			case 'u': G[j] = 'j';break;
			case 'v': G[j] = 'p';break;
			case 'w': G[j] = 'f';break;
			case 'x': G[j] = 'm';break;
			case 'y': G[j] = 'a';break;
			case 'z': G[j] = 'q';break;
			}
		}
		printf("Case #%d: ", i);
		puts(G);
	}
	return 0;
}