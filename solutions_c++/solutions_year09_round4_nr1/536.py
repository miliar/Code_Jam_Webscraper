#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <assert.h>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>

#define INDEX_MAX 41 

using namespace std;

int C[INDEX_MAX][INDEX_MAX];

///////////////////////

double exp[INDEX_MAX];

//////////////////////
int main () {
	for (int i = 0; i < INDEX_MAX; i++) {
		C[i][i]=C[i][0] = 1;
		for (int j = 0; j < i; j++)
			C[i][j] = C[i-1][j] + C[i-1][j-1];	
	}
	
	////////////////////////////////////////////
	
	int nCases = 0;
	scanf("%d",&nCases);
	
	for (int caseNum = 1; caseNum <= nCases; caseNum++) {
		
		int N;
		scanf("%d",&N);
		
		int* X = new int[N];
		char* line = new char[N+1];
		
		for (int n = 0; n < N; n++) {
			scanf("%s",line);
			X[n] = 0;
			for (int i = 0; i < N; i++) {
				if (line[i] == '1')
					X[n] = i;
			}
			//printf("%d ",X[n]);
		}
		
		int count = 0;
		for (int n = 0; n < N; n++) {
			int idx = n;
			
			while (X[idx] > n) {
				idx++;
				count++;
			}
			for (int i = idx; i > n; i--) {
				X[i] = X[i-1];	
			}
		}
		//printf("Case #%d: %.9f\n",caseNum,exp[nCards]);
		printf("Case #%d: %d\n",caseNum,count);
	}
}

