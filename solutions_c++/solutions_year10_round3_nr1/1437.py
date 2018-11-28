#define _CRT_SECURE_NO_DEPRECAT

#include <stdio.h>
#include <memory.h>
#include <algorithm>

#define fi(a,b) for(int i = a; i<=b; i++)
#define fj(a,b) for(int j = a; j<=b; j++)
#define fo(a,b) for(int o = a; o<=b; o++)
#define ZERO(x) memset(x, 0, sizeof(x))

using namespace std;

#define MAX 1003

int T, n;
int ar1[MAX];
int ar2[MAX];
int ans;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	fo(1, T) {
		ans = 0;
		ZERO(ar1);
		ZERO(ar2);
		scanf("%d", &n);
		fi(0, n - 1) {
			scanf("%d %d", &ar1[i], &ar2[i]);
		}
		if(n == 1) {
			printf("Case #%d: %d\n", o, ans); 
			continue;
		}
		fi(0, n - 2) {
			fj(i + 1, n - 1) {
				if((ar1[j] < ar1[i] && ar2[j] > ar2[i]) || (ar1[j] > ar1[i] && ar2[j] < ar2[i])) ans++;
			}
		}
		printf("Case #%d: %d\n", o, ans); 
	}
}