#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int n;
int nt;

// 123 -- 1
// 132 -- 1 + 2 = 3
// 213 -- 1 + 2 = 3
// 231 -- 1 + x
// 312 -- 1 + x
// 321 -- 1 + 2 = 3
//
// 6 * x = 1 + 3 + 3 + (1 + x) + (1 + x) + 3
// 4 * x = 12
// x = 3


// 1234 -- 1
// 1243 -- 3
// 1324 -- 3
// 1342 -- 4
// 1423 -- 4
// 1432 -- 3
// 2134 -- 3
// 2143 -- 1 + x
// 2314 -- 4
// 2341 -- 1 + x
// 2413 -- 1 + x
// 2431 -- 4
// 3124 -- 4
// 3142 -- 1 + x
// 3214 -- 3
// 3241 -- 4
// 3412 -- 1 + x
// 3421 -- 1 + x
// 4123 -- 1 + x
// 4132 -- 4
// 4213 -- 4
// 4231 -- 3
// 4312 -- 1 + x
// 4321 -- 1 + x
//
// 24 * x = 60 + 9 * x
// 15 * x = 60
// x = 4

//
// ... x = n?!

int main()
{
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{	
		printf("Case #%d: ", tt);
		
		scanf("%d", &n);
		int cnt = 0;
		for(int i = 1; i <= n; i++)
		{
			int x;
			scanf("%d", &x);
			if (x != i) cnt++;
		}
				
		printf("%.10lf\n", (double)cnt);
	}
	
	return 0;
}
