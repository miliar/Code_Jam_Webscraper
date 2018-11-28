#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;
int check(int* data, int n)
{
	if (data[0] == 0) return 0;
	for (int i = 0; i < n - 1; ++i) if (data[i] > data[i+1]) return 1;
	return 0;
}
int main()
{freopen("r1b\\B-large.in", "r", stdin);
freopen("r1b\\B-large.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int id = 1;
	while (cas--)
	{
		long long n;
		vector<int> vec;
		string str;
		cin >> str;
		int k = str.length();
		for (int i = 0; i < k; ++i) vec.push_back(str[i]-'0');
		//reverse(vec.begin(), vec.end());
		next_permutation(vec.begin(), vec.end());
		printf("Case #%d: ", id++);
		if (check(&vec[0], vec.size()))
		{
			for (int i = 0; i < vec.size(); ++i) printf("%d", vec[i]);
		}
		else
		{
			int where;
			for (where = 0; ; ++where) if (vec[where] != 0) break;
			printf("%d0", vec[where]);
			vec.erase(vec.begin() + where);
			for (int i = 0; i < vec.size(); ++i) printf("%d", vec[i]);
		}
		puts("");
	}
	return 0;
}
