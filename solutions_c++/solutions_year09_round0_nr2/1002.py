#include <iostream>
#include <strstream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#ifdef LOCAL
#define ll __int64
#define OUTLL "%I64d" 
#else
#define ll long long
#define OUTLL "%lld"
#endif
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SWAP(a,b) a^=b;b^=a;a^=b
using namespace std;

int n;
const int N = 120;
int I, K;
int mat[N][N];
int group[N][N];
int p[N*N];
char no[N*N];
int ng;
char input()
{
	if ( scanf("%d%d", &I, &K) != 2)return 0;
	memset(mat,0x7f,(sizeof mat));
	int i, k;
	for(i=1; i<=I; i++){
		for(k=1; k<=K; k++){
			scanf("%d", &mat[i][k]);
		}
	}
	return 1;
}

int getparent(int i)
{
	if ( p[i] == i)return i;
	p[i] = getparent(p[i]);
	return p[i];
}

int dir[4][2] = {-1,0,0, -1, 0, 1,1,0};
void dfs(int i, int k)
{
	group[i][k] = ng;
	int lv0, lv1, lv;
	int besti, bestk;
	besti = i;
	bestk = k;
	forn(lv,4){
		lv0 = i + dir[lv][0];
		lv1 = k + dir[lv][1];
		if ( mat[lv0][lv1] < mat[besti][bestk] ){
			besti = lv0;	bestk = lv1;
		}
	}

	if(besti == i && bestk == k){
		return;
	}

	int n1 = group[besti][bestk];
	if ( n1 == ng)return;
	if(n1 != 0){
		n1 = getparent(n1);
		if ( n1 < p[ng]){
			p[ng] = n1;
		}
	}else{
		dfs(besti, bestk);
	}
}

int main()
{
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int i, k, lv, ti, t;
	
	ti = 0;
	scanf("%d", &t);
	forn(ti,t){
		input();
		memset(group,0,(sizeof group));
		ng = 0;
		int nn = I*K+I;
		forn(i,nn){
			p[i] = i;
		}
		for(i=1; i<=I; i++){
			for(k=1; k<=K; k++)if(group[i][k] == 0){
				ng++;
//				cout << p[ng] << endl;
				dfs(i,k);
				int lv0,lv1;
//				for(lv0=1; lv0<=I; lv0++,cerr<<endl)for(lv1=1; lv1<=K; lv1++)cout<<(int)group[lv0][lv1]<<' '; 
//				cout << p[ng] << endl;
			}
		}

		int ch = 'a';
		for(i=1; i< nn; i++)if(p[i] == i)no[i] = ch++;

		printf("Case #%d:\n", ti+1);
		for(i=1; i<=I; i++){
			for(k=1; k<=K; k++){
				if(k!=1)putchar(' ');
				putchar(no[p[group[i][k]]]);
				if ( !isalpha((char)no[p[group[i][k]]])){
					cerr << "fsadfsa";
				}
			}
			puts("");
		}
		
	}
	return 0;
}
