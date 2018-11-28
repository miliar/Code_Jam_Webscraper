
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <cassert>

using namespace std;

int main(){
	
	int t; scanf("%d", &t);
	int s[1001];
	int r[1001];
	map<int, int> g;

	for(int x=1; x<=t; ++x){
		int n; scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%d", &s[i]);
			r[i] = s[i];
		}
		sort(r, r+n);
		g.clear();
		for(int i=0; i<n; ++i){
			g[r[i]] = i;
		}
		for(int i=0; i<n; ++i){
			s[i] = g[s[i]];
		}
		int sum = 0;
		int check = 0;
		int lea, j, ptr;
		for(int i=0; i<n; ++i){
			j = s[i];
			lea = s[i];
			ptr = 1;
			while(j != i){
				if(s[j] < lea){
					lea = s[j];
				}
				j = s[j];
				++ ptr;
			}
			if(lea == s[i]){
				check += ptr;
				if(ptr > 1){
					sum += ptr;
				}
			}
		}

		assert(check == n);

		for(int i=0; i<n; ++i){
			//printf("%d ", s[i]+1);
		}
		printf("Case #%d: %d.000000\n", x, sum);
	}
	return 0;
}
