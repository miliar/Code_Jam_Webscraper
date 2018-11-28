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


int n,m;

bool a[200][200];


int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases=0;
	scanf("%d",&test);
	while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		int x1,y1,x2,y2;
		foru(i,1,n) {
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);	
//			printf(
			foru(j,x1,x2)
			  foru(k,y1,y2)
			    a[k][j]=true;
		}
/*		foru(i,1,10){
		  foru(j,1,10) printf("%d",a[i][j]);
		  printf("\n");
		}
*/		int ans=0;
		bool flag;
		while (1){
			flag=false;
			ford(i,199,0)
			  ford(j,199,0) {
					if (!a[i][j]){
			
						if (a[i-1][j] && a[i][j-1]) a[i][j]=true;
						else a[i][j]=false;	
					}
					else {
						flag=true;
						if (!a[i-1][j] && !a[i][j-1]) a[i][j]=false;
						else a[i][j]=true;
					}
				}
			if (!flag) break;
			ans++;	
		}
		printf("%d\n",ans);
		
		
	}
	return 0;
}
