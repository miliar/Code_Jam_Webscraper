#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int maxn=1001;

int n,t1,t2,ca;
char ch[maxn],ch1[maxn],ch2[maxn];
int pos[maxn],pos1[maxn],pos2[maxn];

void init()
{
	cin>>n;
	for (int i=1; i<=n; i++) cin>>ch[i]>>pos[i];
	t1=t2=0;
	for (int i=1; i<=n; i++)
		if (ch[i]=='O')
		{	
			++t1;
			ch1[t1]=ch[i];
			pos1[t1]=pos[i];
		} else
		{
			++t2;
			ch2[t2]=ch[i];
			pos2[t2]=pos[i];
		}
}

void solve()
{
	int now,ans=0;
	if (t1==0 || t2==0)
	{
		now=1;
		for (int i=1; i<=n; i++)
		{
			ans+=abs(pos[i]-now)+1;
			now=pos[i];
		}
		cout<<ans<<endl;
		return;
	}

	int time1=abs(pos1[1]-1)+1, time2=abs(pos2[1]-1)+1;
	int p1=1, p2=1;
	for (int i=1; i<=n; i++)
	{
		if (ch[i]=='O')
		{
			ans+=time1;
			time2-=time1;
			if (p2>t2) time2=0; else time2=max(1,time2);
			time1=abs(pos1[p1+1]-pos1[p1])+1;
			if (p1==t1) time1=0;
			++p1;
		} else
		{
			ans+=time2;
			time1-=time2;
			if (p1>t1) time1=0; else time1=max(1,time1);
			time2=abs(pos2[p2+1]-pos2[p2])+1;
			if (p2==t2) time2=0;
			++p2;
		}
	}
	if (time1>0) ans+=time1; else 
	if (time2>0) ans+=time2;
	cout<<ans<<endl;
}

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
	cin>>ca;
	for (int i=1; i<=ca; i++)
	{
		cout<<"Case #"<<i<<": ";
		init();
		solve();
	}
}
