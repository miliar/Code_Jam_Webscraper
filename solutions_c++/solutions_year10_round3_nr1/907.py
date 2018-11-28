/*
 * main.cpp
 *
 *  Created on: 22-May-2010
 *      Author: user
 */

#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <cstring>
#include <ctype.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	int wire[1000][2];
	int caseNumber=0;
	while (T--) {
		caseNumber++;
		int N;
		scanf("%d",&N);

		for(int i=0;i<N;i++)
		{	scanf("%d %d",&wire[i][0],&wire[i][1]);
//			printf("%d %d\n",wire[i][0],wire[i][1]);
		}
		int count=0;

		for(int i=0;i<N;i++){

			for (int j = 0; j < N; ++j) {
				if(j==i)
					continue;

				if(wire[j][0]>wire[i][0] && wire[j][1] < wire[i][1])
					count++;
			}
		}

		printf("Case #%d: %d\n",caseNumber,count);
	}

	return 0;
}

