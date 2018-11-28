#include <cstdio>

int r, k, n;
long long a[2000], total[2000], next[2000];

void solve(int caz){
    long long sum = 0;
    scanf("%d %d %d", &r, &k, &n);
    for (int i=0; i<n; sum += a[i++])
        scanf("%d", a+i);
    for (int i=0; i<n; i++){
        total[i] = 0;
        next[i] = i;
        while (total[i] < sum && total[i] + a[next[i]] <= k){
            total[i] += a[next[i]];
            next[i] = (next[i] + 1) % n;
        }
    }
    long long rez = 0;
    int poz = 0;
    while (r--){
        rez += total[poz];
        poz = next[poz];
    }
    printf("Case #%d: %I64d\n", caz, rez);
}

int main(){
	freopen("input.txt", "rb", stdin);
	freopen("output.txt", "wb", stdout);
	int tst;
	scanf("%d", &tst);
	for (int i=1; i<=tst; i++)
        solve(i);
    return 0;
}
