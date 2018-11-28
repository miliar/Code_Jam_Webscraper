#include<iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int k=1;k<=T;++k){
		int n;
		cin>>n;
		int a[n],b[n],sum=0;
		for(int i=0;i<n;++i)
			cin>>a[i]>>b[i];
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				if(a[i]>a[j] && b[i]<b[j] || a[i]<a[j] && b[i]>b[j] )
					++sum;
		printf("Case #%d: %d\n",k,sum);
	}
	return 0;
}
