#include <stdio.h>
#include <vector>
using namespace std;

vector<int> tortoise, hare, init;
int R, k, N;

int go(vector<int>& R){
	int p = 0;
	int sum = 0;
	while (p < N && sum  + R[p] <= k)
	{
		sum += R[p];
		p++;
	}
		
	vector<int> shift(N);
	for (int i = 0; i + p < N; ++i) shift[i] = R[i+p];
	for (int i = 0; i < p; ++i) shift[N-p+i] = R[i];
	R = shift;	
	return sum;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int caseID = 1; caseID <= T; ++caseID){
		scanf("%d %d %d",&R,&k,&N);
		
		tortoise.resize(N);		
		hare.resize(N);
		init.resize(N);		
		
		for (int i = 0; i < N; ++i) scanf("%d",&init[i]);
		
		tortoise = init;
		hare = tortoise;
		go(hare);
		go(hare);
		
		while (tortoise != hare){
				go(tortoise);
				go(hare);
				go(hare);		
		}			
		
		int mu = 0; // mu is where the cycle starts
		tortoise = init;
		int ans = 0;
		while (tortoise != hare && R--){
			ans += go(tortoise);
			go(hare);
			mu += 1;			
		}
		
		printf("Case #%d: ", caseID);
		if (!R) {
			printf("%d\n", ans);
			continue;
		}
		
		int ncycle = 1; // find the size and the cost of the cycle
		int cost = 0;
		hare = tortoise;
		cost += go(hare);
		while (tortoise != hare){
			cost += go(hare);
			++ncycle;
		}
		//printf("ncycle = %d\n", ncy
		ans += cost * (R/ncycle);
		int last_part = R%ncycle;
		for (int i = 0; i < last_part; ++i)
			ans += go(tortoise);
		printf("%d\n", ans);
	}

}