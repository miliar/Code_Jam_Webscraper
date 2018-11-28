#include <iostream>
using namespace std;

const int size = 50000;
char str[size];
//char str[] = "aabcaaaa";
int perm[16];

int getLen() {
	int count = 1;
	int len = strlen(str);
	int index = 0;
	char pre = str[0];
	while (index < len) {
		if (str[index] != pre) {
			count++;
			pre = str[index];
		}
		index++;
	}
	return count;
}

int main() {
		freopen("D-small-attempt1.in", "r", stdin);
		freopen("D-small1.out", "w", stdout);
	int l, t;
	scanf("%d", &t);
	for (l = 0; l < t; l++) {
		memset(str, 0, sizeof(str));
		memset(perm, 0, sizeof(perm));
		int perm_num = 0;
		scanf("%d", &perm_num);
		scanf("%s", str);
		//		printf("%s\n", str);
		for (int i = 0; i < perm_num; i++)
			perm[i] = i;
		char orign[size];
		memset(orign, 0, sizeof(orign));
		memcpy(orign, str, sizeof(str));
		int len = size;
		do {
			for (int i = 0; i < strlen(str) / perm_num; i++) {
				for (int j = 0; j < perm_num; j++) {
					str[i * perm_num + j] = orign[i * perm_num + perm[j]];
				}
			}
			int temp = getLen();
			if (temp < len)
				len = temp;
			//			printf("%s\n", str);
		} while (next_permutation(perm, perm + perm_num));
		printf("Case #%d: %d\n", l + 1, len);
	}
	return 0;
}
