#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
int k;
char str[50005];
char target[50005];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j;
	int a[16];
	int r, cs = 0;
	scanf("%d", &r);
	while(r--)
	{
        scanf("%d", &k);
		scanf("%s", str);
		n = strlen(str);
        for(i = 0; i < k; ++i) a[i] = i;
		int minv = 0x7fffffff;
		do
		{
            for(i = 0; i < n / k; ++i)
			{
				int offset = i * k;
                for(j = 0; j < k; ++j)
				{
					target[offset + j] = str[offset + a[j]];
				}
			}
			int c = 1;
			for(i = 1; i < n; ++i)
			{
                if(target[i] != target[i - 1]) c++;
			}
			if(c < minv) minv = c;
		} while(next_permutation(a, a + k));
		printf("Case #%d: %d\n", ++cs, minv);
	}
	return 0;
}