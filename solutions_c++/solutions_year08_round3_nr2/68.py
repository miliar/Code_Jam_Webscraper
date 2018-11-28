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

unsigned long long ans = 0;

void cnt(string x, long long n, int p)
{
	long long a = 0, b;
	int i;
	
	if (x.size() == 0) return;
	for (i = 0; i < x.size(); i++) {
		a = a * 10 + (x[i] - '0');
		b = n + p * a;
		if (i == x.size() - 1) {
			if (b % 2 == 0 || b % 3 == 0 || b % 5 == 0 || b % 7 == 0) {
				ans++;
			}
		} else {
			cnt(x.substr(i + 1), b, 1);
			cnt(x.substr(i + 1), b, -1);
		}
	}
	return;
}
		
void calc(int no)
{
	string x;
	int i;
	
	cin >> x;
	
	ans = 0;
	
	cnt(x, 0, 1);
	
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
