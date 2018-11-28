#include<iostream>
#include<cstring>
using namespace std;


void solve(int T){
	cout<<"Case #"<<T<<": ";

	int M,V;
	cin>>M>>V;

	int inters[10240]={0};
	int interc[10240]={0};
	for(int i=1;i<=(M-1)/2;i++){
		cin>>inters[i];
		cin>>interc[i];
	}
	for(int i=(M-1)/2+1;i<=M;i++)
		cin>>inters[i];

	int dp[10240][2];
	memset(dp,0x2f,sizeof(dp));

	for(int i=(M-1)/2+1;i<=M;i++){
		dp[i][inters[i]]=0;
	}

	for(int i=(M-1)/2;i>=1;i--){
		if(inters[i]==0){ // OR gate
			dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][0]);

			dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][0]);
			dp[i][1]=min(dp[i][1],dp[i*2][0]+dp[i*2+1][1]);
			dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][1]);

			if(interc[i]){
				dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][0]+1);
				dp[i][0]=min(dp[i][0],dp[i*2][1]+dp[i*2+1][0]+1);
				dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][1]+1);

				dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][1]+1);
			}
		}
		else{ // AND gate
			dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][0]);
			dp[i][0]=min(dp[i][0],dp[i*2][1]+dp[i*2+1][0]);
			dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][1]);

			dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][1]);

			if(interc[i]){
				//cout<<"I"<<i<<endl;
				dp[i][0]=min(dp[i][0],dp[i*2][0]+dp[i*2+1][0]+1);

				dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][0]+1);
				dp[i][1]=min(dp[i][1],dp[i*2][0]+dp[i*2+1][1]+1);
				//cout<<dp[i][1]<<" "<<dp[i*2][0]<<" "<<dp[i*2+1][1]<<endl;
				dp[i][1]=min(dp[i][1],dp[i*2][1]+dp[i*2+1][1]+1);
			}
		}
	}

	if(dp[1][V]>20000)cout<<"IMPOSSIBLE\n";
	else cout<<dp[1][V]<<endl;
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int N;
	cin>>N;
	for(int i=1;i<=N;i++)
		solve(i);
}