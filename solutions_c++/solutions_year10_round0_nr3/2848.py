/*
 * p1.cpp
 *
 *  Created on: 08-May-2010
 *      Author: user
 */

#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <sstream>
#include <cstring>
#include <ctype.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
//	freopen("input.in", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	//	int i = 0;
	int casenumber = 0;
	while (T--) {
		casenumber++;
		long R, K;
		int N;
		scanf("%ld %ld %d", &R, &K, &N);

		queue<long> V;
		for (int i = 0; i < N; i++) {
			long t;
			scanf("%ld ", &t);
			V.push(t);
		}
		//		printf("\nread:");
		//		for (int i = 0; !V.empty(); i++) {
		//			printf("%d ", V.front());
		//			V.pop();
		//		}

		long money = 0;
		for (long i = 0; i < R; i++) {
			long fill = 0;
			queue<long> Q;
			do {
				if(V.empty())
					break;
				long first = V.front();
				if (fill + first <= K) {
					V.pop();
					Q.push(first);
					money += first;
					fill += first;
				} else
					break;
			} while (1);

			while(!Q.empty())
			{
				V.push(Q.front());
				Q.pop();
			}
		}
		printf("Case #%d: %ld\n", casenumber, money);
	}

}

