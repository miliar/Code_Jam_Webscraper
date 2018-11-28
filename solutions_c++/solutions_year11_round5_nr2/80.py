#include<iostream>
#include<stdio.h>
#include<string.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=10002;
int x[maxn],y[maxn],z[maxn],ca,ti,n,i,k;
bool ok(int r){
	int i,j;
	fr(i,1,10000)
		z[i]=x[i];
	memset(y,0,sizeof(y));
	fr(i,1,10000){
		if(z[i]==0)
			continue;
		if(y[i]>=z[i])
			y[i+1]+=z[i];
		else{
			int tmp=z[i]-y[i];
			fr(j,i,i+r-1){
				if(z[j]<tmp)
					return false;
				z[j]-=tmp;
			}
			y[i+r]+=tmp;
			y[i+1]+=y[i];
		}
	}
	return true;
}
int find(int le,int ri){
	if(le==ri)
		return le;
	int mid=(le+ri)/2;
	if(ok(mid+1))
		return find(mid+1,ri);
	else
		return find(le,mid);
}
int main(){
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		memset(x,0,sizeof(x));
		fr(i,1,n){
			cin>>k;
			x[k]++;
		}
		if(n==0)
			cout<<"Case #"<<ti<<": "<<0<<endl;
		else
			cout<<"Case #"<<ti<<": "<<find(1,n)<<endl;
	}
}