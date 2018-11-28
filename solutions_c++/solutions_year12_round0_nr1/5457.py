#include <stdio.h>
using namespace std;

char match[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g',
		'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

int main(void) {
	FILE *in = fopen("in", "r");
	FILE *out = fopen("out", "w");

	int T;
	char S[105];
	fscanf(in, "%d\n", &T);

	for (int Q = 1; Q <= T; Q++) {
		fgets(S, 105, in);
		
		for(int i=0; i<101; i++){
			if(S[i]=='\0'){
				S[i-1] = '\0';
			}else if(S[i] != ' '){
				S[i] = match[S[i]-'a'];
			}
		}
		
		fprintf(out, "Case #%d: %s\n", Q, S);

	}
	return 0;
}
