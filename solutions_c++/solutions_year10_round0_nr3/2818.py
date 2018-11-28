#include <iostream>
using namespace std;

int g[1005];

int main(){
	int t, r, k, n, j;
	int first;
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	cin>>t;
	for(int i=0; i<t; i++){
		cin>>r>>k>>n;

		for(j=0; j<n; j++) cin>>g[j];

		int sum=0, roll=g[0], times=0;
		first=0;
		if(n==1) j=0; else j=1;

		while(times<r){
			if(j!=first && roll+g[j]<=k){
				roll+=g[j];
			}
			else{
				sum+=roll;
				times++;
				roll=g[j];
				first=j;
			}

			if(j==n-1) j=0; else j++;
		}

		cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}


	return 0;
}