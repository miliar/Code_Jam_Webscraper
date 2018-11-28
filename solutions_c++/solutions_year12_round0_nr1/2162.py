#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <complex>

using namespace std;

const char go[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char s[200];

inline void solve(int t){
	gets(s);
	int n = strlen(s);
	for(int i = 0; i < n; i++){
		if(s[i] >= 'a' && s[i] <= 'z'){
			s[i] = go[s[i] - 'a'];
		}
	}
	printf("Case #%d: %s\n", t, s);
}

int main(){
	//freopen("abelian.in", "r", stdin);
	//freopen("abelian.out", "w", stdout);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for(int i = 0; i < t; i++){
		solve(i + 1);
	}
	return 0;
}