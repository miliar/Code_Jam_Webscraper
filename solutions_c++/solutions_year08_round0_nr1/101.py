#pragma warning (disable:4786)

#include <iostream>
#include <vector>
#include <map>
#include <string>

#define INF 1000000000
#define N 110
#define M 1010

int ff[N][M];

using namespace std;

int solve(vector<int> &vi,int x,int y,int n)
{
	if(y==-1)
		return 0;
	int i;
	int mn=INF;
	for(i=0;i<n;i++)
	{
		if(i!=vi[y])
		{
			if(ff[i][y-1]==-1)
			{
				ff[i][y-1]=solve(vi,i,y-1,n);
			}
			int f=ff[i][y-1];
			if(i!=x)
				f++;
			if(f<mn)
				mn=f;
		}
	}
	return mn;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int cnt;
	for(cnt=1;cnt<=t;cnt++)
	{
		memset(ff,0xff,sizeof(ff));
		int n;
		map<string,int> ms;
		cin>>n;
		int nn=0;
		int i,j;
		getchar();
		for(i=0;i<n;i++)
		{
			char buf[150];
			cin.getline(buf,150);
			ms[buf]=nn++;
		}
		int q;
		cin>>q;
		getchar();
		vector<int> vi;
		for(j=0;j<q;j++)
		{
			char buf[150];
			cin.getline(buf,150);
			vi.push_back(ms[buf]);
		}
		int res=solve(vi,-1,q-1,n);
		res--;
		if(res<0)
			res=0;
		cout<<"Case #"<<cnt<<": "<<res<<endl;
	}
	return 0;
}
