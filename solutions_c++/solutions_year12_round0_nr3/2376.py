#include <stdio.h>
#include <set>

using namespace std;

int powers[10];

int getw(int a)
{
	for (int i = 0; i < 10; i++)
		if (a < powers[i])
			return i;
	return -1;
}

int rotate(int a, int w)
{
	int last = a % 10;
	a /= 10;
	a += powers[w - 1] * last;
	return a;
}

int solve()
{
	int A = 0, B = 0, W = 0, R = 0;
	scanf("%d %d", &A, &B);
	W = getw(A);
	
	for (int C = A; C < B; C++) {
		int D = C;
		set<int> s;
		for (int i = 0; i < W; i++) {
			D = rotate(D, W);
			if (getw(D) == W && D > C && D <= B && s.find(D) == s.end()) {
				R++;
				s.insert(D);
			}
		}
	}
	return R;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	int a = 1;
	for (int i = 0; i < 10; i++) {
		powers[i] = a;
		a *= 10;
	}
	
	for (int i = 0; i < T; i++)
		printf("Case #%d: %d\n", i + 1, solve());
}