#include<iostream>
#include<map>
#include<cstdio>
using namespace std;

map<int,int> a;

void work(){
	a.clear();
	int n;
	cin>>n;
	for(int i=0,j,k;i<n;i++){
		cin>>j>>k;
		a[j]+=k;
	}
	long long ans=0;
	while(1){
		bool flag=1;
		for(typeof(a.begin()) i=a.begin();i!=a.end();++i)
			if(i->second>=2){
				flag=0;
				ans++;
				a[i->first-1]++;
				a[i->first+1]++;
				a[i->first]-=2;
			}
		if(flag)break;
	}
	cout<<ans<<endl;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n,m=0;
	cin>>n;
	while(n--){
		cout<<"Case #"<<++m<<": ";
		work();
	}
}
