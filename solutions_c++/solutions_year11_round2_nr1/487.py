// MS Visual C++ 2008
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

char s[100][101];

int w[100], l[100];
long double owp[100], oowp[100];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tk = 1; tk <= T; tk++) {
		int n; 
		cin >> n;
		for (int i = 0; i < n; i++)	scanf("%s", &s[i][0]);
		for (int i = 0; i < n; i++) {
			w[i] = l[i] = 0;
			for (int j = 0; j < n; j++) 
				if (s[i][j] == '1') w[i]++;
				else if (s[i][j] == '0') l[i]++;
		}
		for (int i = 0; i < n; i++) {
			owp[i] = 0;
			for (int j = 0; j < n; j++)
				if (s[i][j] == '1') owp[i] += ((long double) w[j]) / (w[j] + l[j] - 1);
				else if (s[i][j] == '0') owp[i] += ((long double) (w[j] - 1)) / (w[j] + l[j] - 1);
			owp[i] /= (l[i] + w[i]);
		}
		for (int i = 0; i < n; i++) {
			oowp[i] = 0;
			for (int j = 0; j < n; j++) 
				if (s[i][j] != '.') oowp[i] += owp[j];
			oowp[i] /= (w[i] + l[i]);
		}
		printf("Case #%d:\n", tk);
		for (int i = 0; i < n; i++) 
			printf("%.7lf\n", 0.25 * (long double) w[i] / (w[i] + l[i]) + 0.50 * owp[i] + 0.25 * oowp[i]);
	}

	return 0;
}