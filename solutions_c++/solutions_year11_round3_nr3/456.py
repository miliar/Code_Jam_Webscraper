#include <cstdio>
#include <cstring>

int T, N, L, H;
int note[1000010];

int gcd(int a, int b)
{
	if(b > a) return gcd(b, a);
	if(b == 0) return a;
	return gcd(b, a%b);
}

int lcm(int a, int b)
{
	return (a*b)/(gcd(a,b));
}

int main()
{
	scanf("%d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		scanf("%d %d %d ", &N, &L, &H);

		for(int i = 0; i < N; ++i) {
			scanf("%d ", &note[i]);
		}

/*		int lcmorio = note[0];
		for(int i = 1; i < N; ++i) {
			lcmorio = lcm(lcmorio, note[i]);
		}*/

		int found = 0;
		for(int i = L; i <= H; ++i) {
			int ok = 1;
			for(int j = 0; j < N; ++j) {
				if(!(note[j]%i == 0 || i%note[j] == 0)) ok = 0;
			}
			if(ok) {
				found = i;
				break;
			}
		}

		printf("Case #%d: ", _42);
		if(found) {
			printf("%d\n", found);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
