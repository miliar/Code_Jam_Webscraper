#include<iostream>
using namespace std;
int a[5000];
int main(){
	freopen("C:/A-large.in","r",stdin);
	freopen("C:/A-large.out","w",stdout);
	int t,tt,n,k;
	cin>>tt;
	for(t=1;t<=tt;t++){
		memset(a,0,sizeof(a));
		int i=0;
		cin>>n>>k;
		while(k){
			a[i++]=k%2;
			k/=2;
		}
		for(i=0;i<n;i++)
			if(!a[i]) break;
		if(i==n) cout<<"Case #"<<t<<": ON"<<endl;
		else cout<<"Case #"<<t<<": OFF"<<endl;
	}
}