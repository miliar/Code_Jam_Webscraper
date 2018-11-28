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
#include <sstream>
#include <cstring>
#include <ctype.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int i = 0;
	while (T--) {
		i++;
		long N, K;
		scanf("%ld %ld", &N, &K);
//		cout << "N=" << N << " l=" << K;//<<endl;

		printf("Case #%d: ", i);
		long lim = (1 << N);
//				cout<<"L="<<lim<<endl;

		char *s;
//		if(K==lim)

		K++;
		if(K >= lim && (K%lim) == 0)
			printf("ON\n");
		else
			printf("OFF\n");

//		printf("%s\n",s);
		fflush(stdout);
	}

}

