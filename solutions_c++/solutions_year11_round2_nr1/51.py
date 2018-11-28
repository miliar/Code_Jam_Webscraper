#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<utility>
#include<sstream>
#include<vector>
#include<string>
#include<set>
#include<map>

using namespace std;

char s[105][105];
int n;
double WP[105], OWP[105], OOWP[105];
int cnt[105];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int ntest;
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++)
	{
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			scanf("%s", &s[i]);

		for(int i=0; i<n; i++)
		{
			cnt[i] = 0;
			for(int j=0; j<n; j++)
				if(s[i][j] != '.') cnt[i]++;
		}
		
		for(int i=0; i<n; i++)
		{
			int win = 0;
			for(int j=0; j<n; j++)
				if(s[i][j] == '1') win++;
			WP[i] = win * 1.0 / cnt[i];
		}
		
		for(int i=0; i<n; i++)
		{
			double total = 0;
			for(int j=0; j<n; j++)
				if(s[i][j] != '.') 
				{
					total += (WP[j] * cnt[j] - (s[j][i] == '1' ? 1 : 0)) / (cnt[j] - 1);
				}
			OWP[i] = total * 1.0 / cnt[i];
		}

		for(int i=0; i<n; i++)
		{
			double total = 0;
			for(int j=0; j<n; j++)
				if(s[i][j] != '.') total += OWP[j];
			OOWP[i] = total * 1.0 / cnt[i];
		}

		printf("Case #%d:\n", test);
		for(int i=0; i<n; i++)
			printf("%.10lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}

	return 0;
}
