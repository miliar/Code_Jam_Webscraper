#include <iostream>
#include <algorithm>

using namespace std;

int a1, a2, b1, b2;

bool sear(int a, int b)
{
	if (a < b) swap(a, b);
	if (a == b) return 0;
	if (a > b && a % b == 0) return 1;
	if (a < b + b) return 1 - sear(b, a - b);
	if (a > b + b) return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		int i, j;
		int num = 0;
		for (i = a1; i <= a2; i++)
			for (j = b1; j <= b2; j++)
				if (sear(i, j)) num++;
		printf("%d\n", num);
	}
	return 0;
}