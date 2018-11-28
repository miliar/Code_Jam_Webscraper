#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
#define maxn 1010
int sc, nsc;
int k, R;
int mas[maxn];
int n;
bool was[maxn];
int next[maxn];
long long sumcur[maxn];
void init(){
	scanf(" %d %d %d ", &R, &k, &n);
	for(int i=0; i<n; i++)
		scanf(" %d ", &mas[i]);
}
void solve(){
	memset(was, 0, sizeof(was));
	memset(sumcur, 0, sizeof(sumcur));
	int cur=0;
	int len=0;
	long long sum=0;
	long long sump=0;
	int tmpR=R;
	for(int i=0; i<n; i++)
		sump+=mas[i];
	if (sump<=k){
		printf("Case #%d: %lld\n", sc, sump*R);
		return;
	}
	while (!was[cur]){
		was[cur]=true;
		len++;
		if (len>R){
			printf("Case #%d: %lld\n", sc, sum);
			return;
		}
		int cap=k;
		int tmpcur=cur;
		while (cap>=mas[tmpcur]){
			cap-=mas[tmpcur];
			sum+=mas[tmpcur];
			sumcur[cur]+=mas[tmpcur];
			tmpcur=(tmpcur+1)%n;
		}
		next[cur]=tmpcur;
		cur=tmpcur;

	}
	R-=len;
	long long sumcyc=0;
	memset(was, 0, sizeof(was));
	len=0;
	while (!was[cur]){
		was[cur]=true;
		len++;
		sumcyc+=sumcur[cur];
		cur=next[cur];
	}
	sum+=(R/len)*sumcyc;
	R%=len;

	while (R>0){
		R--;
		sum+=sumcur[cur];
		cur=next[cur];
	}
	printf("Case #%d: %lld\n", sc, sum);


	//cur=0;
	//int sum2=0;
	//for(int i=1; i<=tmpR; i++){
	//	int cap=k;
	//	while (cap>=mas[cur]){
	//		cap-=mas[cur];
	//		sum2+=mas[cur];
	//		cur=(cur+1)%n;
	//	}
	//}
	//if (sum2!=sum){
	//	cur=cur;
	//}
	
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}