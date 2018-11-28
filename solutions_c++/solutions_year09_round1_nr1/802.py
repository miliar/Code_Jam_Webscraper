// problem a

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bases[20], cnt;
int flag[100000];

char * res;

void Change(int data, int base, char * res, int &len)
{
	int i = 0, t;
	while (1) {
		t = data % base;
		res[i++] = t + '0';
		data /= base;
		if (data == 0) break;
	}
	len = i;
	return ;
}

int Calc(char * res, int len)
{
	int i, sum;
	for (sum=0, i=0; i<len; i++) sum += ((res[i]-'0')*(res[i]-'0'));
	return sum;
}

int main()
{
	int i, k, t, cas, num, mark, len;
	char ch;

	freopen("A-small.in", "r", stdin);
	freopen("res.out", "w", stdout);
	scanf("%d", &cas);

	for (t=1; t<=cas; t++) {
		cnt = 0;
	
		res = new char [1000];

		do {
			scanf("%d", &bases[cnt++]);
			ch = getchar();
		} while (ch != '\n');
		
		for (k=2; ; k++) {
			mark = 1;
			for (i=0; i<cnt; i++) {
				num = k;
				memset(flag, 0, sizeof(flag));
				flag[num] = 1;
				do {
					Change(num, bases[i], res, len);
					num = Calc(res, len);
					if (num == 1) break;
					if (flag[num]) { mark=0; break; }
					else flag[num] = 1;
				} while (1);
				if (mark == 0) break ;
			}
			if (mark == 1) break ;
		}

		printf("Case #%d: %d\n", t, k);

		delete res;
	}

	return 1;
}
