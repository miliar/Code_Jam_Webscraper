
#include <stdio.h>

#define MAX 100000

int l,d,n;
char pattern[MAX];

int main(int argc, char **argv)
{
	scanf("%i %i %i", &l, &d, &n);
	char words[d][l+1];
	for (int i=0; i<d; i++) {
		scanf("%s", words[i]);
	}
	for (int i=0; i<n; i++) {
		scanf("%s", pattern);		
		bool match, gmatch;
		int matches=0;
		for (int j=0; j<d; j++) {
			char* s = pattern;
			gmatch=true;
			for (int k=0; k<l; k++) {
				match = false;
				if (*s == '(') {
					s++;
					while (*s != ')') {
						if (*s == words[j][k]) match=true;
						s++;
					} 
					s++;
				} else {
					if (*s == words[j][k]) match=true;
					s++;
				}
				gmatch = gmatch && match;
			}
			if (gmatch) matches++;		
		}		
		printf("Case #%i: %i\n", i+1, matches);
	}
	return 0;
}
