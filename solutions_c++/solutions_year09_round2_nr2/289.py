#include <stdio.h>
#include <string.h>

char num[30];

int main()
{
	int T;
	char ctmp;
	char str[100];
	scanf("%d", &T);
	for (int iter = 1; iter <= T; iter++) {
		scanf("%s", str);
		int idx = strlen(str);
		int i;
		for (i = 0; i<idx; i++)
			num[i] = str[idx - i - 1];
		num[idx] = '0';

		for (i = 0; i<idx; i++)
			if (num[i] > num[i+1])
				break;
		int j = 0;
		while (num[j]<=num[i+1])
			j++;
		ctmp = num[j];
		num[j] = num[i+1];
		num[i+1] = ctmp;
		for (int k = 0; k<=i/2; k++) {
			ctmp = num[k];
			num[k] = num[i-k];
			num[i-k] = ctmp;
		}
		if (num[idx] == '0')	idx --;
		printf("Case #%d: ", iter);
		for (; idx >=0; idx--)
			printf("%c", num[idx]);
		printf("\n");
	}
	return 0;
}
