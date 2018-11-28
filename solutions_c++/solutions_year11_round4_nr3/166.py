#include <cstdio>
#include <vector>
using namespace std;


bool bp[1000010];

vector<int> pl;

long long work() {
	long long n;
	scanf("%lld", &n);
	if (n == 1)
		return 0;
	int ans = 1;
	for (int i = 0; i < (int)pl.size() && pl[i] <= n; ++i) {
		long long v = n / pl[i] / pl[i];
		while (v) {
			++ans;
			v /= pl[i];
		}
	}
	return ans;
}

#define maxv 1000010
int main() 
{
	for (int i = 2; i < maxv; ++i) {
		if (bp[i])
			continue;
		pl.push_back(i);
		for (long long j = i * 1LL * i; j <= maxv; j += i)
			bp[j] = 1;
	}
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) 
		printf("Case #%d: %lld\n", Ti, work());
}
