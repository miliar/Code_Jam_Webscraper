#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int T, N, S, P, cap1, cap2, count;
	scanf("%d", &T);
	
	for(int j=0; j<T; j++){
		count = 0;
		scanf("%d %d %d", &N, &S, &P);
		vector<int> vec(N);
		
		cap1 = 3*P - 2; //No need for surprise 
		cap1 = max(cap1, 0);
		cap2 = 3*P - 4; //Lower limit for surprise : O
		cap2 = max(cap2, 0);

		for(int i=0; i<N; i++){
			scanf("%d", &vec[i]);
		}
		sort(vec.rbegin(), vec.rend());		

		for(int i=0; i<N; i++){
			if(P && vec[i] == 0)
				continue;
			if(vec[i]>=cap1){
				count++;
			}else if(S && vec[i]>=cap2){
				count++;
				S--;
			}
		}
		
		printf("Case #%d: %d\n", (j+1), count);
	}
	return 0;
}
