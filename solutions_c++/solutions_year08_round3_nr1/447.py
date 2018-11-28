#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	int N, a[1024];
	cin>>N;
	for(int t=1; t<=N; t++){
		int P, K, L;
		cin>>P>>K>>L;
		for(int i=0; i<L; i++) cin>>a[i];
		sort(a, a+L); reverse(a, a+L);
		int i=0, pr=1;
		long long ans=0;
		while(pr<=P&&i<L&&a[i]){
			for(int j=i;i-j<K&&i<L&&a[i]; i++) ans+=pr*a[i];
			pr++;
		}
		if(i<L&&a[i]!=0) cout<<"Case #"<<t<<": Impossible"<<endl;
		else cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}

