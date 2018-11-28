#include <cstdio>
#include <string.h>
using namespace std;

const char hash[] = "yhesocvxduiglbkrztnwjpfmaq";
int t;
char ch[200];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	fgets(ch, sizeof(ch), stdin);
	for(int i = 0; i < t; ++i){
		fgets(ch, sizeof(ch), stdin);
		int len = strlen(ch);
		for(int j = 0; j < len; ++j)
			if(ch[j] != ' ') ch[j] = hash[ch[j] - 'a'];
		printf("Case #%d: %s\n", i + 1, ch);
		//fputs(ch, stdout);
	}
	return 0;
}

