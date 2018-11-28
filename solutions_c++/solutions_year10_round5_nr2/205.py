#include<iostream>
using namespace std;
long long f[30000];
long long ans,l;
long long a[200],maxl;
int n,tt,tot;
int min(long long a,long long b){
	if(a==-1)return b;
	if(b==-1)return a;
	if(a<b)return a;else return b;
}
void workdp(){
	int i,j;
	for(i=0;i<=20000;i++)f[i]=-1;
	f[0]=0;
	for(i=0;i<n;i++)
		for(j=0;j<=20000;j++)
			if((f[j]!=-1)&&(j+a[i]<=20000))
				f[j+a[i]]=min(f[j+a[i]],f[j]+1);
	return;
}
int main(){
    freopen("bs.in","r",stdin);
    freopen("bs.out","w",stdout);
	int i;
	cin>>tot;
	for(tt=1;tt<=tot;tt++){
		cin>>l>>n;
		for(i=0;i<n;i++)cin>>a[i];
		maxl=a[0];
		for(i=1;i<n;i++)
			if(a[i]>maxl)maxl=a[i];
		workdp();
		ans=-1;
		for(i=0;i<=20000;i++){
            long long p=i;
            long long tp=(l-p)/maxl;
			if((f[i]!=-1)&&((l-p)%maxl==0))
          if((ans==-1)||(ans>f[i]+tp))ans=f[i]+tp;
            }
		cout<<"Case #"<<tt<<": ";
		if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
			else cout<<ans<<endl;
	}
	return 0;
}
