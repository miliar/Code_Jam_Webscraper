#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;

int main(){
  int C;
  scanf("%d", &C);
  for(int c = 1; c <= C; ++c){
	int P, Q;
	bool released[10005];
	int to_be_released[20];
	scanf("%d%d", &P, &Q);
	for(int i = 0; i < Q; ++i){
		scanf("%d", &to_be_released[i]);
		to_be_released[i]--;
	}
	sort(to_be_released, &to_be_released[Q]);
	int min_coins = P*Q;
	do {
		for(int i = 0; i < P; ++i)
			released[i] = false;

		int tmp_coins = 0;
//		for(int i = 0; i < Q; ++i){
//			printf("%d ", to_be_released[i]);
//		}
//		printf("\n");
		for(int i = 0; i < Q; ++i){
			int step_coins = 0;
			released[to_be_released[i]] = true;
			int iter = to_be_released[i] - 1;
			while(iter >= 0 && released[iter] == false){
				step_coins++;
				--iter;
			}
			iter = to_be_released[i] + 1;
			while(iter < P && released[iter] == false){
				step_coins++;
				++iter;
			}
//			printf("%d : %d\n", i, step_coins);
			tmp_coins += step_coins;
		}
		min_coins = min(min_coins, tmp_coins);
//		printf(" -> %d\n", tmp_coins);
	}while(next_permutation(to_be_released, &to_be_released[Q]));
    printf("Case #%d: %d\n", c, min_coins);
  }
  return 0;
}
