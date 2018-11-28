#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <utility>
#include <iostream>
using namespace std;

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()

#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define wipen(a) memset((a), -1, sizeof(a))
#define wipez(a) memset((a), 0, sizeof(a))

#define pb push_back
#define sz(c) int((c).size())

const int INF = 0x3F3F3F3F, NEGINF = 0xC0C0C0C0;

int main()
{
	int T, nt;
	scanf("%d", &nt);
	for(T = 0; T < nt; T++)
	{
		int n, sol = 0;
		int row[64], num[64];
		scanf("%d", &n);
		wipez(num);
		for(int i = 0; i < n; i++)
		{
			row[i] = 0;
			for(int j = 0; j < n; j++)
			{
				char c[2];
				scanf("%1s", c);
				if(c[0] == '1') row[i] = j+1;
			}
			num[row[i]]++;
		}
		for(int i = 1; i <= n; i++)
		{
			for(int j = i-1; j < n; j++)
			{
				if(row[j] <= i)
				{
					for(int k = j; k > i-1; k--)
					{
						int temp = row[k-1];
						row[k-1] = row[k];
						row[k] = temp;
						sol++;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", T+1, sol);
	}
	return 0;
}
