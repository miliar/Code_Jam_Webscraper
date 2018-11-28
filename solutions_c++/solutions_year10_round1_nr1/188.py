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
char s[60][60];
char a[60][60];
const int rule[4][2]={1,0, 0,1, 1,1, 1,-1};


bool check(int x, int y){
	int t,x1,y1,tot,i;
	
	rep(t,4) {
		tot=1;
		x1=x; y1=y;
		while (1){
			x1+=rule[t][0];
			y1+=rule[t][1];
			if (x1>=n || x1<0 ||y1>=n ||y1<0) break;
			if (a[x1][y1]!=a[x][y]) break;
			tot++;
		}
		if (tot>=m) return true;
	}
	return false;
}

int main(){
   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,cases;
   scanf("%d",&test);
   cases=0;
   while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d%d",&n,&m);
		rep(i,n) scanf("%s",s[i]);
		rep(j,n) ford(i,n-1,0) a[j][n-1-i]=s[i][j];
		
		//		rep(i,n){
		//	 rep(j,n) printf("%c",a[i][j]);
		//	 printf("\n");
		//	}
		
		int x,y;
		ford(i,n-2,0)
		  rep(j,n)if (a[i][j]!='.') {
			x=i; y=j;
			while (x!=n-1 && a[x+1][y]=='.')
				{ a[x+1][y]=a[x][y]; a[x][y]='.';
				  x++;
				}
		}
		
		
		
		bool flaga,flagb;
		flaga=flagb=false;
		rep(i,n)
		  rep(j,n) if (a[i][j]!='.') {
					if (check(i,j)) {
						if (a[i][j]=='R') flaga=true;
						if (a[i][j]=='B') flagb=true;
					}
			}

		if (flaga && flagb) printf("Both\n");else
		if (flaga) printf("Red\n");else
		if (flagb) printf("Blue\n");else
		printf("Neither\n");
	}
   
   return 0;
}
