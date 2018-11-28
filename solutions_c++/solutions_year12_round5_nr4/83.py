#include <algorithm>
#include <memory.h>
#include <stdio.h>
using namespace std;

int k;
char data[1010];

bool edge[60][60];

// "o" to "0", "i" to "1", "e" to "3", "a" to "4", "s" to "5", "t" to "7", "b" to "8" and/or "g" to "9".
void make_edge(char x, char y)
{
	edge[x-'a'][y-'a'] = true;

	char a=0, b=0;
	if (x=='o') a='0';
	else if (x=='i') a='1';
	else if (x=='e') a='3';
	else if (x=='a') a='4';
	else if (x=='s') a='5';
	else if (x=='t') a='7';
	else if (x=='b') a='8';
	else if (x=='g') a='9';
	if (y=='o') b='0';
	else if (y=='i') b='1';
	else if (y=='e') b='3';
	else if (y=='a') b='4';
	else if (y=='s') b='5';
	else if (y=='t') b='7';
	else if (y=='b') b='8';
	else if (y=='g') b='9';

	if (a) edge[a-'0'+26][y-'a'] = true;
	if (b) edge[x-'a'][b-'0'+26] = true;
	if (a&&b) edge[a-'0'+26][b-'0'+26] = true;
}

bool check[40];

	const int n = 36;

	int answer;

	bool used;

int main()
{
	int i, j;

	int t, tt=0;

	scanf("%d", &t);
	while (t--) {
		scanf("%d", &k);
		scanf("%s", data);

		memset(edge, 0, sizeof(edge));
		for (i=0; data[i+1]; i++) {
			make_edge(data[i], data[i+1]);
		}

		answer = 0;

		int m=0;

		for (i=0; i<n; i++) {
			if (edge[i][i]) {
				edge[i][i] = false;
				m++;
			}
		}
		for (i=0; i<n; i++) for (j=0; j<n; j++) m += edge[i][j];

		for (i=0; i<n; i++) {
			int in=0, out=0;
			for (j=0; j<n; j++) if (edge[i][j]) out++;
			for (j=0; j<n; j++) if (edge[j][i]) in++;

			answer += abs(in-out);
		}

		printf("Case #%d: %d\n", ++tt, answer ? answer/2 + m : answer/2 + m + 1);
	}

	return 0;
}
