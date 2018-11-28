#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
int hasPower[32];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int g = 1; g <= tests; g++){
		int r,k,n;
		queue<int> q;
		scanf("%d %d %d",&r,&k,&n);
		for (int i = 0; i < n; i++){
			int t;
			scanf("%d",&t);
			q.push(t);
		}
		int sum = 0;
		for (int i = 0; i < r; i++){
			int csum = 0;
			int j = 0;
			int len = q.size();
			while (true){
				if (csum + q.front() <= k && j < len){
					csum += q.front();
					q.push(q.front());
					q.pop();
					j++;
				}else{
					sum += csum;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",g,sum);
	}
	return 0;
}