#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 2005;

int n;
int p[MAX];
char str[MAX], temp[MAX];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	int Case = 1, T;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d", &n);
		scanf("%s", str);

		int i, j, k;
		for (i = 0; i < n; ++ i)
			p[i] = i;

		int len, cnt, ans = -1;
		len = strlen(str);
		do
		{
			cnt = 0;
			for(i = 0, k = 0; i < len; )
			{
				for(j = 0; j < n; ++ j)
					temp[i++] = str[p[j]+k];
				k += n ;
			}
			for(i = 0; i < len; )
			{
				j = i;
				while(j+1 < len && temp[j] == temp[j+1])
					j ++;
				i = ++j;
				cnt ++;
			}
			if(ans == -1 || cnt < ans)
				ans = cnt;
		}while (next_permutation(p, p+n));
		printf("Case #%d: %d\n", Case++, ans);
	}
	return 0;
}