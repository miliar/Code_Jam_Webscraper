
#include "cstdio"


int main(int argc, char *argv[]) {
  freopen(argv[1], "r", stdin);

	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		char t[128][128];
		bool opposition[128][128];
		char input[5100];
		char current[5100];
		for (int i = 0; i < 128; i++) {
			for (int j = 0; j < 128; j++) {
				t[i][j] = 0;
				opposition[i][j] = 0;
			}
		}
		for (int i = 0; i < 5100; i++) {
			input[i] = 0;
			current[i] = 0;
		}

		int cn;
  	scanf("%d", &cn);
		//printf("%d\n", cn);
  	for (int ci = 1; ci <= cn; ci++) {
	  	scanf("%s", input);
			//printf("%d %s\n", ci, input);

			t[input[0]][input[1]] = input[2];
			t[input[1]][input[0]] = input[2];
		}

		int dn;
  	scanf("%d", &dn);
  	for (int di = 1; di <= dn; di++) {
	  	scanf("%s", input);

			opposition[input[0]][input[1]] = true;
			opposition[input[1]][input[0]] = true;
		}

		int inputlen;
  	scanf("%d", &inputlen);
  	scanf("%s", input);

		int len = 0;

		//read the first
		for (int i = 0; i < inputlen; i++) {
			current[len] = input[i];
			len++;

			if (len > 1) {
				if (t[current[len-2]][current[len-1]] != 0) {
					current[len-2] = t[current[len-2]][current[len-1]];
					len--;
					continue;
				}

				for (int i = 0; i <= len-2; i++) {
					if (opposition[current[len-1]][current[i]]) {
						len=0;
						continue;
					}
				}
			}
		}

		current[len] = 0;

		printf("Case #%d: [", ti);
		for (int i = 0; i < len; i++) {
			printf("%c", current[i]);
			if (i != len-1) {
				printf(", ");
			}
		}
		printf("]\n");

	}


	return 0;
}





