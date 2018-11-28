#include <cstdio>
using namespace std;
#include <vector>

void doit(int tnumber) {
	int n, k;
	scanf("%d%d", &n, &k);
	bool good = true;
	for (int i = 0; i < n; ++i) {
		if (k % 2 == 0)
			good = false;
		k /= 2;
	}
	printf("Case #%d: ", tnumber);
	if (good)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		doit(i + 1);
	fclose(stdin);
	fclose(stdout);
	return 0;
}
