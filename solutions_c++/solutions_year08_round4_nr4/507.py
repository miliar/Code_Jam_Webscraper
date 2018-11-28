#include <stdio.h>
#include <string.h>

#define MAX 102400
#define MAXK 32

int k, len, min;
int tmp[MAXK], use[MAXK];
char str[MAX], newstr[MAX];

void permu(int index) {
	int i, count;
	char last;

	if(index == k) {
		count = 1;
		for(i = 0; i < len; i++)
			newstr[i] = str[i / k * k + tmp[i % k]];
		last = newstr[0];
		for(i = 1; i < len; i++)
			if(last != newstr[i]) {
				count++;
				last = newstr[i];
			}
		if(min > count)
			min = count;
		return;
	}

	for(i = 0; i < k; i++)
		if(use[i] == 0) {
			use[i] = 1;
			tmp[index] = i;
			permu(index + 1);
			use[i] = 0;
		}
}

void find_ans() {
	int i;

	scanf("%d", &k);
	scanf("%s", str);

	min = MAX;
	len = strlen(str);
	permu(0);
	printf(" %d", min);
}

int main(int argc, char *argv[])
{
	int i, n;

	scanf("%d", &n);
	for(i = 1; i <= n; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
