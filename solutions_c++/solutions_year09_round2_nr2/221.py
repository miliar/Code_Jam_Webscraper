#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
char a[100], b[100], c[100];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int r, cs = 0;
	scanf("%d", &r);
	gets(a);
	while(r--)
	{
        gets(a);
		strcpy(b, a);
		strcpy(c, a);
        n = strlen(a);

		sort(c, c + n);
		for(int i = 0; i < n / 2; ++i)
			swap(c[i], c[ n - i - 1]);

		int flag = (strcmp(a, c) == 0);
		next_permutation(a, a + n);

		if( strcmp(a, b) == 0 || flag )
		{
            n++;
			a[n - 1] = '0';
			a[n] = 0;

			sort(a, a + n);
			if(a[0] == '0')
			{
				for(int i = 1; i < n; ++i)
					if(a[i] != '0')
					{
						swap(a[0], a[i]);
						break;
					}
			}
		}
		printf("Case #%d: %s\n", ++cs, a);
	}
	return 0;
}