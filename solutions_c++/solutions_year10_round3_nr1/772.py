#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

# define INF 0x3f3f3f3f

# define MAXN 1024

using namespace std;

int tc = 1;
int T;

int A[MAXN];
int B[MAXN];
int N;
int main (void){
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", tc++);
		scanf("%d", &N);
		for(int i = 0;i<N;i++){
			scanf("%d%d", &A[i], &B[i]);
		}
		int cnt = 0;
		for(int i = 0;i<N;i++){
			for(int j = 0;j<N;j++){
				if(i==j) continue;
				if(A[j] > A[i] && B[j] < B[i]) cnt++;
				if(A[j] < A[i] && B[j] > B[i]) cnt++;
			}
		}
		printf("%d\n", cnt/2);
	}
	return 0;
}