#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

long long sc(vector<long long> &a, vector<long long> &b)
{
	long long res  =0;
	for (long long i =0; i < a.size(); ++i)
		res += a[i] * b[i];
	return res;
}

void rv(vector<long long> &a, long long n)
{
	a.clear();
	long long tmp;
	for (long long i = 0; i < n; ++i) {
		scanf("%lld", &tmp);
		a.push_back(tmp);
	}
}

long long go()
{
	long long n;
	scanf("%lld", &n);
	vector<long long> a, b;
	rv(a, n); rv(b, n);
	sort(a.begin(), a.end());
	sort(b.rbegin(), b.rend());
	return sc(a, b);
}

void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t;
	scanf("%lld", &t);
	for (long long i = 0; i < t; ++i)
		printf("Case #%lld: %lld\n", i+1, go());
}