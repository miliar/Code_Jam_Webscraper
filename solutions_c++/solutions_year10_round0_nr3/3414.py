#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int T,n,r,k;
int g[1001];
int sum[1001],num[1001];
int main(){
	freopen("readme.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for (int t=0;t<T;t++){
		long long ans=0;
		cin>>r>>k>>n;
		for (int i=0;i<n;i++){
			cin>>g[i];
			sum[i]=0;
		}
		for (int i=0;i<n;i++){
			int j=i;
			while(sum[i]+g[j]<=k){
				sum[i]+=g[j];
				j++;
				if (j==n) j=0;
				if (j==i) break;
			}
			num[i]=j;
		}
		int start=0;
		for (int i=0;i<r;i++){
			ans+=(long long)sum[start];
			start=num[start];
		}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}