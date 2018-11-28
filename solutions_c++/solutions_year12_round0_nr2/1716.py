#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int onto[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int T, cases = 1;
char str[101];

int main()
{
 	freopen("B-large.in", "r", stdin);
 	freopen("out.txt", "w", stdout);
//	freopen("in.txt", "r", stdin);

	int n, s, p;
	int sco[101];

	scanf("%d", &T);
	while(cases <= T){
		scanf("%d%d%d", &n, &s, &p);
		for(int i=0; i<n; i++)
			scanf("%d", &sco[i]);

		int maxsco = 3 * p - 2;
		int minsco = max(p * 3 - 4, p);

		sort(sco, sco + n);

		int ans = 0;
		for(int i=n-1; i>=0; i--){
			if(sco[i] < minsco)
				break;

			if(sco[i] >= maxsco)
				ans ++;
			else if(s>=1){
				-- s;
				ans ++;
			}
		}

		printf("Case #%d: %d\n", cases, ans);
		cases ++;
	}
}