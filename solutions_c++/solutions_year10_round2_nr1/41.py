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

char W[1000];
set<string> S;

int main(){
	int T;scanf("%d\n",&T);
	FORE(test,1,T){
		int n,m;
		scanf("%d%d\n",&n,&m);
		S.clear();
		FOR(i,0,n){
			scanf("%s",W);
			string s;
			FOR(j,1,1000){
				if(W[j]=='/'){
					if(S.find(s)==S.end()) S.insert(s);
					s+=W[j];
				}
				else if(W[j]==' ' || W[j]=='\n' || W[j]==0){
					if(S.find(s)==S.end()) S.insert(s);
					break;				
				}
				else s+=W[j];
			}
		}
		int ret = 0;
		FOR(i,0,m){
			scanf("%s",W);
			string s;
			FOR(j,1,1000){
				if(W[j]=='/'){
					if(S.find(s)==S.end()){
						S.insert(s);
						ret++;
					}
					s+=W[j];
				}
				else if(W[j]==' ' || W[j]=='\n' || W[j]==0){
					if(S.find(s)==S.end()){
						S.insert(s);
						ret++;
					}
					break;				
				}
				else s+=W[j];
			}
		}	
		printf("Case #%d: %d\n",test,ret);	
	}

}
