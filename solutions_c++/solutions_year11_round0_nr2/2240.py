#include <stdio.h>
#include <stdlib.h>

int index = 0;
char stack[100];
char comb[26][26];
char coun[26][26];

void push(char ch) {
	stack[index++] = ch;
}
char pop() {
	return stack[--index];
}

void clear() {
	for (int i=0; i<26; i++) {
		for (int j=0; j<26; j++) {
			comb[i][j] = 0;
			coun[i][j] = 0;
		}
	}

	index = 0;
}

void update_stack() {
	// comb first
	if (index <= 1) return;
	while (1) {
		char a = stack[index-1] - 'A';
		char b = stack[index-2] - 'A';

		if (comb[a][b] == 0) break;

		pop(); pop();
		push(comb[a][b]);
	}

	if (index <= 1) return;
	//coun
	char tmp = stack[index-1] - 'A';
	for (int i=0; i<index-1; i++) {
		if (coun[tmp][stack[i]-'A'] == 1) {
			index = 0;
			break;
		}
	}
}

void print_stack() {
	printf("[");

	if (index == 0) {
		printf("]\n");
		return;
	}

	for (int i=0; i<index-1; i++) {
		printf("%c, ", stack[i]);
	}
	printf("%c", stack[index-1]);
	printf("]\n");
}

void main() {
	freopen("B-large.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int num_cases;
	scanf("%d", &num_cases);

	for (int w=0; w<num_cases; w++) {

		clear();

		int comb_num;
		scanf("%d", &comb_num);

		for (int k=0; k<comb_num; k++) {
			char a, b, c;
			scanf(" %c%c%c ", &a, &b, &c);
			
			comb[a-'A'][b-'A'] = c;
			comb[b-'A'][a-'A'] = c;
		}

		int coun_num;
		scanf("%d", &coun_num);

		for (int k=0; k<coun_num; k++) {
			char a, b;
			scanf(" %c%c", &a, &b);
			coun[a-'A'][b-'A'] = 1;
			coun[b-'A'][a-'A'] = 1;
		}

		int length;
		scanf("%d", &length);
		
		char buffer[1000];
		scanf("%s", buffer);
		for (int k=0; k<length; k++) {
			char tmp;
			tmp = buffer[k];
			//printf("char %c \n", tmp);
			push(tmp);

			update_stack();

			//print_stack();
		}

		printf("Case #%d: ", w+1);
		print_stack();
	}

	//system("pause");
}