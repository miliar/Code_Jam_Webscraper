#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b)
{
	if (b == 0)  return a;
	return gcd(b, a % b);
}

bool work()
{
	long long N;
	int pd, pg;
	cin >> N >> pd >> pg;
	int v = gcd(pd, 100);
	int ed = pd / v;
	int D = 100 / v;
	if (D > N)  return false;
	if (pd < 100 && pg == 100)  return false;
	if (pd > 0 && pg == 0)    return false;
	return true;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		printf("Case #%d: ", k);
		if (work())  printf("Possible\n");
		else printf("Broken\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}