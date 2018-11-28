#include <cstdio>
#include <cmath>
#include <ctime>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;


const int MAXN = 10007;
const double EPS = 1e-9;

double f[MAXN], d[MAXN], l[MAXN];
bool flag[MAXN];

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }

int main()
{
    freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
    	printf("Case #%d: ", t);
    	int n;
    	scanf("%d", &n);
    	int last = 0;
    	for (int i = 0; i < n; i++)
    		cin >> d[i] >> l[i];

    	double D;
    	cin >> D;

    	for (int i = 0; i < n; i++)
    	{
    		f[i] = 0;
    		flag[i] = false;
    	}
    	f[0] = d[0];

    	for (int i = 0; i < n; i++)
    	{
    		int x = -1;
    		for (int j = 0; j < n; j++)
    			if (!flag[j] && (x == -1 || f[x] < f[j]))
    				x = j;
    		flag[x] = true;
    		for (int j = 0; j < n; j++)
    			if (abs(d[j] - d[x]) < f[x] + EPS)
	    			f[j] = max(f[j], min(l[j], abs(d[j] - d[x])));
    	}

    	bool ans = false;
    	for (int i = 0; i < n; i++)
    		ans |= d[i] + f[i] + EPS > D;

    	puts(ans? "YES" : "NO");
    }

    fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
