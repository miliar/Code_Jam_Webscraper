#include<iostream>
#include<algorithm>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
#define swap(a,b) (www=a,a=b,b=www)
using namespace std;

int dp[502][502];

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("pc.txt","w",stdout);
	
	int t,tt,i,j,k,x1,x2,y1,y2,www,ans,ox,v;
	cin >> tt;
	for(t=1 ; t<=tt ; t++){
		memset(dp,0,sizeof(dp));
		cin >> v;
		for(k=0 ; k<v ; k++){
			cin >> x1 >> y1 >> x2 >> y2;
			if(x1>x2) swap(x1,x2);
			if(y1>y2) swap(y1,y2);
			for(i=x1 ; i<=x2 ; i++){
				for(j=y1 ; j<=y2 ; j++){
					dp[i][j]=true;
				}
			}
		}

		ox=true;
		for(ans=0 ; ox ; ans++){
			ox=false;
			for(i=300 ; i>0 ; i--){
				for(j=300 ; j>0 ; j--){
					if(dp[i-1][j] && dp[i][j-1]){
						 dp[i][j]=true;
						ox=true;
					}
					else if(dp[i][j] && (dp[i][j-1] || dp[i-1][j])){
						dp[i][j]=true;
						ox=true;
					}
					else dp[i][j]=false;
				}
			}
		}
		cout << "Case #"  << t << ": " << ans << endl;
	}
	
}
