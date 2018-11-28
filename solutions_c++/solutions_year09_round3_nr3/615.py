#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>

#define MAXN 1
#define INF 0x3f3f3f3f
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define TAM(a) ((int) a.size())
#define pb push_back
#define sb substr
#define wr(a) cout << (a) << endl
#define ABS(x) (((x)< 0) ? (-(x)) : (x))
#define CMP(a, b) (a).compare((b)) 
#define achou(c,x) ((c).find(x) != (c).end()) 
#define reset(c,a) memset(c, a, sizeof(c))
#define ord(c,d) qsort(c, d, sizeof(c[0]), compara) 

using namespace std;

int pd[10004][128];
int vet[128];
int solve(int i, int j){
	//printf("%d %d\n", i, j);
	if(pd[i][j] != -1) return pd[i][j];
	if(i==j){
		return pd[i][j] = 0;
	}
	int menor = INF;
	for(int k=i;k<=j;k++){
		if(vet[k] == 1){
			menor = min(menor, solve(i,k-1) + solve(k+1, j) + (k-i) + (j-k));
		}
	}
	if(menor == INF) menor = 0;
	return pd[i][j] = menor;
}

int main (void){
	int n, q;
	int t;
	scanf("%d", &t);
	int teste = 1;
	while(t--){
		scanf("%d%d", &n, &q);
		reset(vet, 0);
		int ind;
		FOR(i,0,q){
			scanf("%d", &ind);
			vet[ind] = 1;
		}
		reset(pd, -1);

		printf("Case #%d: %d\n", teste++, solve(1,n));
	}
	return 0;
}