#include <stdio.h>
#include <algorithm>

using namespace std;


int main()
{
	int T, Case, n, s, p;
	int dat[101], i, ans;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for(Case = 1; Case <= T; Case++)
	{
		ans = 0;
		scanf("%d %d %d", &n, &s, &p);
		for(i=0;i<n;i++) scanf("%d",&dat[i]);

		sort(dat, dat+n);	

		for(i=n-1;i>=0;i--)
		{
			// 나머지가 0
			if(dat[i] % 3 == 0)
			{
				if(dat[i] / 3 >= p) ans++;
				else if(dat[i] / 3 + 1 >= p && s>0 && dat[i] / 3 -1 >= 0) {ans++; s--;}
			} else if(dat[i] % 3 == 1)
			{
				if(dat[i] / 3 + 1 >= p) ans++;
			} else if(dat[i] % 3 == 2)
			{
				if(dat[i] / 3 + 1 >= p) ans++;
				else if(dat[i] / 3 + 2 >= p && s>0) {ans++; s--;}
			}
		}
		printf("Case #%d: %d\n", Case, ans);
	}
}