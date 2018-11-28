#include<iostream>
#include<cstring>
#include<queue>
using namespace std;

int d[10005],l[10005];
queue<int> q;

int Min(int x,int y) { return x<y?x:y;} 

int main()
{
	freopen("a.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int T,tc,D,n,i,x,y,f;
	cin>>T;
	for(tc=1;tc<=T;tc++)
	{
		cin>>n;
		for(i=0;i<n;i++)
			cin>>d[i]>>l[i];
		cin>>D;
		d[n]=D; l[n]=1;
		while(!q.empty())
			q.pop();
		if(d[0]>l[0])
		{
			cout<<"Case #"<<tc<<": NO"<<endl;
			continue;
		}
		q.push(0);
		q.push(d[0]);
		f=0;
		while(!q.empty())
		{
			x=q.front(); q.pop();
			y=q.front(); q.pop();
			if(x==n)
			{
				f=1;
				break;
			}
			for(i=x+1;i<=n&&d[i]-d[x]<=y;i++)
			{
				q.push(i);
				q.push(Min(l[i],d[i]-d[x]));
			}
		}
		if(f)
			cout<<"Case #"<<tc<<": YES"<<endl;
		else
			cout<<"Case #"<<tc<<": NO"<<endl;
	}
	return 0;
}




