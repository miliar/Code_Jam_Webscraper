#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int N,Na,Nb,T;
int A[2][10000], B[2][10000];
char ar[6];

int mkTime(char *A) {
	return (((int)(A[0]-'0'))*10+((int)(A[1]-'0')))*60+((int)(A[3]-'0'))*10+((int)(A[4]-'0'));
}

int f(const void * a, const void * b) {
	return *(int*)a-*(int*)b;
}

int solve(int * A, int Na, int * B, int Nb) {
	int ans = 0;
	while(Nb--) {
		Na--;
		while(Na>=0&&A[Na]>B[Nb]) {
			Na--;
		}
		if(Na<0) ans++;
	}
	return ans;
}

int main() {
	int i,n;
	freopen("cpp1.in","r",stdin);
	freopen("cpp1.out","w",stdout);
	scanf("%d",&N);
	for(n=1;n<=N;n++) {
		scanf("%d %d %d",&T,&Na,&Nb);
		for(i=0;i<Na;i++) {
			scanf("%s",ar);
			A[0][i] = mkTime(ar);
			scanf("%s",ar);
			A[1][i] = mkTime(ar)+T;
		}
		for(i=0;i<Nb;i++) {
			scanf("%s",ar);
			B[0][i] = mkTime(ar);
			scanf("%s",ar);
			B[1][i] = mkTime(ar)+T;
		}
		qsort(A[0],Na,sizeof(int),f);
		qsort(A[1],Na,sizeof(int),f);
		qsort(B[0],Nb,sizeof(int),f);
		qsort(B[1],Nb,sizeof(int),f);
		printf("Case #%d: %d %d\n",n,solve(B[1],Nb,A[0],Na),solve(A[1],Na,B[0],Nb));
	}
	return 0;
}