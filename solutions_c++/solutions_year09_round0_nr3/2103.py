#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char welcome[] = "welcome to code jam";
char line[550];
int lenw, lenl;
unsigned __int64 cnt;

void go(int l, int w){
	if(w == lenw){
		cnt = ++cnt % 10000;
		return;
	}
	if(l == lenl)
		return;

	for(; (lenl - l) >= (lenw - w); l++){
		if(line[l] == welcome[w])
			go(l +1, w + 1);
	}
}

int main(){
	freopen("C-small.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);
	
	lenw = strlen(welcome);
	int N;
	gets(line);
	N = atoi(line);
	for(int n = 1; n <= N; n++){
		gets(line);
		cnt = 0;
		lenl = strlen(line);
		go(0, 0);
		printf("Case #%d: %04I64u\n", n, cnt % 10000 );
	}
	
	return 0;
}