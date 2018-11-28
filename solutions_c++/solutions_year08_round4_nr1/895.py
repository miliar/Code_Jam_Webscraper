#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

typedef long long intl;

#define MAX 10000

bool gate[MAX+1];
bool chg[MAX+1];
bool val[MAX+1];

int nchg[MAX+1][2];
int m;

int main()
{
	int cc;
	cin>>cc;
	for(int ci=1;ci<=cc;ci++)
	{
		bool v;
		cin>>m>>v;
		int i,j;
		for(i=1;i<=(m-1)/2;i++) cin>>gate[i]>>chg[i];
		for(;i<=m;i++) cin>>val[i];

		memset(nchg,-1,sizeof(nchg));

		for(i=(m-1)/2+1;i<=m;i++) nchg[i][val[i]]=0;

		for(i=(m-1)/2;i>=1;i--)
		{
			if(nchg[2*i][0]!=-1&&nchg[2*i+1][0]!=-1)
			{
				if(chg[i])
				{
					if(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][0]+(gate[i]==false)<nchg[i][0])
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][0]+(gate[i]==false);
					if(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][0]+(gate[i]==true)<nchg[i][0])
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][0]+(gate[i]==true);
				}
				else
				{
					if(gate[i]==true&&(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][0]<nchg[i][0]))
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][0];
					if(gate[i]==false&&(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][0]<nchg[i][0]))
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][0];
				}
			}
			if(nchg[2*i][0]!=-1&&nchg[2*i+1][1]!=-1)
			{
				if(chg[i])
				{
					if(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][1]+(gate[i]==false)<nchg[i][0])
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][1]+(gate[i]==false);
					if(nchg[i][1]==-1||nchg[2*i][0]+nchg[2*i+1][1]+(gate[i]==true)<nchg[i][1])
						nchg[i][1]=nchg[2*i][0]+nchg[2*i+1][1]+(gate[i]==true);
				}
				else
				{
					if(gate[i]==true&&(nchg[i][0]==-1||nchg[2*i][0]+nchg[2*i+1][1]<nchg[i][0]))
						nchg[i][0]=nchg[2*i][0]+nchg[2*i+1][1];
					if(gate[i]==false&&(nchg[i][1]==-1||nchg[2*i][0]+nchg[2*i+1][1]<nchg[i][1]))
						nchg[i][1]=nchg[2*i][0]+nchg[2*i+1][1];
				}
			}
			if(nchg[2*i][1]!=-1&&nchg[2*i+1][0]!=-1)
			{
				if(chg[i])
				{
					if(nchg[i][0]==-1||nchg[2*i][1]+nchg[2*i+1][0]+(gate[i]==false)<nchg[i][0])
						nchg[i][0]=nchg[2*i][1]+nchg[2*i+1][0]+(gate[i]==false);
					if(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][0]+(gate[i]==true)<nchg[i][1])
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][0]+(gate[i]==true);
				}
				else
				{
					if(gate[i]==true&&(nchg[i][0]==-1||nchg[2*i][1]+nchg[2*i+1][0]<nchg[i][0]))
						nchg[i][0]=nchg[2*i][1]+nchg[2*i+1][0];
					if(gate[i]==false&&(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][0]<nchg[i][1]))
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][0];
				}
			}
			if(nchg[2*i][1]!=-1&&nchg[2*i+1][1]!=-1)
			{
				if(chg[i])
				{
					if(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][1]+(gate[i]==false)<nchg[i][1])
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][1]+(gate[i]==false);
					if(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][1]+(gate[i]==true)<nchg[i][1])
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][1]+(gate[i]==true);
				}
				else
				{
					if(gate[i]==true&&(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][1]<nchg[i][1]))
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][1];
					if(gate[i]==false&&(nchg[i][1]==-1||nchg[2*i][1]+nchg[2*i+1][1]<nchg[i][1]))
						nchg[i][1]=nchg[2*i][1]+nchg[2*i+1][1];
				}
			}
		}

		//for(i=1;i<=m;i++)
		//{
		//	for(j=0;j<2;j++) cout<<nchg[i][j]<<" ";
		//	cout<<endl;
		//}
		
		cout<<"Case #"<<ci<<": ";
		if(nchg[1][(int)v]==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<nchg[1][(int)v]<<endl;
	}

	return 0;
}
