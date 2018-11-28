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
int tab[20];
char S[100000];
int n;

int check(){
	int ret = 1;
	FOR(i,0,n-1) if(S[i]!=S[i+1]) ret++;
	return ret;
}
int main(){
	int T;
	cin>>T;
	FORE(t,1,T){
		int k;
		cin>>k;
		string s;
		cin>>s;
		n = s.size();
		FOR(i,0,k) tab[i]=i;
		int best = INF;
		do{
			for(int i = 0;i<n;i+=k){
				for(int j = 0;j<k;j++){
					S[i+j] = s[i+tab[j]];
				}
			}
			int a = check();
			if(a<best) best = a;
		
		}while(next_permutation(tab,tab+k));
		printf("Case #%d: %d\n",t,best);
	}



}
