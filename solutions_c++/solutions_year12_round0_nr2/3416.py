#include <stdio.h>
#include <algorithm>

using namespace std;


int main(){
	int T = 1;
	int N,S,P;
	int temp;
	int result, suprise;
	scanf("%d", &T);
	for (int i = 0; i < T; i++){
		scanf("%d", &N);
		scanf("%d", &S);//suprising triplets
		scanf("%d", &P);//points
		result = 0;
		suprise = 0;
		if ( P == 0){
			for ( int j = 0; j < N; j++)scanf("%d", &temp);
			result = N;
		} else {
			for (int j = 0; j < N; j++){
				scanf("%d", &temp);
				if ( temp > max( 0, (3 * P - 3) ) )result++;
				else if ( temp > max( 0, (3 * P - 5) ) )suprise++;
			}
			result += min(suprise, S);
		}
		printf("Case #%d: %d\n", i + 1, result);
	}
	return 0;
}

