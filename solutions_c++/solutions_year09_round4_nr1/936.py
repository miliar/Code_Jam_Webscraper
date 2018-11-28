#include <cstdio>
#include <vector>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
int cases, n;
int a[200];
char s[100];
scanf("%d", &cases);
for (int t_case = 0; t_case < cases; t_case++) {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", s);
		int k = strlen(s);	
		for (; k>0; k--) if (s[k-1] == '1') break;
		a[i] = k;
	}
	int sol = 0;
	for (int i = 0; i < n; i++) {
		int k = i;
		while (a[k] > i+1) k++;
		sol += k-i;
		for (int j = k; j > i; j--) {int l = a[j]; a[j] = a[j-1]; a[j-1] = l;}
	}
	printf("Case #%d: %d\n", t_case+1, sol);
}

	return 0;
}
