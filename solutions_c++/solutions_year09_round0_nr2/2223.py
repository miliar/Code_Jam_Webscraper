#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n,m;
int a[200][200];
char ans[200][200];
char number;

const int rule[4][2]={
	-1 , 0, 0,-1, 0,1,1,0
};

void find(int sx, int sy, int &x , int &y){
	x=sx;
	y=sy;
	int x1,y1,t;
	int k,mins;
	while (1) {
		k=-1;
		mins=a[x][y];
	rep(t,4){
		x1=x+rule[t][0];
		y1=y+rule[t][1];
		if (x1<1 || x1>n || y1<1 || y1>m) continue;
		if (a[x1][y1] < mins) {
			mins=a[x1][y1];
			k=t;
		}
	}
		if (k>=0) {
			x+=rule[k][0];
			y+=rule[k][1];
		}
		else break;
	}
}

int main(){
   freopen("B-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,num;
   while (		scanf("%d\n",&num)==1){
		foru(test,1,num) {
			printf("Case #%d:\n",test);
			scanf("%d%d",&n,&m);
			foru(i,1,n) 
			  foru(j,1,m) scanf("%d",&a[i][j]);
			memset(ans,0,sizeof(ans));
			number='a';
			int x,y;
			foru(i,1,n) 
			 foru(j,1,m) {
					find(i,j,x,y);				  
					if (ans[x][y]==0) {
						ans[x][y]=number;
						number++;	
					}
					ans[i][j]=ans[x][y];
				}
			foru(i,1,n) {
				foru(j,1,m) if (j==m) printf("%c\n",ans[i][j]);
				else printf("%c ",ans[i][j]);	
			}
		}
	}
   
   return 0;
}
