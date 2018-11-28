#include<cstdio>
#include<iostream>
using namespace std;
const int N=1000;
int Test,test;
int a[N],f[N],g[N],n,m,k;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>Test;
	for (test=1;test<=Test;test++){
		cin>>m>>k>>n;
		long long sum=0,ans=0,now=0;
		for (int i=0;i<n;i++){
			cin>>a[i];
			sum+=a[i];
		}
		if (sum<=k)
			ans=sum*m;
		else{
			int j=0;
			for (int i=0;i<n;i++){
				if (i){
					now-=a[i-1];
				}
				while (now+a[j]<=k){
					now+=a[j++];
					if (j==n)
						j=0;
				}
				f[i]=now;
				g[i]=j;
			}
			j=0;
			for (int i=0;i<m;i++)
				ans+=f[j],j=g[j];
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	
	return 0;
}
