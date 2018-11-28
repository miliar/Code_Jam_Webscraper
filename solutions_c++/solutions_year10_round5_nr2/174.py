#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		long long l;
		int n;
		vector<int> a;
		int dp[100000],cost[100000];
		cin>>l>>n;
		for(int i=0;i<n;i++){
			int aa;
			cin>>aa;
			a.push_back(aa);
		}
		sort(a.begin(),a.end());
		int g=l%a[n-1];
//		cout<<l<<" "<<n<<" "<<a[0]<<" "<<a[1]<<" "<<a[2]<<" "<<g<<endl;
		for(int i=0;i<100000;i++)dp[i]=10000001;
		dp[0]=0;
		for(int i=n-2;i>=0;i--){
//			cout<<a[i]<<endl;
			for(int j=0;j<a[n-1];j++){
				for(int k=0;k<a[n-1];k++){
					int end=j+k*a[i];
					int to=end%a[n-1];
					int cost=dp[j]+k-(end-j)/a[n-1];
					if(to<j)cost--;
					if(dp[to]>cost)dp[to]=cost;
				}
			}
//			for(int j=0;j<a[n-1];j++)
//				cout<<"("<<a[i]<<","<<j<<")="<<dp[j]<<endl;
		}
//		cout<<dp[g]<<endl;
		cout<<"Case #"<<tt<<": ";
		if(dp[g]>=10000001)cout<<"IMPOSSIBLE"<<endl;
		else{
			long long ans=(l-g)/a[n-1]+dp[g];
			cout<<ans<<endl;
		}
	}
	return 0;
}