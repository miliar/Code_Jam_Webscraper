#include <cstdio>
#include <utility>

using namespace std;

const int N = 1003;

int n;
long long size;
int v[N];
long long sum[N];

void make_sums(){
	sum[0] = v[0];
	for (int i = 1; i < n; i++)
		sum[i] = sum[i - 1] + (long long) v[i];
}

long long get_sum(int begin, int end){ //inclusive
	if (begin == 0) return sum[end];
	return sum[end] - sum[begin - 1];
}

pair < long long, int > run(int begin, int end = n, long long max_size = size){
	int b = begin, e = end, last = b;
	long long c_sum = 0;
	//printf("max_size = %d, b = %d, e = %d\n", max_size, b, e);
	while (b < e){
		int mid = (b + e) / 2;
		if (get_sum(b, mid) + c_sum <= max_size) c_sum += get_sum(b, mid), last = mid, b = mid + 1;
		else e = mid;
	}
	pair < long long, int > ans;
	ans.first = get_sum(begin, last);
	//printf("ans.first = %d\n", ans.first);
	ans.second = (last + 1) % n;
	if (begin > 0 && ans.second == 0 && ans.first < max_size){
		pair < long long, int > ans2 = run(0, begin, max_size - ans.first);
		if (ans.first + ans2.first > max_size) return ans;
		ans.first += ans2.first;
		ans.second = ans2.second;
	}
	return ans;
}

int main(){
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++){
		int runs;
		scanf("%d %lld %d", &runs, &size, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &v[i]);
		make_sums();
		long long ans = 0;
		int curr = 0;
		while (runs--){
			pair < long long, int > now = run(curr);
			//printf("De %d a %d soma %d\n", curr, now.second, now.first);
			ans += now.first;
			curr = now.second;
		}
		printf("Case #%d: %lld\n", test, ans);
	}

	return 0;
}
