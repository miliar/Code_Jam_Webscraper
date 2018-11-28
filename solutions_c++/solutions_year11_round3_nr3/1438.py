#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int t, n;
long long l, h, arr[10000], res;

int main()
{
	int i, j;

	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d %lld %lld", &n, &l, &h);
		for (j = 0; j < n; j++)
			scanf("%lld", arr + j);
		for (res = l; res <= h; res++) {
			for (j = 0; j < n; j++)
				if ((res > arr[j] && res % arr[j] != 0) ||
					(res < arr[j] && arr[j] % res != 0))
					goto error;
			goto end;
error:
			;
		}
end:
		printf("Case #%d: ", i + 1);
		if (res > h)
			printf("NO\n");
		else
			printf("%lld\n", res);
	}

	return (0);
}


