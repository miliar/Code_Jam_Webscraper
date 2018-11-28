#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1100
#define MAXNUM 110000000
int N;
int n[MAXN];


int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		int all = 0;
		int smallest = MAXNUM;
		int test = 0;
		scanf("%d", &N);
		for(int i = 0;i < N; i++){
			scanf("%d", &n[i]);
			test ^= n[i];
			all += n[i];
			smallest = min(n[i], smallest);
		}
		if(test != 0){
			printf("Case #%d: NO\n", casenum++);
			continue;
		}
/*
		int ans = 0;

		for(int i = 25;i >= 0; i-- ){
			int mask = (1<<i);
			int num = 0;
			int total = 0;
			int small = MAXNUM;
			for(int j = 0;j < N; j++){
				if((mask & n[j]) && (n[j] < (mask << 1))){
					num++;
					total += n[j];
					small = min(n[j], small);
					//cout<<mask<<" "<<n[j]<<endl;
				}
			}
			if(num == N){
				ans += total - small;
				break;
			}else if(num % 2 == 1){
				//take the smallest element to Patrick
				ans += total - small;
				//break;
			}else{
				//take all
				ans += total;
			}
		}
		if(ans == all){
			ans -= smallest;
		}*/
		printf("Case #%d: %d\n", casenum++, all - smallest);
	}
	return 0;
}

