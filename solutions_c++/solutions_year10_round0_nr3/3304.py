#include<iostream>
#include<queue>
using namespace std;
int main(){
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout); 
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		int R, K, N;
		long long euros = 0;
		queue<int> q;
		scanf("%d %d %d", &R, &K, &N);
		for(int j = 0; j < N; ++j){
			int num;
			scanf("%d", &num);
			q.push(num);
		}
		for(int j = 0; j < R; ++j){
			long long sum = 0;
			int count = 0;
			while(1){
				if(sum + q.front() <= K && count < N){
					count++;
					sum += q.front();
					q.push(q.front());
					q.pop();
				}
				else
					break;
			}
			euros += sum;
		}
		printf("Case #%d: %d\n", i, euros);
	}
	return 0;
}
