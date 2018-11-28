#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

char map[30] = "ynficwlbkuomxsevzpdrjgthaq";
int main(){
	int T, len;
	char str[100];
	char c;
	scanf("%d", &T);
	scanf("%c", &c);
	for(int t = 0; t<T; t++){
		for(int i = 0; ;i++){
			scanf("%c", &c);
			if(c == '\n'){
				len = i;
				str[i] = 0;
				break;
			}
			str[i] = c;
		}
		for(int i = 0; i < len; i++){
			if(str[i] == ' ') continue;
			for(int j = 0; j < 26; j++){
				if(str[i] == map[j]){
					str[i] = 'a' + j;
					break;
				}
			}
		}
		printf("Case #%d: %s\n", t + 1, str);
	}
	return 0;
}

