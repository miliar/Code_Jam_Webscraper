#if 1
#include <iostream>
#include <stdio.h>
double WP[100];
double OWP[100];
double OOWP[100];
char map[100][101];
int N;
using namespace std;
int gcd(int a, int b) { return (b == 0) ? a : gcd(b, a % b); }
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> N;
		for (int i = 0; i < N; i++) scanf("%s", map[i]);
		for (int i = 0; i < N; i++) 
		{
			int total = 0, win = 0;
			for (int j = 0; j < N; j++) 
			{
				if (map[i][j] == '.') continue;
				total++;
				if (map[i][j] == '1') win++;
			}
			WP[i] = (double)win / total;
		}
		for (int i = 0; i < N; i++) 
		{
			double temp = 0;
			int s = 0;
			for (int j = 0; j < N; j++) 
			{
				if (map[i][j] == '.') continue;
				s++;
				int total = 0, win = 0;
				for (int k = 0; k < N; k++) {
					if (map[j][k] == '.' || k == i) continue;
					total++;
					if (map[j][k] == '1') win++;
				}
				temp += (double)win / total;
			}
			OWP[i] = temp / s;
		}
		for (int i = 0; i < N; i++)
		{
			double temp = 0;
			int s = 0;
			for (int j = 0; j < N; j++)
			{
				if (map[i][j] == '.') continue;
				temp += OWP[j];
				s++;
			}
			OOWP[i] = temp / s;
		}
		printf("Case #%d:\n", cases);
		for (int i = 0; i < N; i++)
			printf("%.12lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
#endif