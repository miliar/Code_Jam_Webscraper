#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>

using namespace std;

#define see(x) cout<<#x<<" "<<(x)<<endl
#define sp system("pause")

int n;
int a[1100];

int main(int argc, char *argv[])
{
	freopen("C-large.in", "r", stdin);
	freopen("C.txt", "w", stdout);
	int T, t, i;
	bool res;
	scanf("%d", &T);
	for(t = 1; t <= T; ++t)
	{
		scanf("%d", &n);
		int temp = 0, sum = 0, mv = 1000001;
		for(i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
			temp ^= a[i];
			sum += a[i];
			mv = min(mv, a[i]);
		}
		if(temp != 0)
		{
			printf("Case #%d: NO\n", t);
		}
		else
		{
			printf("Case #%d: %d\n", t, sum - mv);
		} 		
	}
	return 0;
}
