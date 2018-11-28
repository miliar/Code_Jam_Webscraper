#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

void calc(int no)
{
	int p, k, l;
	unsigned long long ans = 0;
	int i;
	cin >> p >> k >> l;
	vector<unsigned long long> x(l);
	
	for (i = 0; i < l; i++) {
		cin >> x[i];
	}
	
	sort(x.rbegin(), x.rend() );
	for (i = 0; i < l; i++) {
		ans += x[i] * (i / k + 1);
	}
	
	printf("Case #%d: %llu\n", no, ans);
	
	return;
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
