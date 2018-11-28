#include<stdio.h>
#include<vector>

using namespace std;

const int lg = 1005;

int teste, test;
void echo(long long val){
	printf("Case #%d: %lld\n", test, val);
}

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	scanf("%d", &teste);
	for (test = 1; test <= teste; test ++){
		long long r = 0, k = 0, n = 0, suma = 0, i = 0, j = 0, w[lg] = {0}, val[lg] = {0}, next[lg] = {0}, poz = 0, rsp = 0;

		fprintf(stderr, "%d\n", test);

		scanf("%lld%lld%lld", &r, &k, &n);
		for (i = 1; i <= n; i ++){
			scanf("%lld", &w[i]);

			suma += w[i];
		}

		if (suma <= k){
			echo(suma * r);
			continue;
		}

		vector<int> v;
		v.push_back(0);
		for (i = 1; i <= n; i ++)
			for (j = 1; j <= n; j ++)
				v.push_back(w[j]);

		for (i = 1; i <= n; i ++){
			for (j = i, suma = 0; suma <= k; j ++)
				suma += v[j];
			j --;

			val[i] = suma - v[j];
			next[i] = j % n;
			if (next[i] == 0)
				next[i] = n;
		}

		//for (i = 1; i <= n; i ++)
		//	printf("%lld %lld\n", next[i], val[i]);

		rsp = 0;
		for (i = 1, poz = 1; i <= r; i ++, poz = next[poz])
			rsp += val[poz];

		echo(rsp);
	}

	return 0;
}

