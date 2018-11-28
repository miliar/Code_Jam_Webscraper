#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

char line[65536];
int buf[1000000];
FILE* fp;

void get_arrange(int n)
{
	int idx = n - 1;
	for (int i=0; i<n; ++i) {
		int nj = i % (n - i) + 1;
		for (int j=0; j<nj; ++j) {
			do {
				idx = (idx + 1) % n;
			} while (buf[idx] >= 0);
		}
		buf[idx] = i+1;
	}
}

void test()
{
	int n = atoi(fgets(line, sizeof(line), fp));
	int num;
	fscanf(fp, "%d", &num);
	assert(num <= 100);
	int sub[100];
	for (int i=0; i<num; ++i)
		fscanf(fp, "%d", &sub[i]);

	for (int i=0; i<n; ++i)	buf[i] = -1;
	get_arrange(n);

	for (int i=0; i<num; ++i) {
		printf(" %d", buf[sub[i]-1]);
	}
	printf("\n");

	fgets(line, sizeof(line), fp);
}


int main(int argc, char* argv[])
{
	fp = fopen(argv[1], "r");

	int n = atoi(fgets(line, sizeof(line), fp));
	for (int i=0; i<n; ++i) {
		printf("Case %d:", i+1);
		test();
	}

	return 0;
}

//
