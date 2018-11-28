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

int lst[100], val[100];

inline void solve(int test){
	int a, b;
	scanf("%d %d", &a, &b);
	int ans = 0;
	for(int i = a; i <= b; i++){
		int sz = 0, cur = i;
		while(cur > 0){
			lst[sz++] = cur % 10;
			cur /= 10;
		}
		reverse(lst, lst + sz);
		int cnt = 0;
		for(int j = 0; j < sz; j++){
			if(lst[j] == 0){
				continue;
			}
			int ch = 0, pos = j;
			for(int z = 0; z < sz; z++){
				ch = ch * 10 + lst[pos++];
				if(pos >= sz){
					pos = 0;
				}
			}
			val[cnt++] = ch;
		}
		sort(val, val + cnt);
		cnt = unique(val, val + cnt) - val;
		for(int j = 0; j < cnt; j++){
			if(val[j] >= a && val[j] <= b && val[j] < i){
				ans++;
			}
		}
	}
	printf("Case #%d: %d\n", test, ans);
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