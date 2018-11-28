#include <iostream>
#include <cstdio>
#include <string>
#include <stack>
#include <vector>

using namespace std;

int main () {
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0; t<T; t++) {
		int a=1,b=1,n=0,ans=0,freea=0,freeb=0;
		char s[200];
		int x[200];
		cin>>n;
		for (int i=0; i<n; i++) scanf ("%1s%d",&s[i],&x[i]);
		for (int i=0; i<n; i++) 
			if (s[i]=='O') {
				ans+=max(0,abs(x[i]-a)-freea)+1;
				freeb+=max(0,abs(x[i]-a)-freea)+1;
				freea=0;
				a=x[i];
			} else {
				ans+=max(0,abs(x[i]-b)-freeb)+1;
				freea+=max(0,abs(x[i]-b)-freeb)+1;
				freeb=0;
				b=x[i];
			}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
		
	}
}