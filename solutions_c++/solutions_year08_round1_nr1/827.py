#include <iostream>
#include <cstdlib>

using namespace std;

int x[1000], y[1000];

int cmp1(const void *a, const void *b){
	int *aa = (int *)a;
	int *bb = (int *)b;
	return *aa - *bb;
}

int cmp2(const void *a, const void *b){
	int *aa = (int *)a;
	int *bb = (int *)b;
	return *bb - *aa;
}

int main()
{
	int kase, T, N;
	cin >> T;
	for (kase = 1; kase <= T; kase++){
		cin >> N;
		int i;
		for (i = 0; i < N; i++)
			cin >> x[i];
		for (i = 0; i < N; i++)
			cin >> y[i];

		qsort(x, N, sizeof(int), cmp1);
		qsort(y, N, sizeof(int), cmp2);
		long long ans = 0;
		for (i = 0; i < N; i++)
			ans += x[i] * y[i];
		cout << "Case #" << kase << ": " << ans << endl;
	}
return 0;
}

