#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <queue>
#include <map>
#include <stack>
using namespace std;

int main(){
	
	freopen("D-large.in", "r", stdin);
	freopen("D-large.txt", "w", stdout);

	int T;
	int cas = 1;
	int n;
	int num;

	scanf("%d", &T);
	while (T--){
		scanf("%d", &n);
		int ans = 0;
		for (int i = 1; i <= n; i++){
			scanf("%d", &num);
			if (num != i)
				ans++;
		}
		printf("Case #%d: %.6lf\n",cas++, ans*1.0);

	}
	return  0;
}
