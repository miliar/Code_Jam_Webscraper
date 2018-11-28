#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <cmath>
using namespace std;


char inp[1000010];
char res[1000010];
int dig1[10];
int dig2[10];
bool ok;
int len;
bool rec(int index) {
	if (ok == true)
		return ok;
	if (inp[index] == 0)
		return false;
	int val = inp[index] - '0';
	if (dig1[val] > 0) {
		dig1[val]--;
		res[index] = val + '0';
		if (rec(index + 1) == true)
			return true;
		else
			dig1[val]++;
	}
	for (int i = val + 1; i < 10; ++i) {
		if (dig1[i] > 0) {
			res[index] = i + '0';
			dig1[i]--;
			for (int k = 0; k < 10; ++k) {
				while (dig1[k] > 0) {
					res[++index] = k + '0';
					dig1[k]--;
				}
			}
			ok = true;
		}
	}
	return ok;
}

int main() {
	freopen("C:\\in.txt", "r", stdin);
	freopen("C:\\out.txt", "w", stdout);
	int t = 0;
	scanf("%d\n", &t);
	for (int test = 1; test <= t; ++test) {
		gets(inp);
		memset(dig1, 0, sizeof(dig1));
		memset(dig2, 0, sizeof(dig2));
		memset(res, 0, sizeof(res));
		for (int i = 0; inp[i] != 0; ++i) {
			dig1[inp[i] - '0']++;
			dig2[inp[i] - '0']++;
		}
		ok = false;
		printf("Case #%d: ", test);
		if (rec(0) == true) {
			puts(res);			
		} else {
			int len = strlen(inp);
			for (int i = 1; i < 10; ++i) {
				if (dig2[i] > 0) {
					printf("%c0", i + '0');
					dig2[i]--;
					break;
				}
			}
			for (int i = 0; i < 10; ++i) {
				while (dig2[i] > 0) {
					printf("%c", i + '0');
					dig2[i]--;
				}
			}
			printf("\n");
		}
	}
	return 0;
}
