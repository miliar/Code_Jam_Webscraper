#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=100002;
long long x[maxn],v[102],i,j,ca,ti,n;
long long l,ans;
int main(){
	freopen("b0.in","r",stdin);
	freopen("b0.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>l>>n;
		fr(i,0,maxn-1)
			x[i]=maxn;
		x[0]=0;
		fr(i,1,n){
			cin>>v[i];
			long long tmp=v[i];
			fr(j,tmp,maxn-1)
				if(x[j]>x[j-tmp]+1)
					x[j]=x[j-tmp]+1;
		}
		ans=l+1;
		fr(i,0,maxn-1)
			if(i<=l&&x[i]<maxn)
				fr(j,1,n)
					if((l-i)%v[j]==0&&ans>x[i]+(l-i)/v[j])
						ans=x[i]+(l-i)/v[j];
		if(ans>l)
			cout<<"Case "<<ti<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case "<<ti<<": "<<ans<<endl;
						
	}
}