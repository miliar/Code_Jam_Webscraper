#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

int n;
long long l;
int a[111];
int d[111111];
int e[111111];
int mm;
bool v[111111];

void f(int x,int j) {
	int t=d[j];
	if (j+x<mm) t++;
	int u=(j+x)%mm;
	//cerr<<"x j u d[j] d[u]"<<x<<' '<<j<<' '<<u<<' '<<d[j]<<' '<<d[u]<<endl;
	if (d[u]<0 || d[u]>t) {
		d[u]=t;
	}
}
void f2(int x,int j) {
	int p=j;
	while(true) {
		f(x,j);
		j=(j+x)%mm;
		v[j]=false;
		if (j==p) return;
	}
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>l>>n;
		for(int i=0;i<n;i++) cin>>a[i];
		memset(d,-1,sizeof d);
		memset(e,-1,sizeof e);
		d[0]=0; e[0]=0;
		mm=0;
		for(int i=0;i<n;i++) mm=max(a[i],mm);
		int dest=l%mm;
		for(int i=0;i<n;i++) {
			memset(v,true, sizeof v);
			for(int j=0;j<mm;j++) if (d[j]>=0 && v[j]) {
				f2(a[i],j);
				f2(a[i],j);
			}
		}
		//cerr<<l<<mm<<d[dest]<<endl;
		long long ans=d[dest];
		cout<<"Case #"<<T<<": ";
		if (ans<0) cout<<"IMPOSSIBLE"<<endl;
		else {
			ans=ans+(l/mm);
			cout<<ans<<endl;
		}
		
	}
	return 0;
}
