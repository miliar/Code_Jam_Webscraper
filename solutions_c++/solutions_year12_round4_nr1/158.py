#include<iostream>
#include<cstdio>
#include<algorithm>
#define x first
#define y second
using namespace std;
typedef long long ll;
int main(){
	ll d,t,n,m,mr;
	cin>>t;
	pair<ll,ll> v[10009];
	ll md[10009];
	for(int z=1;z<=t;z++){
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>v[i].x>>v[i].y;
		}
		cin>>v[n].x;
		v[n].y=0;
		cout<<"Case #"<<z<<": ";
		for(int i=0;i<=n;i++){
			md[i]=0;
		}
		md[0]=v[0].x;
		mr=1;
		for(int i=0;mr<=n && i<n;i++){
			while(mr<=n && v[mr].x<=v[i].x+md[i]){
				md[mr]=v[mr].x-v[i].x;
				if(md[mr]>v[mr].y)
					md[mr]=v[mr].y;
				mr++;
			}
		}
		if(mr<=n)
			cout<<"NO"<<endl;
		else
			cout<<"YES"<<endl;
		//printf("Case #%d: \n",z);
	}
	return 0;
}
