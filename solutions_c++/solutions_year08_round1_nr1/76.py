#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n;
long long a[1010],b[1010];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,t=0;
	cin >> Q;
	while (Q--){
		cin >> n;
		for (int i=0;i<n;i++) cin >> a[i];
		for (int i=0;i<n;i++) cin >> b[i];
		sort(a,a+n);
		sort(b,b+n);
		long long ans=0;
		for (int i=0;i<n;i++)
			ans=ans+(long long)a[i]*b[n-i-1];
		t++;
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}