#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>


int map[102][102],d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char s[102][102],good[102][102];
int to[102][102][2];
int r,c;
bool islink(int r1,int c1,int r2,int c2){
	//printf("45");
	if(to[r1][c1][0]==r2&&to[r1][c1][1]==c2)return true;
	if(to[r2][c2][0]==r1&&to[r2][c2][1]==c1)return true;
	//printf("45\n");
	return false;
}
void solve(int rr,int cc,char out){
	//printf("%d %d\n",rr,cc);
	good[rr][cc]=out;
	for(int k=0;k<4;k++){
		if(rr+d[k][0]>=0&&rr+d[k][0]<r&&cc+d[k][1]>=0&&cc+d[k][1]<c&&islink(rr,cc,rr+d[k][0],cc+d[k][1])&&!good[rr+d[k][0]][cc+d[k][1]]){
			//printf("ok\n");
			solve(rr+d[k][0],cc+d[k][1],out);
		}
	}
}
int main(){
	int t,no=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&r,&c);
		int max=-1;
		memset(good,0,sizeof(good));

		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				scanf("%d",&map[i][j]);

			}
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				int min=1000000;
				int ind=-1,all=0,equal=0;
				for(int k=0;k<4;k++){
					if(i+d[k][0]>=0&&i+d[k][0]<r&&j+d[k][1]>=0&&j+d[k][1]<c){
						all++;
						if(map[i][j]==map[i+d[k][0]][j+d[k][1]])equal++;
						if(map[i+d[k][0]][j+d[k][1]]<min&&map[i+d[k][0]][j+d[k][1]]<map[i][j]){
							min=map[i+d[k][0]][j+d[k][1]];
							ind=k;
						}
					}
				}
				if(all==equal||ind==-1){
					to[i][j][0]=-2;
					to[i][j][1]=-2;
				}
				else {
					to[i][j][0]=i+d[ind][0];
					to[i][j][1]=j+d[ind][1];
				}
			}
		}
		char out='a';
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(good[i][j])continue;
				solve(i,j,out);
				out++;
			}
		}
		printf("Case #%d:\n",no++);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){//
				//printf("(%d,%d) ",to[i][j][0],to[i][j][1]);
				if(j==0)printf("%c",good[i][j]);
				else printf(" %c",good[i][j]);
			}printf("\n");
		}
	}
				
					
	return 0;
}

