#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;
#define N 10100
#define INF 100000

int num[N];
bool used[N];
int p, q;

int cost(int i,int q){
	int res=0;
	for(int j=num[i]-1;j>=1;j--){
		if(used[j])break;
		res++;
	}
	for(int j=num[i]+1;j<=p;j++){
		if(used[j])break;
		res++;
	}
	return res;
}
int rec(int tm, int q){
	if(tm>q)return 0;
	int res=INF, t;
	for(int i=0; i<q; i++){
		if(!used[num[i]]){
			used[num[i]]=1;
			t=rec(tm+1,q)+cost(i,q);
			if(t<res)res=t;
			used[num[i]]=0;
		}
	}
	return res;
}

int main(){
	int t;
	freopen("C-small.in","r",stdin); freopen("C-small.out", "w", stdout);
	//freopen("C-large.in","r",stdin); freopen("C-large.out", "w", stdout);
	
	scanf("%d", &t);
	for(int x=1;x<=t;x++){
		int  res=0;
		scanf("%d %d", &p, &q);
		for(int i=0;i<q;i++){
			scanf("%d", &num[i]);	
		}
		memset(used,0,sizeof(used));
		res=rec(1,q);
		printf("Case #%d: %d\n",x,res);
	}
	return 0;
}