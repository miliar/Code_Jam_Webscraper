#include <iostream>
#include <vector>
#include <algorithm>
//#include <cmath>

using namespace std;
typedef long long llong;

int n;
llong a,b;
llong nums[10000];
llong A[10001],B[10001];

llong gcd(llong a, llong b){
	if(!b) return a;
	return gcd(b,a%b);
}

int main(){

	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin>>n>>a>>b;
		for(int i=0;i<n;i++)
			cin>>nums[i];
		sort(nums, nums+n);

		int pos=0;
		llong ans=-1;
		for(llong k,i=a;i<=b;i++) {
			for(k=0;k<n;k++)
				if (nums[k]%i&&i%nums[k])
					break;
			if(k==n)
			{
				pos=1;
				ans=i;
				break;
			}
		}

		/*
		A[0]=1;
		for(int i=0;i<n;i++)
			A[i+1]=nums[i]/gcd(A[i],nums[i])*A[i];
		
		B[n]=nums[n-1];
		for(int i=n-1;i>=0;i--)
			B[i]=gcd(B[i+1],nums[i]);

		int pos=0;
		llong ans=-1;
		for(int i=0;i<=n&&!pos;i++){
			if(B[i]%A[i]==0){
				llong x=max(a,i>0?nums[i-1]:a);
				llong y=min(b,i<n?nums[i]:b);
				llong f=B[i]/A[i];
				llong sf=((llong)sqrt((double)f))+1;
				for(llong k=1;k<sf&&k*A[i]<=y;k++)
					if(f%k==0) {
						if(k*A[i]>=x&&k*A[i]<=y) {
							pos=1;
							ans=k*A[i];
						}
					}
				for(llong k=1;k<sf;k++)
					if(f%k==0) {
						if(f/k*A[i]>=x&&f/k*A[i]<=y) {
							pos=1;
							ans=f/k*A[i];
						}
					}

			}
		}
		*/
		cout<<"Case #"<<MM<<": ";
		if (pos)
			cout<<ans<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}