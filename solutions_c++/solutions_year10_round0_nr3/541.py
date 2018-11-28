#include <iostream>
#include <cstdio>
using namespace std;

int g[1100],v[1100];
long long sum[1100];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,cs,r,k,n,i,theNext,per,now,circleLen,theRemain,cnt;
	long long get,oneCircle;
	cin>>t;
	for(cs=1;cs<=t;cs++)
	{
		cout<<"Case #"<<cs<<": ";
		memset(v,0,sizeof(v));
		cin>>r>>k>>n;
		oneCircle=0;
		for(i=0;i<n;i++)
		{
			cin>>g[i];
			oneCircle+=g[i];
		}
		if(oneCircle<=k)
		{
			cout<<oneCircle*r<<endl;
			continue;
		}
		get=0;
		now=r;
		cnt=1;
		theNext=0;
		while(v[theNext]==0)
		{
			if(now==0) break;
			v[theNext]=cnt;
			sum[theNext]=get;
			cnt++;
			per=0;
			for(i=theNext;;i=(i+1)%n)
			{
				per+=g[i];
				if(per>k) break;
			}
			per-=g[i];
			get+=per;
			theNext=i;
			now--;
		}
		if(now==0)
		{
			cout<<get<<endl;
			continue;
		}
		oneCircle=get-sum[theNext];
		circleLen=cnt-v[theNext];
		get+=now/circleLen*oneCircle;
		theRemain=now%circleLen;
		while(theRemain--)
		{
			per=0;
			for(i=theNext;;i=(i+1)%n)
			{
				per+=g[i];
				if(per>k) break;
			}
			theNext=i;
			per-=g[i];
			get+=per;
		}
		cout<<get<<endl;
	}
	return 0;
}
