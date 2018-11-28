#include <iostream>
#include <cstdio>
#include <set>
#include <string>
#include <cstring>

using namespace std;

set<string> dirs;

char tmp[101];
int len;

int insert() {
	int r = 0;
	while (len) {
		if (dirs.find(tmp) == dirs.end()) {
			r++;
			dirs.insert(tmp);
		}
		
		while (tmp[len - 1] != '/') len--;
		len--;
		tmp[len] = 0;
	}	
	return r;
}

inline void task() {
	dirs.clear();
	
	int a, b;
	scanf("%d %d", &a, &b); gets(tmp);
	for (int i = 0; i < a; i++) {
		gets(tmp);
		dirs.insert(tmp);
	}
	
	int r = 0;
	for (int i = 0; i < b; i++) {
		gets(tmp);
		len = strlen(tmp);
		r += insert();
	}
	
	printf("%d\n", r);
}

int main() {
	int t;
	scanf("%d", &t); gets(tmp);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		task();
	}
}

