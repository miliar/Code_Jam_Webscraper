#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
const int maxn=1001;
const int oo=(1<<25);
int s,q,z;
int f[maxn][maxn];
int a[maxn];
map<string,int> mp;

void init(){
	mp.clear();
	z=0;
	scanf("%d",&s);
	char nouse[10];
	gets(nouse);
	for (int i=1;i<=s;i++){
		char cur[maxn];
		gets(cur);
		string str=cur;
		if (mp.find(str)==mp.end()){
			z++;
			mp[str]=z;
		}
	}
	scanf("%d",&q);
	gets(nouse);
	for (int i=1;i<=q;i++){
		char cur[maxn];
		gets(cur);
		string str=cur;
		a[i]=mp[str];
	}
	return;
}

int dp(){
	memset(f,0,sizeof(f));
	for (int i=1;i<=q;i++){
		for (int j=1;j<=s;j++){
			if (a[i]==j){
				f[i][j]=oo;
				continue;
			}
			f[i][j]=f[i-1][j];
			for (int k=1;k<=s;k++){
				if (k==j){
					continue;
				}
				f[i][j]=min(f[i][j],f[i-1][k]+1);
			}
		}
	}
	int ans=oo;
	for (int i=1;i<=s;i++){
		ans=min(ans,f[q][i]);
	}
	return ans;
}

int main(){
	//freopen("in.txt","r",stdin);
	int t;
	int cse=0;
	for (scanf("%d",&t);t>=1;t--){
		init();
		cse++;
		printf("Case #%d: %d\n",cse,dp());
	}
	return 0;
}
