#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

#define MAXN 10000

struct range
{
	int len, last;
} s[MAXN];

int a[MAXN];
int n, k;


int main()
{
    int tc;
	//freopen("b2.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
		scanf("%i", &n);
		for(int i=0; i<n; ++i) scanf("%i", &a[i]);
		sort(&a[0], &a[n]);
		k = 0;
		for(int i=0; i<n; ++i)
		{	
			int p = -1;
			for(int j=0; j<k; ++j)
				if (s[j].last + 1 == a[i] && (p==-1 || s[j].len < s[p].len)) p = j;
			if (p == -1)
			{				
				s[k].last = a[i];
				s[k].len = 1;
				k++;
			}
			else
			{
				s[p].len++;
				s[p].last++;
			}
		}
		int ans = 10000;
		if (k==0) ans = 0;
		for(int i=0; i<k; ++i) if (s[i].len < ans) ans = s[i].len;
        printf("Case #%i: %i\n", tt, ans);
    }
}