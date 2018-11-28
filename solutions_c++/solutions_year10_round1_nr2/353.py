#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T,n,a[101],m,del,ins;
int f[101][256];
int low(int x){
	if (x<0) return 0;
	if (m==0) return 100000000;
	if (x%m==0) return x/m;
	return x/m+1;
}
void input(){
	cin>>del>>ins>>m>>n;
	for (int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
}
void solve(){
	for (int i=0;i<256;i++){
		if (i!=a[0])
			f[0][i]=del+ins;
	}
	for (int i=0;i<256;i++){
		f[0][i]=min(f[0][i],abs(i-a[0]));
		if (abs(i-a[0])<=m){
			f[0][i]=min(f[0][i],ins);
		}
	}
	for (int i=1;i<n;i++){
		for (int j=0;j<256;j++){
			f[i][j]=f[i-1][j]+del;
			for (int k=0;k<256;k++){
				if (k!=j && m==0) continue;
				f[i][j]=min(f[i][j],f[i-1][k]+del+ins*(low(abs(j-k)-m)+1));
			}
			for (int k=0;k<256;k++){
				if (k!=j && m==0) continue;
				f[i][j]=min(f[i][j],f[i-1][k]+abs(j-a[i])+ins*(low(abs(j-k)-m)));
			}
		}
	}
}
int main(){
	freopen("readme.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for (int t=1;t<=T;t++){
		input();
		solve();
		int gmin=2000000000;
		for (int i=0;i<256;i++){
			gmin=min(gmin,f[n-1][i]);
		}
		cout<<"Case #"<<t<<": ";
		cout<<gmin<<endl;
		for (int i=0;i<n;i++){
			for (int j=0;j<256;j++){
				f[i][j]=0;
			}
		}
	}
	return 0;
}