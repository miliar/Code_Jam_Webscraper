/*
 * Author: NomadThanatos
 * Created Time:  2012/4/14 15:32:43
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;

#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())

const int MAXINT = -1u>>1;

int main() {
	freopen("B.out","w",stdout);
	int T,ca = 1;
	int N,S,P;
	scanf("%d",&T);
	while(scanf("%d%d%d",&N,&S,&P) == 3) {
		int res = 0;
		for(int i = 0 ; i < N ; i++) {
			int tmp;
			scanf("%d",&tmp);
			if (tmp >= 3 * P - 2) {
				res++;
				continue;
			}
			if (P - 2 >= 0 && tmp >= 3 * P - 4 && S > 0) {
				res++;
				S--;
				continue;
			}
		}
		printf("Case #%d: %d\n",ca,res);
		ca++;
	}
    return 0;
}

