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
#define MAX 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define MP make_pair
#define FS first
#define SD second


bool sito [1000100];
int primes[100000];
int lprime;
vector<int> pol[1000100];
bool byl[1000100];
int stos[1000100];
int lstos = 0;

void BFS(int v){
	byl[v]=true;
	lstos = 1;
	stos[0] = v;
	
	while(lstos!=0){
		int u = stos[--lstos];
		FOR(i,0,SZ(pol[u])){
			int w = pol[u][i];
			if(!byl[w]){
				byl[w]=true;
				stos[lstos++]=w;
			}
		}
	}

}

int main(){
	lprime = 0;
	FOR(i,0,1000000) sito[i] = true;
	FOR(i,2,1000000){
		if(!sito[i]) continue;
		primes[lprime++]=i;
		for(int j=i;j<1000000;j+=i) sito[j] = false;
	}

	int T;
	scanf("%d",&T);
	
	FORE(t,1,T){
		LL A,B,P;
		scanf("%lld%lld%lld",&A,&B,&P);
		FOR(i,0,1000100) pol[i].clear();
		
		FOR(i,0,lprime){
			LL p = primes[i];
			if(p<P) continue;
			LL start = (A/p)*p;
			if(A%p!=0) start+=p;
			LL ost = -1;
			while(start<=B){
				if(ost!=-1){
					pol[ost-A].push_back(start-A);
					pol[start-A].push_back(ost-A);
				}
				ost = start;
				start+=p;
			}
		}
		LL ile = B-A+1;
		FOR(i,0,ile) byl[i]=false;
		int ret = 0;
		FOR(i,0,ile){
			if(!byl[i]){
				BFS(i);
				ret++;
			}
		}
		printf("Case #%d: %d\n",t,ret);
	
	}

}
