#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>

using namespace std;

int init;
int a[1001][1001];
int b[1001];
int c[1001];
int diamond = 0;


void search(int v){
	c[v] = init;
	int i;
	for(i=0;i<b[v];i++){
		if(c[a[v][i]] == init){
			diamond=1;
			return ;
		}
		else 
			search(a[v][i]);
	}
	return;
}
int main(){
	int T,m;
	scanf("%d",&T);
	for(m=1;m<=T;m++){

		int i, j, k, n, x, l;
		diamond = 0;
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%d",&x);
			b[i] = x;
			for(j=0;j<x;j++){
				scanf("%d",&l);
				a[i][j] = l;
			}
		}
		memset(c, 0, sizeof(c));
		for(i=1;i<=n;i++){
			init = i;
			search(i);
		}
		printf("Case #%d: ",m);
		if(diamond)
			printf("Yes\n");
		else 
			printf("No\n");


	}


	return 0;
}


