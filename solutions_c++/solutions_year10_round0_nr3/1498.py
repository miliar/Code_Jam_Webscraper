
#include <iostream>
using namespace std;


long long group[2000];
long long next[1000];
long long costs[1000];

int solve(int caseno)
{
	int r,k,n;

	cin>>r>>k>>n;

	for(int i=0;i<n;++i){
		cin>>group[i];
		group[n+i] = group[i];
	}

	for(int i=0;i<n;++i){
		long long sum = 0;
		int j;
		for(j=0;j<n;++j){
			if(sum+group[i+j]>k){
				break;
			}
			sum+=group[i+j];
		}
		if(j==0)
			next[i] = i+1;
		else
			next[i] = (i+j)%n;
		costs[i] = sum;
	}

	int start = 0;
	long long result = 0;
	for(int i=0;i<r;++i){
		result+=costs[start];
		start=next[start];	
	}

	cout<<"Case #"<<caseno<<": "<<result<<endl;
}

int main()
{
	int t ;
	cin>>t;
	for(int i=1;i<=t;++i){
		solve(i);
	}

	return 0;
}
