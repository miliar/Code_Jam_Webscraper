#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "gcj";

int N,n,cnt,cnt1;
char s[100];
int a[100];
int pos[100];
int t[100];

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &N);
	for (int I=1; I<=N; ++I)
	{
		scanf("%d\n", &n);
		for (int i=0; i<n; ++i)
		{
			a[i] = 0;
			gets(s);
			for (int j=0; j<n; ++j)
				if (s[j] == '1')
					a[i] = j;
		}

		for (int i=0; i<n; ++i)
			pos[i] = i;
		cnt = 10000000;

		//do
		//{
		//	bool f = true;
		//	for (int i=0; i<n; ++i)
		//		f = f && (a[pos[i]] <= i);

		//	if (f)
		//	{
		//		for (int i=0; i<n; ++i)
		//			t[pos[i]] = i;
		//		int c = 0;
		//		for (int i=0; i<n; ++i)
		//			for (int j=1; j<n; ++j)
		//				if (t[j-1] > t[j])
		//				{
		//					swap(t[j-1], t[j]);
		//					++c;
		//				}
		//		cnt = min(cnt, c);
		//	}
		//} while (next_permutation(&pos[0], &pos[n]));

		cnt1 = cnt;
		cnt = 0;
		for (int i=0; i<n; ++i)
		{
			int j = i;
			for (; j<n && a[j] > i; ++j)
				;
			for (int t=j-1; t>=i; --t)
			{
				swap(a[t], a[t+1]);
				++cnt;
			}

		}

		//if (cnt != cnt1)
		//	printf("");
		
		printf("Case #%d: %d\n", I, cnt);
	}

	return 0;
} 