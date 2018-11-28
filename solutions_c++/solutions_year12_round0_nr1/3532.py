#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;
char str[111];
int main(){
	int TC;
	scanf("%d\n", &TC);
//	a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
	char mp[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	for(int tc=1; tc<=TC; tc++){
		fgets(str, 111, stdin);	
		printf("Case #%d: ", tc);
		//printf("%s\n", str);
		for(int i=0; i<strlen(str); i++){
			if(str[i] == ' ')
				printf(" ");
			else
				printf("%c", mp[str[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
