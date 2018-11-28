//============================================================================
// Name        : GCJ-bigint.cpp
// Author      : chris.deyoung
// Version     :
// Copyright   : Your copyright notice
// Description : Google Code Jam, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {

	//	freopen("A.in","r",stdin);
	//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//	freopen("A-small-attempt3.in","r",stdin);freopen("A-small-attempt3.out","w",stdout);
	//	freopen("A-small-attempt4.in","r",stdin);freopen("A-small-attempt4.out","w",stdout);
	//	freopen("A-small-attempt5.in","r",stdin);freopen("A-small-attempt5.out","w",stdout);
	//	freopen("A-small-attempt6.in","r",stdin);freopen("A-small-attempt6.out","w",stdout);
		freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);
		int testcase, N, N2, K;
		int val, ktest;
		int snappers[50];

		scanf(" %d",&testcase);

		for (int caseId=1;caseId<=testcase;caseId++) {
			printf("Case #%d: ",caseId);
			scanf(" %d %d ", &N, &K);
//			printf(" N= %d K= %d\n", N, K);
			for (int i=0; i<40; i++){
				snappers[i] = 0;
			}
			val = 0;
	//		if (K >= N){
				ktest = K;
				for (int i=0; i<ktest; i++){
					if (K==1){
						snappers[i]=1;
						break;
					} else {
						snappers[i]=ktest%2;
						ktest=ktest/2;
					}
				}
				for (int l=0; l<40; l++){
//					printf("%d", snappers[l]);
				}
//				printf("\n %d", K);
				for (int i=0; i<(N-1); i++){
					if (snappers[i] != 1){
//						printf("OFF\n");
						val = 0;
						break;
					}
					else val = 1;
//					printf("ON");
				}
				N2 = 2;
				for (int i=1; i<N; i++){
					N2 = (N2*2);
				}


				N2 = (int) pow((double)2, (double) N);
		//		printf("K+1= %d, N2= %d, ( (K + 1) % ( N2 )= %d ", K+1, N2, (K + 1) % ( N2 ) );
				if ( ( (K + 1) % ( N2 ) ) == 0){
					printf("ON\n");
				} else {
					printf("OFF\n");
				}
		//	}
//			fprintf("\n***\n");
			if (val == 1){
		//		printf("ON\n");
			} else {
		//		printf("OFF\n");
			}
			fflush(stdout);
		}
	return 0;
}
