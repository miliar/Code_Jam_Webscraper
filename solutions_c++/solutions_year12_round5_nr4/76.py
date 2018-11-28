#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;


const int MAXL = 1024;
const int INF = (int)1e+9;

int a[36][36];
int f[36], g[36];
char m[256];
char s[MAXL];
int n, k;

int main()
{
    freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);

    int test;
    m['o'] = '0';
    m['i'] = '1';
    m['e'] = '3';
    m['a'] = '4';
    m['s'] = '5';
    m['t'] = '7';
    m['b'] = '8';
    m['g'] = '9';
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
    	printf("Case #%d: ", t);
    	memset(a, 0, sizeof(a));
    	memset(f, 0, sizeof(f));
    	memset(g, 0, sizeof(g));

    	scanf("%d\n", &k);
    	gets(s);
    	n = strlen(s);
    	for (int i = 1; i < n; i++)
    	{
    		a[s[i - 1] - 'a'][s[i] - 'a']++;

    		if (m[s[i - 1]])
	    		a[m[s[i - 1]] - '0' + 26][s[i] - 'a']++;

    		if (m[s[i]])
	    		a[s[i - 1] - 'a'][m[s[i]] - '0' + 26]++;

	    	if (m[s[i - 1]] && m[s[i]])
	    		a[m[s[i - 1]] - '0' + 26][m[s[i]] - '0' + 26]++;
    	}

    	for (int i = 0; i < 36; i++)
    		for (int j = 0; j < 36; j++)
    		{
    			if (a[i][j])
    			{
//    				printf("%d %d %d\n", i, j, a[i][j]);
        			f[i]++;
        			g[j]++;
    			}
    		}

    	int ans = INF;
    	for (int i = 0; i < 36; i++)
    		for (int j = 0; j < 36; j++)
    		{
    			f[i]++;
    			g[j]++;
//*
    			int res = 0;
		    	for (int i = 0; i < 36; i++)
		    		res += max(f[i], g[i]);
		    	ans = min(ans, res);

		    	f[i]--;
		    	g[j]--;
//*/
    		}
    	printf("%d\n", ans);
    }

    fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
