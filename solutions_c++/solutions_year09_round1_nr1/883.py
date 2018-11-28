#include <iostream>
using namespace std;

bool hash[10][100000];
bool flag[100000];


int  fun(int x, int b) 
{
	int sum = 0, i, tmp;
	char str[10000];
	itoa(x, str, b);
	for (i = 0; str[i]; i++) {
		tmp = str[i] - '0';
		sum +=tmp * tmp;
	}
	return sum;
}

void fun2()
{
	int tmp, i, j;
	memset(hash, false, sizeof(hash));
	for (i = 2; i <= 10; i++) {
		for (j = 2; j <= 100000; j++) {
			memset(flag, true , sizeof(flag));
			tmp = fun(j, i);
			while (true) {
				if (flag[tmp]) {
					flag[tmp] = false;
					if (tmp == 1) {
						hash[i][j] = true;
						//printf("%d %d      ", i, j);
						break;
					} else {
						tmp = fun(tmp, i);
					}
				} else {
					break;
				}
			}
		}
	}
}

int main()
{
	fun2();
	char tmp;
	int num[20];
	int j, k, c, i, t;
	freopen("c:\A-small-attempt1.in", "r", stdin);
	freopen("c:\A-small-attempt1.out", "w", stdout);
	scanf("%d", &t);
	c = 0;
	while (t--) {
		c++;
		i = 1;
		while (i) {
			scanf("%d%c", &num[i], &tmp);
			if (tmp == '\n') break;
			i++;
		}
		for (j = 2; ;j++) {
			for (k = 1; k <= i; k++) {
				if(!hash[num[k]][j]) {
					goto END;
				}
			}
			printf("Case #%d: %d\n", c, j);
			break;
END:;
		}
	}

}