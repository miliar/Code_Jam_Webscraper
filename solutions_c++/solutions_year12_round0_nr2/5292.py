//be name oo
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		int ans = 0;
		for(int i = 0; i < n; i++){
			int t;
			scanf("%d", &t);
			bool sur = false, norm = false;
			for(int i = max(t / 3 - 1, 0); i <= min(t / 3 + 2, 10); i++)
				for(int j = max(t / 3 - 1, 0); j <= min(t / 3 + 2, 10); j++)
					for(int k = max(t / 3 - 1, 0); k <= min(t / 3 + 2, 10); k++)
						if(i + j + k == t){
							if(min(i, min(j, k)) + 2 < max(i, max(j, k)))
								continue;
							if(max(i, max(j, k)) < p)
								continue;
							if(min(i, min(j, k)) + 1 < max(i, max(j, k)))
								sur = true;
							else
								norm = true;
						}
// 			cerr << norm << endl;
			if(norm)
				ans++;
			else{
				if(sur && s){
// 					cerr << p << end;
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}

