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

int X[60];
int V[60];
bool ok[60];

int main(){
   int T;
   scanf("%d\n",&T);
   FORE(test,1,T){
 		int n,k,b,t;
 		scanf("%d%d%d%d",&n,&k,&b,&t);
		FOR(i,0,n) scanf("%d",&X[i]);
		FOR(i,0,n) scanf("%d",&V[i]);
		FOR(i,0,n) ok[i] = false;
		for(int i = n-1;i>=0;i--){
			if(k>0 && V[i]*t>=b-X[i]){
				k--;
				ok[i] = true;
			}
		}
		if(k>0) printf("Case #%d: IMPOSSIBLE\n",test);
		else{
			int ret = 0;
			FOR(i,0,n){
				if(ok[i]){
					FOR(j,i+1,n) if(!ok[j]) ret++;
				}
			}
			printf("Case #%d: %d\n",test,ret);
		}
   }

}
