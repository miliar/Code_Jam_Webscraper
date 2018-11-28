#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, t;
int k;
int st2[31];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	st2[0] = 1;
	for (int i = 1; i < 31; i++)
		st2[i] = st2[i - 1] * 2;
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d%d", &n, &k);
		bool on = true;
		for (int i = 0; i < n; i++)
			if ((k & (1 << i)) == 0)
				on = false;
		if (on)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
