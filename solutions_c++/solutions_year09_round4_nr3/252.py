#include <stdio.h>
#include <string.h>

#define MAX 110

/** Igor's code; 
 *   ////////////////////////
 *   // BIPARTITE MATCHING //
 *   ////////////////////////
 *
 * This file is part of my library of algorithms found here:
 *      http://www.palmcommander.com:8081/tools/
 * LICENSE:
 *      http://www.palmcommander.com:8081/tools/LICENSE.html
 * Copyright (c) 2003
 * Contact author:
 *      igor at cs.ubc.ca
 **/
 
int graph[MAX][MAX];
bool seen[MAX];
int matchL[MAX], matchR[MAX];
int nleftbpm, nrightbpm;

bool bpm( int u ){
	for( int v = 0; v < nrightbpm; v++ ) if( graph[u][v] ){
		if( seen[v] )
			continue;
		seen[v] = true;
		if( matchR[v] < 0 || bpm( matchR[v] ) ){
			matchL[u] = v;
			matchR[v] = u;
			return true;
		}
	}
	return false;
}
int bpm_main(){
	memset( matchL, -1, sizeof( matchL ) );
	memset( matchR, -1, sizeof( matchR ) );
	static int cnt,i;
	for(cnt = i = 0; i < nleftbpm; i++ ){
		memset( seen, 0, sizeof( seen ) );
		if( bpm( i ) )
			cnt++;
	}
	return cnt;
}
/***end igor***/

int v[110][30];

int main(){
	int t,u,n,k,i,j,p;
	scanf("%d",&t);
	for (u=0; u<t; u++){
		scanf("%d%d",&n,&k);
		for (i=0; i<n; i++) {
			for (j=0; j<n; j++)
				graph[i][j]=0;
			for (j=0; j<k; j++){
				scanf("%d",&v[i][j]);
			}
		}
		nleftbpm=nrightbpm=n;
		for (i=0; i<n; i++){
			for (j=i+1; j<n; j++){
				for (p=0; p<k && v[i][p]<v[j][p]; p++);
				if (p==k) graph[i][j]=1;
				else{
					for (p=0; p<k && v[i][p]>v[j][p]; p++);
					if (p==k) graph[j][i]=1;
				}
			}
		}
		printf("Case #%d: %d\n",u+1,n-bpm_main());
	}
	return 0;
}
