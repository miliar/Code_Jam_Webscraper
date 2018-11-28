#include <stdio.h>
#include <vector>
#include <deque>
#include <algorithm>
#include <map>
#include <string>
//#include "bnum.h"
using namespace std;
#define MP make_pair
#define FS first
#define SD second
#define PI pair<int,int>
#define VI vector<int>
#define INF 1000000000

typedef long long LL;
typedef long long bnum;

bnum ile[3][3];
int t;

int main() {
	scanf("%d",&t);
	int id=1;
	while(t--) {
		for(int i=0;i<3;i++) for(int i2=0;i2<3;i2++) ile[i][i2]=0;
		LL n,a,b,c,d,x0,y0,M;
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&a,&b,&c,&d,&x0,&y0,&M);
		LL X=x0,Y=y0;
		for(int i=0;i<n;i++) {
			ile[X%3][Y%3]=ile[X%3][Y%3]+1;
			X = (a * X + b) % M;
			Y = (c * Y + d) % M;
		}
		//printf("wysz");fflush(stdout);
		bnum wyn=0;
		 //wyn.czysc();
	     //wyn.dl=1;
	     //wyn.w[0]=0;
	     //wyn.wyrownaj(0);
		 
		for(int x1=0;x1<3;x1++)for(int y1=0;y1<3;y1++) {
			if(ile[x1][y1]>2) {
				bnum nos=(ile[x1][y1]-2)*(ile[x1][y1]-1)*ile[x1][y1]/6;
				wyn=wyn+nos;
			}
		}
		//printf("%I64d\n",wyn);
		
		for(int x1=0;x1<3;x1++)for(int y1=0;y1<3;y1++)
		for(int x2=0;x2<3;x2++)for(int y2=0;y2<3;y2++) {
			if(ile[x1][y1]>1) {
			if((x1!=x2||y1!=y2)&&(x1+x1+x2)%3==0&&(y1+y1+y2)%3==0) {
				bnum nos=(ile[x2][y2])*(ile[x1][y1]-1)*ile[x1][y1]/2;
				wyn=wyn+nos;
			}
			}
		}
		bnum wynik=0;
		for(int x1=0;x1<3;x1++)for(int y1=0;y1<3;y1++)
		for(int x2=0;x2<3;x2++)for(int y2=0;y2<3;y2++) 
		for(int x3=0;x3<3;x3++)for(int y3=0;y3<3;y3++) {
			if((x1!=x2||y1!=y2)&&(x1!=x3||y1!=y3)&&(x2!=x3||y2!=y3)&&(x1+x2+x3)%3==0&&(y1+y2+y3)%3==0) {
				bnum nos=ile[x1][y1]*ile[x2][y2]*ile[x3][y3];
				wynik=wynik+nos;
				//if(nos) printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
			}
		}
		//printf("%I64d\n",wyn);
		printf("Case #%d: %I64d\n",id++,wynik/6+wyn);
		//wyn.wys();
	}
	
	return 0;
}
