#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int nt;

int n;

char s[100][101];

bool dontcount[100];

double WP(int k)
{
	int sum = 0, win = 0;
	for(int i = 0; i < n; i++)
	if (!dontcount[i])
	{
		sum += (s[k][i] != '.');
		win += (s[k][i] == '1');
	}
	return (double) win / sum;
}

double OWP(int k)
{
	dontcount[k] = true;
	double sum = 0.0;
	int cnt = 0;
	for(int i = 0; i < n; i++)
	if (s[k][i] != '.') 
	{
		sum += WP(i);
		cnt++;
	}
	dontcount[k] = false;
	return sum / cnt;
}

double OOWP(int k)
{
	double sum = 0.0;
	int cnt = 0;
	for(int i = 0; i < n; i++)
	if (s[k][i] != '.') 
	{
		sum += OWP(i);
		cnt++;
	}
	return sum / cnt;
}


double RPI(int k)
{
	return 0.25 * WP(k) + 0.50 * OWP(k) + 0.25 * OOWP(k);
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d:\n", tt);
		
		scanf("%d", &n);
		for(int i = 0; i < n; i++) scanf("%s", s[i]);

		for(int i = 0; i < n; i++) dontcount[i] = false;
		
		for(int i = 0; i < n; i++) printf("%.12lf\n", RPI(i));
	}
	
	return 0;
}