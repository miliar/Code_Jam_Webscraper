#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std; 
const int maxn=42;
char s[maxn];
int i,j,x[maxn],y[maxn],ca,ti,n,tmp,k,mincost;
bool ok(int a,int b){
	int now=a+1,i,j;
	fr(i,a,n)
		if(i!=b)
			y[now++]=x[i];
	fr(i,a+1,n)
		fr(j,i+1,n)
			if(y[i]>y[j])
				swap(y[i],y[j]);
	fr(i,a+1,n)
		if(y[i]>i)
			return false;
	return true;
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		mincost=0;
		fr(i,1,n){
			scanf("%s",s+1);
			x[i]=0;
			fr(j,1,n)
				if(s[j]=='1')
					x[i]=j;
		}
		fr(i,1,n)
			fr(j,i,n)
				if(ok(i,j)&&x[j]<=i){
					tmp=x[i];
					for(k=j-1;k>=i;--k)
						x[k+1]=x[k];
					x[i]=tmp;
					mincost+=j-i;
					break;
				}
		cout<<"Case #"<<ti<<": "<<mincost<<endl;
	}
}
