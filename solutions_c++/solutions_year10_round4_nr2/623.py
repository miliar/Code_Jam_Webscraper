#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int i,j,k,l,n,ri,repeat,p,m[3000],v[3000],u[3000],d;

void dfs(int m,int d){
	int n=0;
	if(m==1){
		if(d==0){
			u[m]=1;
		}
		return;
	}
	if(d>0)n=d-1;
	dfs(m/2,n);
	if(d==0){
			u[m]=1;
	}
	return;
}
	
int main(){
	freopen("B-small-attempt0.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d",&repeat);
	for(ri=1;ri<=repeat;ri++){
		printf("Case #%d: ",ri);
		scanf("%d",&p);
		memset(u,0,sizeof(u));
		l=1<<p;
		for(i=l;i<l+l;i++)
			scanf("%d",&m[i]);
		for(i=1;i<=p;i++){
			l=1<<(p-i);
			for(j=l;j<l+l;j++){
				scanf("%d",&v[j]);
			}
		}
		l=1<<p;
		for(i=l;i<l+l;i++){
			dfs(i/2,m[i]);
		}
		int t=0;
		for(i=1;i<l;i++){
			t+=u[i];
		}
		printf("%d\n",t);	
	}
}
