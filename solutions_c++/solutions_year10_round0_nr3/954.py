#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int r,k,n,g[1000],a;
long long ans[1000],tot;
int flag[1000];

void solve() {
	memset(ans,0,sizeof(ans));
	a=0;
	for (int i=0;i<1000;i++)
		flag[i]=-1;

	int num,now=0,start;
	for (int i=0;i<r;i++) {
		num=0;
		start=now;
		while (num+g[now]<=k) {
			num+=g[now];
			now++;
			if (now==n)
				now=0;
			if (now==start)
				break;
		}
		ans[a]=num;
//		cout<<a<<": "<<num<<endl;
		flag[start]=a++;
		if (flag[now]!=-1)
			break;
	}

	tot=0;
	for (int i=0;i<a;i++)
		tot+=ans[i];

	long long temp=0;
	for (int i=flag[now];i<a;i++)
		temp+=ans[i];
	
	long long times=(r-a)/(a-flag[now]);
	tot+=(times*temp);
//	cout<<temp<<" "<<times<<endl;

	times=(r-a)%(a-flag[now]);
	for (int i=flag[now];i<a && times--;i++)
		tot+=ans[i];
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>r>>k>>n;
		for (int i=0;i<n;i++)
			scanf("%d",&g[i]);
		solve();
		cout<<"Case #"<<++kase<<": "<<tot<<endl;
	}
	return 0;
}
