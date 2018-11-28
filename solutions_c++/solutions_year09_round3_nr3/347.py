/*
 * Prison.C
 *
 *  Created on: Sep 13, 2009
 *      Author: pvncad
 */


#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main () {
	int T;
	scanf("%d", &T);
	for (int ci = 1; ci <= T; ci ++)
	{
		int P, Q;
		scanf("%d%d", &P, &Q);
		int c[P];
		int p[Q];
		for (int i = 0; i < P; i ++) {
			c[i] = i;
		}
		for (int i = 0; i < Q; i ++) {
			scanf("%d", &p[i]);
			p[i] --;
		}
		int minbribe = -1;
		do {
			int bribe = 0;

			for (int i = 0; i < P; i ++) {
				c[i] = i;
			}

			for (int i = 0; i < Q; i ++) {
				int rel = p[i];

				for (int j = rel - 1; j >= 0; j --) {
					if (c[j] != -1) {
						bribe ++;
					}
					else {
						break;
					}
				}
				for (int j = rel + 1; j < P; j ++) {
					if (c[j] != -1) {
						bribe ++;
					}
					else {
						break;
					}
				}
				c[rel] = -1;
			}

			if (minbribe == -1 || minbribe > bribe) {
				minbribe = bribe;
			}
		}while (next_permutation(p , p + Q));

		printf("Case #%d: %d\n", ci, minbribe);
	}
		return 0;

}
