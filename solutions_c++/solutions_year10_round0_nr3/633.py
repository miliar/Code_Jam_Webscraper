#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
#define MAXN 1010
#define LL __int64
int r,m,n;
int a[MAXN];
LL last[MAXN];
int vst[MAXN];
LL sum[MAXN];

LL solve(int ca)
{
	LL ans=0,s=0;

	int i,j,k;
	for(i=1,sum[0]=a[0];i<n;i++)
		sum[i]=sum[i-1]+a[i];

//	if(ca==23)cout<<sum[n-1]<<endl;

	if(m>=sum[n-1])return sum[n-1]*r;

	memset(last,0,sizeof(last));
	memset(vst,0,sizeof(vst));
	for(i=0,k=1;k<=r;k++){
		bool flag=false;
		for(s=0,j=i;s+a[j]<=m;){
			s+=a[j];
			if(j==0)flag=true;
			if((++j)>=n)j=0;
		}
		if(j==i)return ans;//a[i]>m, failed to run any longer

		if(flag){
			if(vst[j-1])break;
			last[j-1]=ans+s;
			vst[j-1]=k;
		}
		ans+=s;//如果发生重复，这一次不算
		i=j;
	}

//	if(ca==23)cout<<"ans="<<ans<<endl;
	if(k>r)return ans;

	//k回合后重复，即k-vst[j-1]个回合是一个循环节
	r-=k-1;
	int round=k-vst[j-1];
	LL roundVal=ans+s-last[j-1];
//	if(ca==23)cout<<"round="<<round<<", roundVal="<<roundVal<<endl;

	//现在是从第i个开始
	ans+=roundVal*(r/round);
	r%=round;
	if(r==0)return ans;

	while(r--){
		for(s=0,j=i;s+a[j]<=m;){
			s+=a[j];
			if((++j)>=n)j=0;
		}
		if(j==i)return ans;//a[i]>m, impossible
		ans+=s;
		i=j;
	}
	return ans;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,ca,i;
	for(scanf("%d",&t),ca=1;ca<=t;ca++){
		scanf("%d%d%d",&r,&m,&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		cout<<"Case #"<<ca<<": "<<solve(ca)<<endl;
	}
	return 0;
}