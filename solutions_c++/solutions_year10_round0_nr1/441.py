#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define FS first
#define SD second

int main(){
	int T;scanf("%d",&T);
	FORE(test,1,T){
		int n,k;
		scanf("%d%d",&n,&k);
		k++;
		int p = 1;
		FOR(i,0,n) p = p*2;
		if(k%p==0) printf("Case #%d: ON\n",test);
		else printf("Case #%d: OFF\n",test);
	}

}
