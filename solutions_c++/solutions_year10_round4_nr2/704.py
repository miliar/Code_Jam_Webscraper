#include<iostream>
#include<cstdio>
using namespace std;
const int N=11;
const int M=1<<N;
const int inf=1000000000;
int n,a[M],f[M*2][N],g[M*2];
void getg(int node,int l,int r,int now,int goal){
	if (goal==now)
		cin>>g[node];
	if (r-l!=1){
		int m=(l+r)/2;
		getg(node*2,l,m,now-1,goal);
		getg(node*2+1,m+1,r,now-1,goal);
	}
}
void getf(int node,int l,int r){
	for (int i=0;i<=n;i++)
		f[node][i]=inf;
	if (r-l==1){
		int k=a[l];
		if (k<a[r])
			k=a[r];
		for (int i=k;i<=n;i++)
			f[node][i]=0;
		if (k)
			f[node][k-1]=g[node];
	}else{
		int m=(l+r)/2;
		getf(node*2,l,m);
		getf(node*2+1,m+1,r);
		for (int i=0;i<=n;i++)
			for (int j=0;j<=n;j++){
				int k=i;
				if (i<j)
					k=j;
				if (f[node][k]>f[node*2][i]+f[node*2+1][j])
					f[node][k]=f[node*2][i]+f[node*2+1][j];
			}
		for (int i=0;i<=n;i++)
			if (f[node][i]>f[node][i+1]+g[node])
				f[node][i]=f[node][i+1]+g[node];
	}
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cin>>n;
		for (int i=0;i<1<<n;i++){
			cin>>a[i];
			a[i]=n-a[i];
		}
		for (int i=0;i<n;i++)
			getg(1,0,(1<<n)-1,n-1,i);
		getf(1,0,(1<<n)-1);
		cout<<"Case #"<<t<<": "<<f[1][0]<<endl;
	}
	return 0;
}
