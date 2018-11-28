#include <cstdio>

using namespace std;

int n, s, p, t[105], cases;

void process(int tc)
{
	scanf("%d %d %d", &n, &s, &p);

	for (int i = 0; i < n; i++) {
		scanf("%d", &t[i]);
	}

	int ans = 0;
	
	for (int i = 0; i < n; i++) {
		if (t[i] % 3 == 0) {
			if (t[i] == 0) {
				if (p == 0) {
					ans++;
				}
			}
			else if (t[i] == 30) {
				ans++;
			}
			else if (t[i]/3 < p && (t[i] + 3)/3 >= p && s) {
				ans++;
				s--;
			}
			else if (t[i]/3 >= p) {
				ans++;
			}
		}
		else if (t[i] % 3 == 1) {
			if (t[i] == 1) {
				if (p <= 1) {
					ans++;
				}
			}
			else if (t[i] == 28) {
				ans++;
			}
			else if ((t[i] + 2)/3 >= p) {
				ans++;
			}
		}
		else if (t[i] % 3 == 2) {
			if (t[i] == 29) {
				ans++;
			}
			else if ((t[i] + 1)/3 < p && (t[i] + 4)/3 >= p && s) {
				ans++;
				s--;
			}
			else if ((t[i] + 1)/3 >= p) {
				ans++;
			}
		}
	}

	printf("Case #%d: %d\n", tc, ans);
}

int main()
{
	scanf("%d", &cases);
	
	for (int i = 0; i < cases; i++)
		process(i + 1);		
		
	return 0;
}
