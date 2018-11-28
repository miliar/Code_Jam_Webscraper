#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int power10[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int n10 = sizeof(power10)/sizeof(4);
vector<int> pasang[2000005];
set<int> himpunan;

struct scmp {
	bool operator() (const int a, const int b) const {
		return a <= b;
	}
};

int getLength(int nilai)
{
	for (int i = 1; i < n10; i++)
		if (power10[i-1] <= nilai && nilai <= power10[i]-1) return i;
	return n10;
}

bool cmp(int a, int b)
{
	return a <= b;
}

int main()
{
	freopen("Cinput.txt", "r", stdin);
	freopen("Coutput.txt", "w", stdout);
	int batas = 2000000;
	int i, j, num, len, newNum, divisor;
	int tc, nc, res, a, b;
	set<int>::iterator it;
	for (i = 12; i <= batas; i++) {
		num = i;
		len = getLength(i);
		for (j = 1; j < len; j++) {
			divisor = power10[j];
			newNum = num/divisor+(num%divisor)*power10[len-j];
			if (newNum > num)
				himpunan.insert(newNum);
		}
		for (it = himpunan.begin(); it != himpunan.end(); it++)
			pasang[i].push_back(*it);
		himpunan.clear();
	}
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		res = 0;
		scanf("%d%d", &a, &b);
		for (i = a; i <= b; i++) {
			len = pasang[i].size();
			for (j = 0; j < len; j++)
				if (pasang[i][j] > b) break;
			res += j;
		}
		printf("Case #%d: %d\n", nc, res);
	}
}
