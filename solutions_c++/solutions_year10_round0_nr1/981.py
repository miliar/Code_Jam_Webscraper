#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int main()
{
	int T, n, k, i;
	freopen("A.in", "r", stdin);
	//freopen("DownloadA-small.out", "w", stdout);
	freopen("A.out", "w", stdout);
	for(scanf("%d", &T), i = 1; i <= T; i++)
	{
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i);
		printf("%s\n", ((k + 1) % (1 << n)) ? "OFF" : "ON");
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
