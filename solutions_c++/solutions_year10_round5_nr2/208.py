#include<iostream>
using namespace std;
const int maxn=40000;
__int64 f[maxn];
__int64 pq,l;
__int64 a[200],maxs;
int n,tt,tot;
int min(__int64 a,__int64 b){
	if(a==-1)return b;
	if(b==-1)return a;
	if(a<b)return a;else return b;
}
void workdp(){
	int i,j;
	for(i=0;i<=maxn;i++)f[i]=-1;
	f[0]=0;
	for(i=0;i<n;i++)
		for(j=0;j<=maxn;j++)
			if((f[j]!=-1)&&(j+a[i]<=maxn))
				f[j+a[i]]=min(f[j+a[i]],f[j]+1);
	return;
}
int main(){
	int i;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>tot;
	for(tt=1;tt<=tot;tt++){
		cin>>l>>n;
		for(i=0;i<n;i++)cin>>a[i];
		maxs=a[0];
		for(i=1;i<n;i++)
			if(a[i]>maxs) maxs=a[i];
		workdp();
		pq=-1;
		for(i=0;i<=maxn;i++){
            __int64 p=i;
            __int64 tp=(l-p)/maxs;
			if((f[i]!=-1)&&((l-p)%maxs==0))
          if((pq==-1)||(pq>f[i]+tp))pq=f[i]+tp;
            }
		cout<<"Case #"<<tt<<": ";
		if(pq==-1)cout<<"IMPOSSIBLE"<<endl;
			else cout<<pq<<endl;
	}
	return 0;
}
