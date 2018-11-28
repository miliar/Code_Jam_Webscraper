#include<iostream>
#include<string>
using namespace std;
int v[105][105],w[105][105];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	cin>>t;
	int cas=1;
	while(t--)
	{
		int n;
		memset(v,0,sizeof(v));
		cin>>n;
		int x1,x2,y1,y2;
		int X=0,Y=0;
		for(int i=0;i<n;i++)
		{
			cin>>x1>>y1>>x2>>y2;
			if(x2>X) X=x2;
			if(y2>Y) Y=y2;
			for(int i=y1;i<=y2;i++)
			{
				for(int j=x1;j<=x2;j++)
					v[i][j]=1;
			}
		}
		if(n==0)
		{
			cout<<"Case #"<<cas++<<": "<<0<<'\n';
			continue;
		}
		int res=0;

	//	cout<<Y<<' '<<X<<'\n';

		int si=1,sj=1;
		while(1)
		{
			memset(w,0,sizeof(w));
			int tot=0;
			while(1)
			{
				if(sj>X)
				{
					si++;sj=1;
				}
				if(v[si][sj]) break;
				sj++;
			}
			int id=(si-1)*X+sj;
			while(id<=X*Y)
			{
				int i=(id-1)/X+1;
				int j=(id-1)%X+1;
				if(v[i][j]==0)
				{
					if(v[i-1][j]&&v[i][j-1])
					{
						w[i][j]=1;
						tot++;
					}
				}
				else
				{
					if(v[i-1][j]==0&&v[i][j-1]==0)
						w[i][j]=0;
					else
					{
						w[i][j]=1;
						tot++;
					}
				}
				id++;
			}
			res++;
			if(tot==0) break;
			for(int i=1;i<=Y;i++)for(int j=1;j<=X;j++)
				v[i][j]=w[i][j];
		}
		cout<<"Case #"<<cas++<<": "<<res<<'\n';
	}
	return 0;
}