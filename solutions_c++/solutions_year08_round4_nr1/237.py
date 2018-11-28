#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn=10100;
int m,v,s[maxn],c[maxn],f[maxn][2];

void init(){
	int i;
	scanf("%d %d",&m,&v);
	for (i=1;i<=(m-1)/2;i++)
		scanf("%d%d",&s[i],&c[i]);		
	for (i=(m-1)/2+1;i<=m;i++)
		scanf("%d",&s[i]);	
	return;
}

void update(int &a,int x){
	if (x!=-1&&(a==-1||a>x))
		a=x;	
	return;
}

int min(int a,int b){
	if (a==-1) return b;else
	if (b==-1) return a;else	
	if (a<b) return a;else return b;
}


void work(){
	int i;
	memset(f,0xff,sizeof(f));	
	for (i=m;i>(m-1)/2;i--)
		f[i][s[i]]=0;
	for (i=(m-1)/2;i>=1;i--){
		if (s[i]==0){
			if (f[i*2][1]!=-1 || f[i*2+1][1]!=-1) {
				if (f[i*2][1]!=-1)
					update(f[i][1],f[i*2][1]+min(f[i*2+1][0],f[i*2+1][1]));
				if (f[i*2+1][1]!=-1)
					update(f[i][1],f[i*2+1][1]+min(f[i*2][0],f[i*2][1]));
			}
			if (f[i*2][0]!=-1 && f[i*2+1][0]!=-1)
				update(f[i][0],f[i*2][0]+f[i*2+1][0]);
		} else {
			if (f[i*2][0]!=-1 || f[i*2+1][0]!=-1) {
				if (f[i*2][0]!=-1)
					update(f[i][0],f[i*2][0]+min(f[i*2+1][0],f[i*2+1][1]));
				if (f[i*2+1][0]!=-1)
					update(f[i][0],f[i*2+1][0]+min(f[i*2][0],f[i*2][1]));
			}
			if (f[i*2][1]!=-1 && f[i*2+1][1]!=-1)
				update(f[i][1],f[i*2][1]+f[i*2+1][1]);
		}
		if (c[i]==1){
			if (s[i]==1){
				if (f[i*2][1]!=-1 || f[i*2+1][1]!=-1) {
					if (f[i*2][1]!=-1)
						update(f[i][1],f[i*2][1]+min(f[i*2+1][0],f[i*2+1][1])+1);
					if (f[i*2+1][1]!=-1)
						update(f[i][1],f[i*2+1][1]+min(f[i*2][0],f[i*2][1])+1);
				}
				if (f[i*2][0]!=-1 && f[i*2+1][0]!=-1)
					update(f[i][0],f[i*2][0]+f[i*2+1][0]+1);
			} else {
				if (f[i*2][0]!=-1 || f[i*2+1][0]!=-1) {
					if (f[i*2][0]!=-1)
						update(f[i][0],f[i*2][0]+min(f[i*2+1][0],f[i*2+1][1])+1);
					if (f[i*2+1][0]!=-1)
						update(f[i][0],f[i*2+1][0]+min(f[i*2][0],f[i*2][1])+1);
				}
				if (f[i*2][1]!=-1 && f[i*2+1][1]!=-1)
					update(f[i][1],f[i*2][1]+f[i*2+1][1]+1);
			}			
				
		}
	}
	if (f[1][v]==-1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n",f[1][v]);
	return;
}

int main(){
	int t;
	scanf("%d",&t);
	for (int cse=1;cse<=t;cse++){
		printf("Case #%d: ",cse);
		init();
		work();
	}
	return 0;
}
