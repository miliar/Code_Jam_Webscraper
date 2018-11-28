#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
int Xmax[1000000];
int Xmin[1000000];
int Ymax[1000000];
int Ymin[1000000];
int kier[][2] = {{0,1},{1,0},{0,-1},{-1,0}};
char cykl[100];

void popraw(int x,int y){
	if(Xmax[y]<x) Xmax[y] = x;
	if(Xmin[y]>x) Xmin[y] = x;
	if(Ymax[x]<y) Ymax[x] = y;
	if(Ymin[x]>y) Ymin[x] = y;
}

int main(){
	int T;
	scanf("%d",&T);
	FORE(t,1,T){
		int L,x=6000,y=6000,k = 0;
		int pole = 0;
		scanf("%d",&L);
		for(int i=0;i<1000000;i++){
			Xmax[i] = Ymax[i] = -1;
			Xmin[i] = Ymin[i] = 1000000;
		}
		FOR(i,0,L){
			char c;
			int ile;
			while(true){
				c = getchar();
				if(c=='F' || c == 'L' || c == 'R') break;
			}
			cykl[0]=c;
			ile = 1;
			while(true){
				c = getchar();
				if(c!='F' && c != 'L' && c != 'R') break;
				cykl[ile++]=c;
			}
			int d;
			scanf("%d",&d);
			FOR(i,0,d){
				FOR(j,0,ile){
					c = cykl[j];
					if(c=='F'){
						if(k==1) pole+=y/2;
						if(k==3) pole-=y/2;
						x+= kier[k][0];
						y+= kier[k][1];
						popraw(x,y);
						x+= kier[k][0];
						y+= kier[k][1];
						popraw(x,y);
					}
					else if(c=='R'){
						k=(k+1)%4;
					}
					else k--;			
					if(k==-1) k = 3;
				}
			}
		}
		int ret = 0;
		if(pole<0) pole = -pole;
		for(int i=1;i<=12000;i+=2){

			for(int j=1;j<=12000;j+=2){
			if( (i>=Xmin[j] && i<=Xmax[j]) || (j>=Ymin[i] && j<=Ymax[i]) ){

				ret++;
			}
			}

		}
		printf("Case #%d: %d\n",t,ret-pole);
		
	}
}
