#include <stdio.h>
#include <algorithm>

#define SIZE 1000

using namespace std;

int T, t;
__int64 A, B, P;

int prost[SIZE];
int p[SIZE];
int num;
int a[SIZE];
int len;
int dad[SIZE];
int i, j;
int used[SIZE];

bool find(int x, int y, bool unite)
{
  int i, j;
  i = x; while (dad[i] > 0) i = dad[i];
  j = y; while (dad[j] > 0) j = dad[j];
  if (unite && (i != j)) dad[j] = i;
  return (i != j);
}

int maxFactor(int a, int b)
{
	int i;
	int p = 1;
	for (i = 0; i < num; i++)
		if (a % prost[i] == 0 && b % prost[i] == 0)
			if (prost[i] > p) p = prost[i];

	return p;
}

int main() {

  for (i = 0; i < SIZE; i++) p[i] = 1;

  num = 0;
  i = 2;
  while (1) {
    while (p[i] == 0) {
      i++;
      if (i == SIZE) break;
    }
    if (i == SIZE) break;

    prost[num] = i;
    num++;

    j = i + i;
    while (j < SIZE) {
      p[j] = 0;
      j += i;
    }

    i++;
  }
  

	FILE *in = fopen("B-small.in", "rt");
	FILE *out = fopen("B-small.out", "wt");

	//FILE *in = fopen("B-large.in", "rt");
	//FILE *out = fopen("B-large.out", "wt");

	fscanf(in, "%d", &T);

	for (t = 1; t <= T; t++) {

		fscanf(in, "%I64d %I64d %I64d", &A, &B, &P);

		for (i = A; i <= B; i++) a[i-A + 1] = i;
		len = B - A + 1;

		for (i = 0; i <= len; i++) dad[i] = 0;

		for (i = 1; i <= len; i++) {
			for (j = i + 1; j <= len; j++) {
				if (maxFactor(a[i], a[j]) >= P)
					//dad[j] = dad[i];
					find(i, j, true);
			}
		}
	
		for (i = 1; i <= len; i++)
			used[i] = 0;
		
		__int64 cnt = 0;
		for (i = 1; i <= len; i++) {
			if (dad[i] == 0) cnt++;
		}
		
		fprintf(out, "Case #%d: %d\n", t, cnt);
	}

	fclose(in);
	fclose(out);

	return 0;
}