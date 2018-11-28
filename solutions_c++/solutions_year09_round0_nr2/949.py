// B.Watersheds.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include"iostream"
using namespace std;
int map[101][101];
struct node
{
	bool hash;
	int no,x,y;
	int visite();
}w[101][101];
int usedcode,n,m;
int step[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int node::visite()
{
	if(hash)
		return no;
	else{
		int min = -1,minp = -1,xx,yy,i;
		hash = 1;
		for(i=0;i<4;i++){
			xx = x + step[i][0];
			yy = y + step[i][1];
			if(xx < 0 || xx >= n || yy < 0 || yy >= m || map[xx][yy] >= map[x][y])
				continue;
			if(minp == -1 || min > map[xx][yy]){
				minp = i;
				min = map[xx][yy];
			}
		}
		if(minp == -1)
			no = usedcode++;
		else{
			xx = x + step[minp][0];
			yy = y + step[minp][1];
			no = w[xx][yy].visite();
		}
		return no;
	}
}
bool hash[27];
int p[27];
int main()
{
	int t,i,j,num,ci = 1;
	freopen("G:\\\B-large.in","r",stdin);
		freopen("G:\\bout.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&m);
		usedcode = 0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++){
				w[i][j].x = i;
				w[i][j].y = j;
				w[i][j].hash=0;
				scanf("%d",&map[i][j]);
			}
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				w[i][j].visite();
		memset(hash,0,sizeof(hash));
		num = 0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(!hash[w[i][j].no]){
					hash[w[i][j].no] = 1;
					p[w[i][j].no] = num++;
				}
			}
		}
		printf("Case #%d:\n",ci++);
		for(i=0;i<n;printf("\n"),i++)
			for(j=0;j<m;j++)
				printf("%c ",p[w[i][j].no]+'a');
	}
	return 0;
}

		

				
		


			
