#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

struct astr {
	int type;
	int flavor;
};

vector<astr> cust[3000];
int N,M;

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	int i,j,k;
	int pow2[30];
	pow2[0]=1;
	for (i=1; i<=20; i++) {
		pow2[i]=2*pow2[i-1];
	}
	for (t=1; t<=T; t++) {
		scanf("%d %d", &N, &M);
		for (i=0; i<M; i++) {
			int x;
			scanf("%d", &x);
			cust[i].clear();
			for (j=0; j<x; j++) {
				astr y;
				scanf("%d %d", &y.flavor,&y.type);
				y.flavor--;
				cust[i].push_back(y);
			}
		}
		int anse=-1;
		int minbatch=1000;
		for (i=0; i<pow2[N]; i++) {
			for (j=0; j<M; j++) {
				for (k=0; k<cust[j].size(); k++) {
					int f=cust[j][k].flavor;
					int p=cust[j][k].type;
					bool ada=i & pow2[f];
					if (ada==p) break;
				}
				if (k==cust[j].size()) break;
			}
			if (j==M) {
				int nbatch=0;
				for (k=0; k<N; k++) {
					if (i & pow2[k])
						nbatch++;
				}
				if (anse==-1 || nbatch<minbatch) {
					minbatch=nbatch;
					anse=i;
				}
			}
		}
		if (anse==-1) {
			printf("Case #%d: IMPOSSIBLE\n",t);	
		}
		else {
			printf("Case #%d:",t);
			for (i=0; i<N; i++) {
				if (anse & pow2[i])
					printf(" 1");
				else
					printf(" 0");
			}
			printf("\n");
		}
	}
	return 0;
}