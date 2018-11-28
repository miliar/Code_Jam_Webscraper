#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int main(){

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("cout.txt", "w", stdout);

	int T;
	int cas = 1;
	int n, l, h;
	int num[105];

	scanf("%d", &T);
	while (T--){
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);

		bool sflag = false;
		printf("Case #%d: ", cas++);

		for (int i = l; i <= h; ++i){
			bool flag = true;
			for (int j = 0; j < n; ++j){
				if (i%num[j] != 0 && num[j]%i != 0){
					flag = false;
					break;
				}
			}
			if (flag){
				sflag = true;
				printf("%d\n", i);
				break;
			}		
		}

		if (!sflag)
			printf("NO\n");
	}
	
	return 0;
}