#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
char needle[20] = "welcome to code jam";
char haystack[503];
int matches = 0;

void findS(int posN, int posH){
	if (posN == 19){
		matches++;
		return;
	}
	int len = 0;
	while (haystack[len] != '\n')
		len++;
	for (int i = posH; i < len; i++)
		if (haystack[i] == needle[posN])
			findS(posN+1, i+1);
}
int main(){
	int N;
	scanf ("%d", &N);
	getchar();
	for (int x = 0; x < N; x++){
		char temp = 'a';
		int i = 0;
		while (temp != '\n'){
			scanf("%c", &temp);
			haystack[i] = temp;
			i++;
		}
		matches = 0;
		findS(0, 0);
		matches%=10000;
		printf("Case #%d: %04d\n",x+1, matches);
	}
	return 0;
}
