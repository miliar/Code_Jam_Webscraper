#include <stdio.h>
#include <string.h>

#define BUF_SIZE 10000

int mapping[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

char buffer[BUF_SIZE];

void read_line()
{
	fgets(buffer, BUF_SIZE, stdin);
	buffer[strlen(buffer) - 1] = '\0';
}

int main()
{
	int N = 0;
	read_line();
	
	sscanf(buffer, "%d", &N);
	
	for (int i = 0; i < N; i++) {
		read_line();
		
		for (int j = 0; j < strlen(buffer); j++) {
			int a = buffer[j];
			a -= 'a';
			if (a >= 0 && a < 26) {
				buffer[j] = (char)(mapping[a] + 'a');
			}
		}
		
		printf("Case #%d: %s\n", i + 1, buffer);
	}
}