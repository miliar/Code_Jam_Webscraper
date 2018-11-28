#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int nt, n;

char s[200];

int pos[100];

bool sq()
{
	__int64 x = 0;
	for(int i = 0; i < n; i++) x = x * 2 + s[i] - '0';
	
	__int64 L = 0, R = 1 << 30;
	while(R - L > 1)
	{
		__int64 mid = (L + R) / 2;
		if (mid * mid <= x) L = mid; else R = mid;
	}
	
	//printf("x = %I64d, L = %I64d\n", x, L);
	
	return L * L == x;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d: ", tt);
		
		scanf("%s", s);
		
		n = strlen(s);
		int cnt = 0;
		for(int i = 0; i < n; i++) if (s[i] == '?') pos[cnt++] = i;
		
		int all = (1 << cnt) - 1;
		for(int i = 0; i <= all; i++)
		{
			int t = i;
			for(int j = 0; j < cnt; j++) { s[pos[j]] = '0' + (t & 1); t /= 2;}
			if (sq()) break;
		}
		puts(s);
	}
	return 0;
}