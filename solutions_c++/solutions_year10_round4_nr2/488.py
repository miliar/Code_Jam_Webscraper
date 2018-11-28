#include<iostream>
#include<algorithm>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
using namespace std;

int in[1200],dp[12][1200];
int dp2[12][1200][12];
int dp3[12][1200][12];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("pb2.txt","w",stdout);
	
	int w,t,tt,i,j,k,ans,p,l,x,s;
	cin >> tt;
	for(t=1 ; t<=tt ; t++){
		cin >> p;
		w=1<<p;
		memset(dp2,0,sizeof(dp2));
		memset(dp3,0,sizeof(dp3));
		for(i=0 ; i<w ; i++){
			cin >> in[i];
	//		dp3[0][i][in[i]]=true;
			for(j=in[i] ; j>=0 ; j--){
				dp3[0][i][j]=true;
			}
		}
		w=1<<(p-1);
		for(i=1 ; i<=p ; i++){
			for(j=0 ; j<w ; j++){
				cin >> dp[i][j];
			}
			w/=2;
		}
		w=1<<(p-1);
//		for(i=0 ; i<w ; i++) cin >> in[i];
		for(i=1 ; i<=p ; i++,w/=2){
			for(j=0 ; j<w ; j++){
				for(k=1 ; k<=p ; k++){
					x=0x7FFFFFFF;
					if(dp3[i-1][j*2][k] && dp3[i-1][j*2+1][k]){
						x=min(dp2[i-1][j*2][k-1]+dp2[i-1][j*2+1][k-1]+dp[i][j],dp2[i-1][j*2][k]+dp2[i-1][j*2+1][k]);
					}
					else if(dp3[i-1][j*2][k-1] && dp3[i-1][j*2+1][k-1]) {
						x=dp2[i-1][j*2][k-1]+dp2[i-1][j*2+1][k-1]+dp[i][j];
					}
					if(x<0x7FFFFFFF){
						dp3[i][j][k]=true;
						dp2[i][j][k]=x;
					}
				}
			}
		}
		cout << "Case #" << t << ": " << dp2[p][0][p] << endl;
	}
}
