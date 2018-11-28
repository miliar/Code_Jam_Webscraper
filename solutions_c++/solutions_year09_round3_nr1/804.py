#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <list>
#include <map>
#include <vector>

char buffer[62];
unsigned long long number[62];
int n;

void readdata()
{
	scanf("%s\n", buffer);
	n = strlen(buffer);
	if (buffer[n - 1] == '\n' || buffer[n - 1] == '\r') {
		buffer[n - 1] = 0;
		n--;
	}
}

void solve()
{
	int let[27] = {0};
	int cf[10] = {0};
	int i;
	int min = 0;
	for (i = 0; i < n; i++) {
		if (isalpha(buffer[i]) && let[buffer[i] - 'a'] == 0) {
			min++;
			let[buffer[i] - 'a'] = 1;
		}
		else if (isdigit(buffer[i]) && cf[buffer[i] - '0'] == 0) {
			min++;
			cf[buffer[i] - '0'] = 1;
		}
	}

	unsigned long long sol = 0;
	int base = min;
	if (base == 1)
		base = 2;

	int l[27] = {0};
	int c[10] = {0};

	for (i = 0; i < 27; i++)
		l[i] = -1;
	for (i = 0; i < 10; i++)
		c[i] = -1;

	if (isalpha(buffer[0]))
		l[buffer[0] - 'a'] = 1;
	else
		c[buffer[0] - '0'] = 1;

	number[0] = 1;

	sol = 1;

	i = 1;

	while (i < n) {
		if (isalpha(buffer[i]))
			if (l[buffer[i] - 'a'] != -1) {
				
				sol = sol * base + 1;
				number[i] = 1;
				i++;
				continue;
			}
			else
				l[buffer[i] - 'a'] = 0;
		else
			if (c[buffer[i] - '0'] != - 1) {
				
				sol = sol * base + 1;
				number[i] = 1;
				i++;
				continue;
			}
			else
				c[buffer[i] - '0'] = 0;
		sol = sol * base + 0;
		number[i] = 0;
		i++;
		break;
	}

	min = 2;

	int crt;

	for (; i < n; i++) {
		if (isalpha(buffer[i]))
			if (l[buffer[i] - 'a'] != -1)
				crt = l[buffer[i] - 'a'];
			else {
				l[buffer[i] - 'a'] = min;
				crt = min;
				min++;
			}
		else 
			if (c[buffer[i] - '0'] != -1)
				crt = c[buffer[i] - '0'];
			else {
				c[buffer[i] - '0'] = min;
				crt = min;
				min++;
			}
		number[i] = crt;
		sol = sol * base + crt;
	}

	sol = 0;
	for (i = 0; i < n; i++)
		sol = sol * base + number[i];
	printf("%llu\n", sol);
}

int main()
{
	freopen("in5.in", "rt", stdin);
	freopen("out5.out", "wt", stdout);
	
	int it, t;
	scanf("%d\n", &t);
	for (it = 1; it <= t; it++) {
		printf("Case #%d: ", it);
		readdata();
		solve();
	}

	return 0;
}