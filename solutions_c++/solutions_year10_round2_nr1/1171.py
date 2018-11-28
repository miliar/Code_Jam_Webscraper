#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char give[15000][101];

void substring(size_t start, size_t stop, const char *src, char *dst, size_t size)
{
   int count = stop - start;
   if ( count >= --size )
   {
      count = size;
   }
   sprintf(dst, "%.*s", count, src + start);
}


int main(int argc, char *argv[]) {
	int num_of_test;
	int n, m;
	int j, count;
	char tmp[101], want[101], dir[101];
	scanf("%d", &num_of_test);
	for (int z = 1; z <= num_of_test; z++) {
		count = 0;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) scanf("%s", give[i]);
		for (int i = 0; i < m; i++) {
			scanf("%s", want);
			for (int j = 1; j < strlen(want); j++) {
				while (want[j] != '/') j++;
				int found = 0;
				substring(0, j, want, dir, sizeof (dir));
				for (int i = 0; i < n; i++) {
					if (strcmp(dir, give[i]) == 0) {
						found = 1;
						break;	
					}
				}
				if (!found) {
					count++;
					strcpy(give[n++], dir);
				}
			}
		}
		printf("Case #%d: %d\n", z, count);
	}
	return 0;
}
