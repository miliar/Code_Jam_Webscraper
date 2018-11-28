#include<iostream>
#include<cstdio>
#include<cstring>
typedef long long key;
using namespace std;
key a[40000010],pri[4000010];
void prime()
{
	memset(a,0,sizeof(a));
	int i,j;
	for(i=2;i<=2000;i++)
		if(!a[i])
			for(j=i*i;j<=4000000;j+=i)
				a[j]=1;
	for(i=0,j=2;j<=4000000;j++)
		if(!a[j]) pri[i++]=j;
}
int solve(key n,key c)
{
	key tmp=c;
	int cnt=0;
	while(tmp<n){
		tmp*=c;
		cnt++;
	}
	if(tmp==n) return cnt;
	return cnt-1;
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
	prime();
	key t,n;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		printf("Case #%d: ",k);
		if(n==1){
			printf("0\n");
			continue;
		}
		int i,j;
		key ans=1;
		for(i=0;pri[i]*pri[i]<=n;i++)
			ans+=solve(n,pri[i]);
		cout<<ans<<endl;
	}
	return 0;
}
