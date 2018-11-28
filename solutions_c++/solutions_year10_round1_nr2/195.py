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
int a[110];
int f[110][260];
int dele,adds;

int abss(int x){
	if (x<0)return -x;
	else return x;
}
int infinite;

int calc(int x,int y){
	if (x==256) return 0;
	
	x=abss(y-x);
	y = x/m;
	if (y*m<x) y++;
	if (y<=0) return 0;
	else return (y-1)*adds;
}
int main(){
   freopen("B-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,cases;
   scanf("%d",&test);
   cases=0;
   while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d%d%d%d",&dele,&adds,&m,&n);
		foru(i,1,n) {scanf("%d",&a[i]); }

//		continue;
		memset(f,60,sizeof(f));

		f[1][256] = 0;
		infinite=f[0][0];
//		rep(i,256) {
//			f[1][i] = abss(a[1]-i);
//		}
		bool flag;
		
//		printf("%d %d\n",adds,dele);
		foru(i,1,n)
		  rep(j,257) if (f[i][j]!=infinite){
			if (abss(j-a[i])<=m || j==256) flag=true;
			else flag=false;
			if (flag) f[i+1][a[i]] = min(f[i+1][a[i]], f[i][j]);
			f[i+1][j] = min(f[i+1][j] , f[i][j]+dele);
			
			
			rep(k,256) {
				if (m==0) {
					if (j!=k && j!=256) continue;
                    f[i+1][k] = min(f[i+1][k] , f[i][j] + abss(a[i]-k));
				}
				else
				f[i+1][k] = min(f[i+1][k] , f[i][j] + abss(a[i]-k) + calc(j,k));
			}
//			printf(":%d\n",f[i][125]);
		 }
		 int ans=infinite;
		 rep(j,257) ans=min(ans,f[n+1][j]);
		 printf("%d\n",ans);
	}
   
   return 0;
}
