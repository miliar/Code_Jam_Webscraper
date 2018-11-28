//speaking.cpp
//By λKT345

#include<cstdio>

const int MAL=28;

char tra[MAL]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
			   'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	int T;
	char temp;
	scanf("%d\n", &T);
	for(int i=1; i<=T; i++) {
		printf("Case #%d: ", i);
		while(scanf("%c", &temp)!=0&&temp!='\n'){
			if('a'<=temp&&temp<='z') {
				printf("%c", tra[temp-'a']);
			} else {
				printf("%c", temp);
			}
		}
		printf("\n");
	}
	return 0;
}
