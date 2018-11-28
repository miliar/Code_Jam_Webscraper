#include<algorithm>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

int t;
int n;
int T[1100];
int P[1100];
int q[1100];

const bool cmp(const int&a,const int&b){
	return T[a]*(1-P[b])>T[b]*(1-P[a]) || 
		T[a]*(1-P[b])==T[b]*(1-P[a]) && a<b;
}

int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int h,i,j,k;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&T[i]);
		}
		for(i=0;i<n;i++){
			scanf("%d",&P[i]);
			q[i]=i;
		}
		sort(q,q+n,cmp);
		printf("Case #%d:",h);
		for(i=0;i<n;i++){
			printf(" %d",q[i]);
		}
		printf("\n");
	}
	return 0;
}