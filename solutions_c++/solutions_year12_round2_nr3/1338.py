//============================================================================
// Name        : 3.cpp
// Author      : lw
// Version     :
// Copyright   : ;]
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

bool kolejnyv2(vector<int> &v, vector<int> &v1, int ile, int N, int sum1,
		int sum2) {
	if (sum1 < sum2)
		return false;
	else if (ile < N) {
		if (v1[ile] == 0) {

			if (kolejnyv2(v, v1, ile + 1, N, sum1, sum2))
				return true;
			v1[ile] = 2;
			if (kolejnyv2(v, v1, ile + 1, N, sum1, sum2 + v[ile]))
				return true;
			v1[ile] = 0;
		} else if (kolejnyv2(v, v1, ile + 1, N, sum1, sum2))
			return true;

	} else {
		if (sum1 == sum2 && sum1 != 0)
			return true;
	}
	return false;
}

bool kolejnyv1(vector<int> &v, vector<int> &v1, int ile, int N, int sum1) {
	if (ile < N) {
		v1[ile] = 0;
		if (kolejnyv1(v, v1, ile + 1, N, sum1))
			return true;
		v1[ile] = 1;
		if (kolejnyv1(v, v1, ile + 1, N, sum1 + v[ile]))
			return true;
		v1[ile] = 0;
	} else if (kolejnyv2(v, v1, 0, N, sum1, 0))
		return true;
	return false;
}

int main() {
	int T = 1;
	int N;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		vector<int> v(N);
		for (int j = 0; j < N; j++)
			scanf("%d", &v[j]);
		//mamy wczytane dane
		sort(v.begin(), v.end());
		//posortowane w porzadku rozsnacym
		vector<int> v1(N, 0);
		printf("Case #%d:\n", i + 1);
		if (kolejnyv1(v, v1, 0, N, 0)) {
			for (int j = 0; j < N; j++)
				if (v1[j] == 1)
					printf("%d ", v[j]);
			printf("\n");
			for (int j = 0; j < N; j++)
				if (v1[j] == 2)
					printf("%d ", v[j]);
					printf("\n");
		} else{
			
			printf("Impossible");
			printf("\n");
			}
			
			
			

	}

	return 0;
}
