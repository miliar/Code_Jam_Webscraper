//a Hewr
#include <iostream>
#include <cstdio>
using namespace std;
#define fo(i,a,b) for (int i = a; i <= b; ++i)
#define updmax(a,b) a = max(a, b)

const int mn = 11000;

int f[mn], d[mn], l[mn];
int T, n, des;

int main(){
	scanf("%d", &T);
	fo (Ca, 1, T){
		scanf("%d", &n);
		fo (i, 1, n) scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &des);
		printf("Case #%d: ", Ca);
		if (d[1] > l[1]){
			printf("NO\n");
			continue;
		}
		f[1] = d[1];
		fo (i, 2, n){
			f[i] = 0;
			fo (j, 1, i - 1) if (d[j] + f[j] >= d[i])
				updmax(f[i], min(l[i], d[i] - d[j]));
		}
		bool ok(0);
		fo (i, 1, n) if (d[i] + f[i] >= des){
			ok = 1;
			break;
		}
		if (ok) printf("YES\n");
		else printf("NO\n");
	}
}
