#include <cmath>
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAXN = 150;
int a[MAXN], b[MAXN];
int pa[MAXN], pb[MAXN];
int main()
{
	int t, n, pos,k;
	char ch;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for ( k = 1; k <= t; k++)
	{
		scanf("%d", &n);
		a[0] = b[0] = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> ch >> pos;
			if (ch == 'O')
				a[++a[0]] = pos, pa[a[0]] = j;;
			if (ch == 'B')
				b[++b[0]] = pos, pb[b[0]] = j;
		}
		int sa = 1, sb = 1, apos = 1, bpos = 1, count = 0;
		while (sa <= a[0] || sb <= b[0])
		{
			if (sa > a[0])
			{
				count += abs(b[sb] - bpos) + 1;
				bpos = b[sb];
				sb++;
				continue;
			}
			if (sb > b[0])
			{
				count += abs(a[sa] - apos) + 1;
				apos = a[sa];
				sa++;
				continue;
			}
			count++;
			if (bpos == b[sb])
			{
				if (pa[sa] > pb[sb])
				{
					sb++;
					if (apos != a[sa])
					{
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					}
				}else{
					if (apos != a[sa])
					{
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
					}else sa++;
				}
			}
			else
			{
				bpos = bpos < b[sb] ? (bpos + 1) : (bpos - 1);
				if (pa[sa] > pb[sb])
				{
					if (apos != a[sa])
						apos = apos < a[sa] ? (apos + 1) : (apos - 1);
				}else{
					if (apos == a[sa])
					{
						sa++;
					}else apos = apos < a[sa] ? (apos + 1) : (apos - 1);
				}
			}
		}
		printf("Case #%d: %d\n",k,count); 
	}
	return 0;
}
