#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
using namespace std;

const int MAX = 130;

int c, d, n;
int change[MAX][MAX];
int erase[MAX][MAX];

int getId(char ch) {
	return ch - 'A' + 1;	
}

char getCh(int id) {
	return (char)(id - 1 + 'A');	
}

int main() {
freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int i, j, cas, iCas, top, len, f;
	char ch1, ch2, ch3;
	char str[MAX];
	char st[MAX];
	scanf("%d", &cas);
	for (iCas = 1; iCas <= cas; ++iCas) {
		memset(change, 0, sizeof(change));
		memset(erase, 0, sizeof(erase));
		scanf("%d", &c);
		for (i = 0; i < c; ++i) {
			scanf(" %c%c%c", &ch1, &ch2, &ch3);
			change[ch1][ch2] = ch3;
			change[ch2][ch1] = ch3;
		}
		scanf("%d", &d);
		for (i = 0; i < d; ++i) {
			scanf(" %c%c", &ch1, &ch2);
			erase[ch1][ch2] = erase[ch2][ch1] = 1;	
		}
		scanf("%d", &len);
		scanf("%s", str);
		top = 0;
		st[top] = str[0];
		for (i = 1; i < len; ++i) {
			if (top >= 0 && change[st[top]][str[i]] != 0)
			   st[top] = change[st[top]][str[i]];
 		    else {
				 f = 0;
				 for (j = 0; j <= top; ++j)
				 	 if (erase[st[j]][str[i]]) {
					 	top = -1;
					 	f = 1;
						 break;							 
				     }
	     		 if (f == 0)
	     		 	st[++top] = str[i];
		    }
		}
		printf("Case #%d: [", iCas);
		if (top >= 0)
		   printf("%c", st[0]);
		for (i = 1; i <= top; ++i) {
			printf(", %c", st[i]);	
		}
		printf("]\n");
    }	
} 