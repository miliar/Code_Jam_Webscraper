#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <cmath>
#include <map>

using namespace std;
int N,K,B,T;
struct check
{
	int x,v;
}C[51];
int tt[51];
bool cmp(check a,check b)
{
	return a.x>=b.x;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int TT;
	cin>>TT;
	for(int t=1;t<=TT;t++)
	{
		cin>>N>>K>>B>>T;
		for(int i=0;i<N;i++)
			scanf("%d",&C[i].x);
		for(int i=0;i<N;i++)
			scanf("%d",&C[i].v);
		sort(C,C+N,cmp);
		for(int i=0;i<N;i++)
			tt[i]=C[i].v*T+C[i].x-B;
		int cannot=0;
		int can=0;
		int ans=0;
		for(int i=0;i<N;i++)
		{
			if(tt[i]<0)
				cannot++;
			else
				ans+=cannot,can++;
			if(can==K)
				break;
		}
		cout<<"Case #"<<t<<": ";
		if(can==K)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}