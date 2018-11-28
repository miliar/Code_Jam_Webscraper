#include <cstdio>
#include <iostream>

using namespace std;

char table[26];

bool translated[26];

char plaintext[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up z";
char encrypted[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv q";

int main() {
	for(int i=0; encrypted[i] != '\0'; i++) {
		if(encrypted[i] >= 'a' && encrypted[i] <= 'z') {
			table[encrypted[i]-'a'] = plaintext[i];
			translated[plaintext[i]-'a'] = true;
		}
	}
	
	for(int i=0; i<26; i++) {
		if(table[i] == 0) {
			for(int j=0; j<26; j++) {
				if(translated[j] == false) {
					table[i] = j+'a';
					break;
				}
			}
			break;
		}
	}
	
	int N;
	scanf("%d", &N);
	
	for(int i=0; i<N; i++) {
		char str[105];
		cin.getline(str, 104);
		if((str[0] < 'a' || str[0] > 'z') && (str[1] < 'a' || str[1] > 'z')) {
			i--;
			continue;
		}
		
		printf("Case #%d: ", i+1);
		
		for(int j=0; str[j] != '\0'; j++) {
			if(str[j] == ' ')
				printf(" ");
			else
				printf("%c", table[str[j]-'a']);
		}
		
		printf("\n");
	}
}