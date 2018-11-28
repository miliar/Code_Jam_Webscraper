#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define M 105
#define Max(a,b) a>b?a:b
int f[M];
int ans,maxn,n;
void dfs(int x,int boy,int girl ,int b,int g) {
    if(x>n) return;
	if(g>b) return;
    if(girl==boy&&g>0){
    	ans=Max(ans,b);
	}
	dfs(x+1,boy^f[x],girl^f[x],b-f[x],g+f[x]);
	dfs(x+1,boy,girl,b,g);
}

int main(){
	int boy,girl,i,j,cas,aa,b,g;
	freopen("C:\\Users\\lenovo\\Desktop\\C-small-attempt1.in","r",stdin);
	freopen("C:\\Users\\lenovo\\Desktop\\stdout.txt","w",stdout);
	scanf("%d",&cas);
	int cou=1;
	while(cas--&&scanf("%d",&n)){
		maxn=0;aa=0;
		for(i=0;i<n;i++){
			scanf("%d",&f[i]);
			maxn+=f[i];
			aa^=f[i];
		}		
		ans=girl=0;boy=aa;
		b=maxn;g=0;
		dfs(0,boy,girl,b,g);
		if(ans==0) printf("Case #%d: NO\n",cou++);
		else 
			printf("Case #%d: %d\n",cou++,ans);
	}
	return 0;
}
