#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
__int64 numbers[100];
int size;
__int64 pow(__int64 base, int times) 
{
	__int64 ret = 1;
	while (times > 0) {
		ret *= base;
		--times;
	}
	return ret;
}
__int64 change(int base)
{
	__int64 ret = 0;
	__int64 ten = base;
	reverse(numbers, numbers + size);
	for (int i=0; i<size; ++i) {
		ret += pow(ten, i) * numbers[i];
	}
	return ret;
}

int main()
{
	freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
//	ifstream fin("c-small.in");
//	ofstream fout("c-small.out");
	int test_case;
	scanf("%d", &test_case);
	for (int tt=1; tt<=test_case; ++tt) {
		__int64 ans = 0;
		bool used[256];
		char input[100];
		memset(used, 0, sizeof used);
		scanf("%s", input);
		int i;
		size = strlen(input);
		char max = '0';
		int base = 0;
		for (i=0; i<size; ++i) {
			if (!used[input[i]]) {
				used[input[i]] = true;
				++base;
			}
		}
		if (base == 1) ++base;
		int setter[256];
		for (i=0; i<256; ++i) setter[i] = -1;
		setter[input[0]] = 1;
		numbers[0] = 1;
		int num_cnt = 0;
		for (i=1; i<size; ++i) {
			if (setter[input[i]] != -1) {
				numbers[i] = setter[input[i]];
			} else {
				if (num_cnt == 1) ++num_cnt;
				numbers[i] = num_cnt;
				setter[input[i]] = num_cnt;
				++num_cnt;
			}
		}
//		for (i=0; i<size; ++i) {
//			printf("%d ", numbers[i]);
//		}
//		printf("base: %d  ", base);
		ans = change(base);
		printf("Case #%d: %I64d\n", tt, ans);
	}

	return 0;
}