#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n,k;
vector<string>vs;
string str;
int r;
int dir[4][2]={0,1,1,0,1,1,1,-1};
void roate()
{
	r=vs.size();
	for(int i=0;i<r;i++)
	{
		int kk=r-1;
		int j;
		for(j=r-1;kk>=0&&j>=0;j--,kk--)
		{
			while(kk>=0&&vs[i][kk]=='.')
				kk--;
			if(kk>=0)
				vs[i][j]=vs[i][kk];
			else j++;
		}
		while(j>=0)
		{
			vs[i][j]='.';
			j--;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n>>k;
		vs.clear();
		for(int i=0;i<n;i++)
		{
			cin>>str;
			vs.push_back(str);
		}
	
		roate();
		//for(int i=0;i<n;i++)
		//	cout<<vs[i]<<endl;
		bool blue=false,red=false;
		for(int i=0;i<r;i++)
			for(int j=0;j<r;j++)
			{
				if(vs[i][j]=='.')
					continue;
				for(int s=0;s<4;s++)
				{
					int ti=i+dir[s][0]*(k-1);
					int tj=j+dir[s][1]*(k-1);
					if(ti>=0&&ti<r&&tj>=0&&tj<r)
					{
						int kk;
						for(kk=1;kk<k;kk++)
						{
							if(vs[i+dir[s][0]*kk][j+dir[s][1]*kk]!=vs[i][j])
								break;
						}
						if(kk==k)
						{
							if(vs[i][j]=='R')
								red=true;
							else if(vs[i][j]=='B')
								blue=true;
						}
					}
				}
			}
		cout<<"Case #"<<t<<": ";
		if(red==false&&blue==false)
		{
			cout<<"Neither"<<endl;
		}
		else if(red==true&&blue==true)
		{
			cout<<"Both"<<endl;
		}
		else if(red==true)
		{
			cout<<"Red"<<endl;
		}
		else
		{
			cout<<"Blue"<<endl;
		}
		/*for(int kk=j-1;kk>=0&&kk>=j-k+1;kk--)
		if(vs[i][j]!=vs[i][kk])
		break;
		if(kk==j-k)
		{
		if(vs[i][j]=='R')
		red=true;
		if(vs[i][j]=='B')
		blue=true;
		}
		for(int j=r-1;j>=0;j--)
			{
				for(int i=0;i<r;i++)
				{
					if(vs[i][j]=='.')
						continue;
					for(int kk=i+1;kk<r;kk<=i+k-1;kk++)
						if(vs[i][j]!=vs[kk][j])
							break;
					if(kk==i+k)
					{
						if(vs[i][j]=='R')
							red=true;
						if(vs[i][j]=='B')
							blue=true;
					}
				}
			}*/
	
			
	}
	return 0;
}