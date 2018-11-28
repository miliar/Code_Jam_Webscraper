#include <stdio.h>
#include <string.h>

char reference[] = {"welcome to code jam"};
char line[550];

int cache[550][30];

int counthem (int ref, int ln) {
	if (ref == -1) return 1;
	if (ln == -1) return 0;

	if (cache[ref][ln] != -1)
		return cache[ref][ln];

	int local_count = 0;

	if (reference[ref] == line[ln]) {
		local_count = (local_count + counthem(ref-1,ln-1))%10000;
	}
	local_count += counthem (ref,ln-1);

	return cache[ref][ln] = local_count;
}

int main () {

	int cases;
	
	scanf ("%d\n",&cases);

	int end2 = strlen(reference);
	for (int i = 0; i < cases; i++) {
		memset(cache,-1,sizeof(cache));
		fgets (line, sizeof(line),stdin);

		int end = strlen(line)-1;
		if (line[end] == '\n') end--;

		printf ("Case #%d: %04d\n",i+1,counthem(end2-1,end));
	}

	return 0;
}
