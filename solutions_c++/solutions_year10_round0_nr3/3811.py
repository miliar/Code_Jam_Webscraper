#include<iostream>
using namespace std;
int main(){
	int t;
	int r,k,n;
	int g[10];
	int cas=1;
	cin>>t;
	while(t--){
		cin>>r>>k>>n;
		for(int i=0;i<n;i++){
			cin>>g[i];
		}
		int j=0,cost=0;
		for(int i=0;i<r;i++){
			int sum=0;
			int left=n;
			while(1){
				sum+=g[j%n];
				j++;
				left--;
				if(sum==k)
					break;
				else if(sum<k){
				if(left>0)
					continue;
				else 
					break;
				}
				else
				{	j--;sum-=g[j%n];break;	}
				
			}
			cost+=sum;
		}
		cout<<"Case #"<<cas<<": "<<cost<<"\n";
		cas++;
	}
	return 0;
}

