#include <iostream>

using namespace std;

int n, k;
int num[40];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	num[1] = 1;
	int i;
	for (i = 2; i <= 30; i++)
		num[i] = num[i - 1] + num[i - 1] + 1;
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d %d", &n, &k);
		k %= num[n] + 1;
		if (k == num[n]) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}