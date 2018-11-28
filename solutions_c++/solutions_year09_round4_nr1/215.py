#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int a[50],n,ans;


int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>n;
		for(int i=0;i<n;i++) {
			a[i]=0;
			char ch;
			for(int j=0;j<n;j++) {
				cin>>ch;
				if (ch!='0') a[i]=j;
			}
		}
		ans=0;
		for(int i=0;i<n;i++) {
			for(int j=i;j<n;j++) if (a[j]<=i) {
				for(int k=j-1;k>=i;k--) {
					int t=a[k+1]; a[k+1]=a[k]; a[k]=t;
					ans++;
				}
				break;
			}
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
