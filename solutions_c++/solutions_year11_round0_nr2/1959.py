#include<cstdio>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a,b) ((a) < (b) ? (a) : (b))
#define _max(a,b) ((a) > (b) ? (a) : (b))
using namespace std;

string ans = "", s;
int n, T;
bool a[333][333];
char f[333][333];
int main(){
/*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		memset(f, '\0', sizeof(f));
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++)
		{
			cin>> s;
			f[(int) s[0]][(int) s[1]] = s[2];
			f[(int) s[1]][(int) s[0]] = s[2];
		}
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			cin>> s;
			a[(int) s[0]][(int) s[1]] = 1;
			a[(int) s[1]][(int) s[0]] = 1;
		}
		scanf("%d", &n);
		cin>> s;
		ans = "";
		for (int i = 0; i < n; i++)
		{
			int m = ans.size();
			if (m == 0) ans += s[i];else
			if (f[(int) s[i]][(int) ans[m - 1]] >= 'A') ans[m - 1] = f[(int) s[i]][(int) ans[m - 1]];else
			{
				for (int j = 0; j < m; j++) if (a[(int) s[i]][(int) ans[j]])
				{
					ans = "";
					break;
				}
				if (ans != "") ans += s[i];
			}
		}
		printf("Case #%d: [", t);
		int m = ans.size();
		for (int i = 0; i < m - 1; i++) cout<< ans[i]<< ", ";
		if (m) cout<< ans[m - 1];
		puts("]");
	}
	return 0;
}
