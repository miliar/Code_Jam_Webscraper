#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int ip[]={-1,0,0,1};
int jp[]={0,-1,1,0};

bool valid(int i, int j, int h, int w)
{
	if(i<0||i>=h)return false;
	if(j<0||j>=w)return false;
	return true;
}

int root(int f[], int i)
{
	while(f[i]!=i)
	{
		f[i]=f[f[i]];
		i=f[i];
	}
	return i;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int h,w;
		cin>>h>>w;
		int mount[128][128];
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				cin>>mount[i][j];

		int flow[10240];
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				int mini=mount[i][j];
				int flowi=i;
				int flowj=j;
				for(int d=0;d<4;d++)
				{
					int ii=i+ip[d];
					int jj=j+jp[d];
					if(valid(ii,jj,h,w)==false)continue;

					if(mount[ii][jj]<mini)
					{
						mini=mount[ii][jj];
						flowi=ii;
						flowj=jj;
					}
				}

				flow[i*w+j]=flowi*w+flowj;
			}
		}
		//
		for(int i=0;i<h*w;i++)root(flow,i);

		char ans[128][128];
		char last='a';
		map<int,char> mm;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				int r = root(flow, i*w+j);
				if(mm.find(r)==mm.end())
					mm[r]=last++;

				ans[i][j]=mm[r];
			}
		}

		cout<<"Case #" << t <<":"<<endl;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				if(j)cout<<" ";
				cout<<ans[i][j];
			}
			cout<<endl;
		}
	}
}