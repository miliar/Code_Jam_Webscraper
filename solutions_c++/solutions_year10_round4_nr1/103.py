#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;
int a[310][310];
int start[310];
int len[310];
int ans;


bool check(int x1,int y1, int x2 , int y2){
	if (x1<0 || y1<0 || x2<0 || y2<0) return true;
	if (a[x1][y1]<0 || a[x2][y2]<0) return true;
	if (a[x1][y1]==a[x2][y2]) return true;
	return false;
}


bool centers(int x, int y) {
	int i,j,k;
	foru(i,1,2*n-1)
	  	foru(j,1,2*n-1) if (a[i][j]>=0)
	  	  if (!(check(i,j , 2*x - i , j) && check(i,j, i , 2*y - j)))
	  	    return false;
	return true;
}

int abss(int x){
	if (x<0) return -x;
	else return x;	
}
int find(int x, int y){
	int ans=0;
	int i,j;
	foru(i,1,2*n-1)
	  foru(j,1,2*n-1) if (a[i][j]>=0)
	    	ans = max(ans , abss(x-i) + abss(y-j));
	return ans+1;
	
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases=0;
	scanf("%d",&test);
	
	
	while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d",&n);
		memset(a,-1,sizeof(a));
		foru(i,1,n)  {
			j=n-i+1;
			len[i]=i;
			start[i]=j;
			foru(k,1,len[i]) {
				scanf("%d",&a[i][j]);	
				j+=2;
			}	
		}
		 
		foru(i,n+1,2*n-1)  {
		   j=i-n + 1;
		   len[i]=2*n-i;
		   start[i]=j;
		   foru(k,1,len[i]) {
				scanf("%d",&a[i][j]);
				j+=2;
			}
		}

/*printf("\n");
		foru(i,1,2*n-1){
		  foru(j,1,2*n-1) printf("%d ",a[i][j]);
		  printf("\n");
		}
		printf("\n");
*/
		ans = 1000;
		foru(i,1,2*n-1)
		  foru(j,1,2*n-1) if (centers(i,j)){
				ans=min(ans , find(i,j));
			}
				
/*		int heng,shu;
		heng=min(tryup() , trydown());
		shu =min(tryleft() , tryright());
	//	printf("%d %d\n",heng,shu);
		ans = max(heng , shu);
*/	
	//	printf("%d %d\n",n,ans);
		n = (1+n)*n - n;
		ans = (1+ans)*ans - ans;
		
		printf("%d\n", ans - n   );
	}
	
	return 0;	
	
	
}
