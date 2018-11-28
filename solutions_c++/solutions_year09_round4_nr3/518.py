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

int M[100][100];
int nodeAccountedFor[100];
int series[100][25];

bool seriesCross(int* A, int* B, int n) {
	if (A[0] < B[0]) {
		for (int i = 1; i < n; i ++) {
			if (A[i] >= B[i])
				return true;
		}
		return false;
	} else if (A[0] > B[0]) {
		for (int i = 1; i < n; i ++) {
			if (A[i] <= B[i])
				return true;
		}
		return false;
	}
	
	return true;
}

bool isClique(int* flag, int n) {
	for (int i = 0; i < n; i++) {
		if (flag[i]) {
			for (int j = i+1; j < n; j++) {
				if (flag[j]) {
					if (M[i][j] == 0)
						return false;
				}
			}
		}
	}
	return true;
}

bool hasNext(int* flag, int n) {
	for (int i = 0; i < n; i++) {
		if (flag[i] == 0)
			return true;
	}
	return false;
}

void moveToNext(int* flag, int n) {
	for (int i = 0; i < n; i++) {
		if (flag[i] == 0) {
			flag[i] = 1;
			return;
		}
		else
			flag[i] = 0;
	}
}

int sum(int* flag, int n) {
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (flag[i])
			count++;
	}
	return count;
}

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
		int nNodes, seriesLength;
		scanf("%d %d",&nNodes,&seriesLength);
		
		for (int n = 0; n < nNodes; n++) {
			for (int k = 0; k < seriesLength; k++) {
				scanf("%d",&series[n][k]);
			}
			nodeAccountedFor[n] = 0;
		}
		
		for (int a = 0; a < nNodes; a++) {
			for (int b = 0; b < nNodes; b++) {
				if (seriesCross(series[a],series[b],seriesLength)) {
					M[a][b] = 1;
				} else
					M[a][b] = 0;
			}
		}

		int n = nNodes;
		int maxCliqueSize = 0;
		int* flag = new int[n];
		
		while (hasNext(flag,n)) {
			moveToNext(flag,n);
			if (isClique(flag,n)) {
				int d = sum(flag,n); 
				if (d > maxCliqueSize)
					maxCliqueSize = d;
			}
		}
		printf("Case #%d: %d\n",caseNum,maxCliqueSize);
	}
}
