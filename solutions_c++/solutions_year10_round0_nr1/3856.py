#define _CRT_SECURE_NO_DEPRECATE
#include<stdio.h>

#define fi(a,b) for(i=a;i<=b;i++)
#define fj(a,b) for(j=a;j<=b;j++)

int chek[31];
int tok[31];
int ans[31];
int n, k, t;

int main() {
	int i, j;
	int d = 0;
	tok[1] = 1;
	int f;
	freopen("a.in","r", stdin);
	freopen("a.out","w", stdout);
	scanf("%d", &t);
	ans[1] = 1;
	fi(2, 30) {
		ans[i] = ans[i - 1] * 2 + 1;
	}
	/*while(ans[20] == 0) {
		d++;
		f = 0;
		fj(1, 30) {
			if(tok[j]) chek[j] = !chek[j];
			else break;
		}
		fj(1, 30) {
			if(!chek[j] && !f) {
				f = 1;
				tok[j] = 1;
				continue;
			}
			if(!f) tok[j] = 1;
			else tok[j] = 0;
		}
		fj(1, 30) {
			if(tok[j] && chek[j] && !ans[j]) {
				ans[j] = d;
			}
		}
	}*/
	fi(1, t) {
		scanf("%d %d", &n, &k);
		d = k % (ans[n] + 1);
		if(d == ans[n]) {
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}