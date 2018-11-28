#include <iostream>
#include <map>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;


int s,p;
int dp[200][5];
int mark[500];
bool bi[500];

void calc(int b,int i){
	int a;
	for(a=0;a<=10;a++){
		if(3*a==b){ 
			dp[i][2]++;
			if(a>=p) dp[i][3]++; 
		}
		if(3*a-1==b && a-1>=0) { 
			dp[i][2]++;
			if(a>=p) dp[i][3]++;
		}
		if(3*a-2==b){  
			if(a-1>=0){ 
				dp[i][2]++; if(a>=p) dp[i][3]++;
			}
			if(a-2>=0){ 
				dp[i][0]++; if(a>=p) dp[i][1]++; 
			}
		}
		if(3*a-3==b && a-2>=0){ 
			dp[i][0]++; if(a>=p) dp[i][1]++;
		}
		if(3*a-4==b && a-2>=0){ 
			dp[i][0]++; if(a>=p) dp[i][1]++; 
		}
	}
}


int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int a,b,c,d,e,n,t,ti,ans,sp,up,un,k;
	cin>>t;
	for(int cr=1;cr<=t;cr++){
		cin>>n>>s>>p;
		ti=0; sp=0; up=0;
		ans=0; c=0; un=0; 
		k=0;
		for(a=0;a<=100;a++){ mark[a]=0; bi[a]=0; }
		for(a=0;a<n;a++){
			cin>>b;
			dp[a][0]=0; dp[a][1]=0; dp[a][2]=0; dp[a][3]=0;
			calc(b,a);
		}
		//for(a=0;a<n;a++) cout<<dp[a][0]<<","<<dp[a][1]<<" "<<dp[a][2]<<","<<dp[a][3]<<endl;
		bi[0]=1;
		for(a=0;a<n;a++){
			for(b=n;b>=0;b--){
				if(bi[b]){
					if(dp[a][0]>0 && dp[a][1]>0){ bi[b+1]=1; mark[b+1]=max(mark[b+1],mark[b]+1); }
					if(dp[a][0]>0 && dp[a][1]==0){ bi[b+1]=1; mark[b+1]=max(mark[b+1],mark[b]); }
					if(dp[a][2]>0 && dp[a][3]>0){ bi[b]=1; mark[b]=max(mark[b]+1,mark[b]); }
					//if(dp[a][2]>0 && dp[a][3]==0){ bi[b]=1; mark[b]=max(mark[b],mark[b]); }
				}
			}
			//for(b=0;b<=n;b++) if(bi[b]) cout<<b<<" "<<mark[b]<<endl;
		}
		cout<<"Case #"<<cr<<": "<<mark[s]<<endl;
	}
	return 0;
}
	
