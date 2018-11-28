#include<iostream>
#include<cstdio>
#include<algorithm>
#define HM (1000000000LL)
using namespace std;
typedef long long ll;
int main(){
	int t,n;
	cin>>t;
	int s[15];
	ll h[15];
	ll mn,mx;
	bool ip;
	ll smn,smx,st;
	for(int z=1;z<=t;z++){
		cin>>n;
		for(int i=0;i<n-1;i++){
			cin>>s[i];
			s[i]--;
		}
		h[n-1]=HM/2;
		h[n-2]=HM/2;
		cout<<"Case #"<<z<<": ";
		ip=false;
		smn=HM/2;
		smx=HM/2;
		st=HM/8;
		for(int i=n-3;i>=0;i--){
			mn=-1;
			mx=HM+1;
			for(int j=i+1;j<s[i];j++){
				if(mn<h[s[i]]-(s[i]-i)*(h[s[i]]-h[j])/(s[i]-j))
					mn=h[s[i]]-(s[i]-i)*(h[s[i]]-h[j])/(s[i]-j);
			}
			for(int j=s[i]+1;j<n;j++){
				if(mx>h[s[i]]-(s[i]-i)*(h[j]-h[s[i]])/(j-s[i]))
					mx=h[s[i]]-(s[i]-i)*(h[j]-h[s[i]])/(j-s[i]);
			}
			if(mx==HM+1)
				mx=mn+100;
			if(mx>HM)
				mx=HM;
			if(mn==-1)
				mn=mx-100;
			if(mn<0)
				mn=0;
			if(mx<mn){
				ip=true;;
				break;
			}
			h[i]=(mx+mn)/2;
			if(h[i]>smx)
				smx=h[i];
			if(h[i]<smn)
				smn=h[i];
			st/=2;
		}
		if(ip)
			cout<<"Impossible"<<endl;
		else{
			for(int i=0;i<n;i++){
				cout<<h[i];
				if(i==n-1)
					cout<<endl;
				else
					cout<<" ";
			}
		}
		//printf("Case #%d: \n",z);
	}
	return 0;
}
